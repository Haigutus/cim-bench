"""Render matched PowerIO namespace-cache evidence with all groups and caveats."""
import hashlib
import json
from pathlib import Path
import sys

from generate_lifecycle_report import plt, point, save

CASES = {'svedala_igm_cgmes_3': 'Svedala · CGMES 3.0', 'realgrid_cgmes_2_4': 'RealGrid · CGMES 2.4.15'}
PLATFORMS = {'native': 'macOS ARM64', 'linux': 'Linux ARM64 VM'}
KINDS = [('baseline', '#677993', 'Baseline 4dcd8812'), ('candidate', '#147D70', 'Candidate 2d570215')]
QUERIES = ['lines', 'generators', 'loads', 'substations']


def main(directory):
    report = json.loads((directory / 'comparison.json').read_text())
    for entry in report['raw_manifest']:
        assert hashlib.sha256((directory / 'raw' / entry['file']).read_bytes()).hexdigest() == entry['sha256']
    rows = {(r['platform'], r['dataset'], r['query'], r['participant']): r for r in report['rows']}
    graphs = directory / 'graphs'
    graphs.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'svg.hashsalt': 'namespace-cache-20261110'})
    for platform, title in PLATFORMS.items():
        fig, axes = plt.subplots(2, 2, figsize=(10, 7.5))
        for i, (case, label) in enumerate(CASES.items()):
            for j, (metric, unit, ylabel) in enumerate([
                ('load_to_use_ns', 1e6, 'Load + four first queries (ms)'),
                ('after_warm_peak_rss_bytes', 2**20, 'Process high-water RSS (MiB)'),
            ]):
                ax = axes[i, j]
                for index, (kind, color, name) in enumerate(KINDS):
                    point(ax, rows[platform, case, 'all', kind]['metrics'][metric], index, unit, color)
                ax.set_xticks([0, 1], [x[2].replace(' ', '\n') for x in KINDS])
                ax.set_title(label)
                ax.set_ylabel(ylabel)
                ceiling = max(max(rows[platform, case, 'all', kind]['metrics'][metric]['samples']) for kind, _, _ in KINDS)
                ax.set_ylim(0, ceiling / unit * 1.12)
                ax.grid(axis='y', alpha=.2)
        fig.suptitle(f'{title} · load-to-use and memory', fontsize=14)
        fig.text(.5, .01, 'Seven independent processes per build/case/mode; points retain every observation.\nBars: pointwise 95% bootstrap median intervals. Same PowerIO workload; no competitor ranking.', ha='center', fontsize=9)
        fig.tight_layout(rect=(0, .065, 1, .96))
        save(fig, graphs, platform + '_lifecycle')
        fig, axes = plt.subplots(2, 2, figsize=(11, 7.5))
        for i, (case, label) in enumerate(CASES.items()):
            for j, stage in enumerate(('first', 'warm')):
                ax = axes[i, j]
                scale = 1000 if stage == 'first' else 1
                for index, query in enumerate(QUERIES):
                    for (kind, color, name), offset in zip(KINDS, (-.12, .12)):
                        point(ax, rows[platform, case, query, kind]['metrics'][f'{query}_{stage}_ns'], index, scale, color, offset)
                ax.set_xticks(range(4), QUERIES)
                ax.set_title(f'{label} · {stage} call')
                values = [v for r in report['rows'] if r['query'] in QUERIES
                          for v in r['metrics'][f"{r['query']}_{stage}_ns"]['samples']]
                if stage == 'first':
                    ax.set_ylabel('Microseconds per call (log scale)')
                    ax.set_yscale('log')
                    ax.set_ylim(min(values) / scale * .8, max(values) / scale * 1.15)
                    ax.set_yticks([5, 10, 20, 50], ['5', '10', '20', '50'])
                else:
                    ax.set_ylabel('Nanoseconds per call')
                    ax.set_ylim(0, max(values) * 1.15)
                ax.grid(axis='y', alpha=.2)
        fig.suptitle(title + ' · isolated first and warm queries', fontsize=14)
        fig.legend(handles=[plt.Line2D([], [], color=c, marker='o', linestyle='', label=n) for _, c, n in KINDS],
                   loc='upper center', bbox_to_anchor=(.5, .96), ncol=2)
        fig.text(.5, .01, 'Single-query groups use a fresh process/model. Warm observations are per-process medians of nine calibrated batches.\nFirst calls include invocation/timer overhead; intervals are descriptive and uncorrected across groups.', ha='center', fontsize=9)
        fig.tight_layout(rect=(0, .065, 1, .90))
        save(fig, graphs, platform + '_queries')
    fig, axes = plt.subplots(1, 2, figsize=(12, 6.5), sharex=True)
    for ax, platform in zip(axes, PLATFORMS):
        groups = [r for r in report['paired'] if r['platform'] == platform]
        labels = []
        for index, row in enumerate(groups):
            value = row['candidate_over_baseline']['load_to_use_ns']
            mid = value['median']; lo, hi = value['bootstrap_median_95pct']
            labels.append(CASES[row['dataset']].split(' · ')[0] + ' / ' + row['query'])
            ax.scatter(value['samples'], [index] * 7, color='#677993', alpha=.35, s=16)
            ax.errorbar(mid, index, xerr=[[mid-lo], [hi-mid]], fmt='o', color='#147D70', capsize=4)
        ax.axvline(1, linestyle='--', color='#444444', linewidth=1)
        ax.set_yticks(range(len(groups)), labels)
        ax.invert_yaxis()
        ax.set_title(PLATFORMS[platform])
        ax.set_xlabel('Candidate / baseline load-to-use (lower is faster)')
        ax.grid(axis='x', alpha=.2)
    fig.suptitle('Paired load-to-use ratios · all 20 groups', fontsize=14)
    fig.text(.5, .01, 'Dots: seven repeat-block ratios. Intervals: pointwise 95% bootstrap medians; no familywise correction.\nSvedala all-query intervals include 1 on both platforms. Shared host; warm uncontrolled file caches.', ha='center', fontsize=9)
    fig.tight_layout(rect=(0, .07, 1, .95))
    save(fig, graphs, 'paired_load_to_use')
    for path in graphs.glob('*.svg'):
        path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines()) + '\n')
    lines = ['# CGMES namespace-cache experiment', '',
        'All 280 predeclared serial fresh-process runs succeeded: seven independent repeats × two builds × two platforms × two cases × five query selections. This compares PowerIO before and after one internal cache change; it is not a competitor ranking.', '',
        'Baseline: `4dcd881266b943f4405351e9e4f2aef30039a8b1`. Candidate: `2d570215aea1b0dc7d0257e0b0909753869253fb`. Harness: `ea5444916ef4d038ebf514b4617ec078f83914da`.', '',
        'Both builds use release mode, locked dependencies, default features plus `gridfm`, and maturin 1.16.0. Native builds use Rust 1.98.1/Python 3.13.18; Linux builds use the same pinned Rust 1.99.0 builder image and Python 3.14 runtime. Platforms are analyzed separately. The 18-core Apple M5 Pro/64 GiB desktop and its 8-CPU/16 GiB Linux VM are shared environments, without affinity or file-cache flushing. Per-run ambient observations are retained.', '',
        report['method'], '',
        'The paired median RealGrid all-query load-to-use ratio is 0.9732 [0.9633, 0.9800] on macOS and 0.9450 [0.9408, 0.9541] on Linux. Svedala all-query ratios are 0.9611 [0.9233, 1.0333] and 0.9200 [0.8362, 1.0023]; these intervals do not establish a Svedala improvement. These are descriptive pointwise intervals from seven pairs, not guarantees or multiple-comparison-adjusted claims.', '',
        '![All paired ratios](graphs/paired_load_to_use.svg)', '',
        '| Platform | Case | Query selection | Candidate / baseline load-to-use [95% interval] | Baseline → candidate, ms | Peak RSS, MiB |',
        '|---|---|---|---:|---:|---:|']
    for entry in report['paired']:
        p, case, query = entry['platform'], entry['dataset'], entry['query']
        ratio = entry['candidate_over_baseline']['load_to_use_ns']; lo, hi = ratio['bootstrap_median_95pct']
        a, b = [rows[p, case, query, kind]['metrics'] for kind, _, _ in KINDS]
        lines.append(f"| {PLATFORMS[p]} | {CASES[case]} | {query} | {ratio['median']:.4f} [{lo:.4f}, {hi:.4f}] | {a['load_to_use_ns']['median']/1e6:.3f} → {b['load_to_use_ns']['median']/1e6:.3f} | {a['after_warm_peak_rss_bytes']['median']/2**20:.2f} → {b['after_warm_peak_rss_bytes']['median']/2**20:.2f} |")
    lines += ['', '## Query costs and memory', '',
        'The optimization caches at most 512 bytes of a recognized CIM namespace per document during parsing. Query code is unchanged, but measured query latency is not uniformly lower. The Linux RealGrid isolated first generator query has a paired ratio of 1.0975 [1.0583, 1.1857]; several warm-query groups also have pointwise intervals above 1. All such observations remain in the comparison JSON and figures. These small, uncorrected comparisons do not by themselves identify a causal query-code regression.', '',
        'Native RealGrid all-query median peak RSS rises from 311.83 to 314.16 MiB in this cohort; the paired interval includes 1. RSS includes interpreter/import and allocator effects and is not a measurement of the cache allocation itself. No uniform memory reduction is claimed.', '']
    for platform in PLATFORMS:
        lines += [f'![{PLATFORMS[platform]} lifecycle](graphs/{platform}_lifecycle.svg)', '', f'![{PLATFORMS[platform]} queries](graphs/{platform}_queries.svg)', '']
    lines += ['## Correctness qualification', '',
        '- All four required local gates pass at candidate 2d570215: formatting, workspace tests, C ABI tests and all seven Clippy configurations. All 131 focused CGMES regressions pass, including namespace rebinding and bounded-cache cases.',
        '- Both measured cases have byte-identical complete IR, retained replay, fresh CGMES output, IR-restored fresh output and ordered diagnostics across the two wheels. Raw network outputs are retained locally; hashes and reproduction scripts are included.',
        '- Native PowSyBl 1.16.1 passes 24 synthetic transformer/tap cases for each wheel, both before and after PowerIO CGMES re-import. It checks physical impedance, rated voltages and every phase-tap step and detects altered negative controls. This does not test power-flow solves or comprehensive CGMES conformance.',
        '- Two harness setup errors are preserved: the first fidelity capture lacked the RealGrid input link; the first native-oracle negative control attempted to mutate linear tap fields after canonical re-emission had correctly made them tabular. The corrected v2 oracle changes the relevant fields explicitly and requires at least one mutation. No library failure was suppressed.', '',
        '## Limits', ''] + ['- ' + x for x in report['limitations']]
    lines += ['', '## Evidence and reproduction', '',
        '- [Comparison JSON](comparison.json) retains every reduced process sample, first/warm metric, memory phase, paired ratio and input fingerprint.',
        '- [Plan](raw/plan.json), raw invocation/results, [build receipts](builds/), [qualification receipts](qualification/) and [manifest](manifest.json) pin sources, compilers, options, wheels, container images and inputs. Logs are losslessly compressed.',
        '- [Reproduction scripts](reproduce/) preserve the host commands; configure equivalent local paths and obtain the pinned source/data commits. No dataset or wheel binaries are vendored.',
        '- Regenerate this report with `python tools/generate_namespace_report.py results-native-lifecycle/2026-11-10-cgmes-namespace-cache` using `matplotlib==3.10.8`.', '']
    (directory / 'comparison_summary.md').write_text('\n'.join(lines))
    manifest = [dict(file=str(p.relative_to(directory)), bytes=p.stat().st_size, sha256=hashlib.sha256(p.read_bytes()).hexdigest())
                for p in sorted(directory.rglob('*')) if p.is_file() and p.name != 'manifest.json']
    (directory / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(directory / 'comparison_summary.md')


if __name__ == '__main__':
    main(Path(sys.argv[1]))
