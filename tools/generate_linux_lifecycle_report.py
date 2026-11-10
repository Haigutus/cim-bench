"""Render the pinned Linux native-model cohort, including coverage limitations.

Usage: python tools/generate_linux_lifecycle_report.py COHORT_DIRECTORY
Requires matplotlib==3.10.8; the directory contains comparison.json and raw/.
"""
import hashlib
import json
from pathlib import Path
import sys

from generate_lifecycle_report import DATASETS, QUERIES, plt, point, save as save_figure

LABELS = {
    'stable': 'PowerIO da32f73e', 'rc': 'PowerIO 3abeee34',
    'cimoxide': 'cimoxide 0.3.3', 'veragrid': 'VeraGrid 6.7.7',
    'libcimpp': 'libcimpp',
}
COLORS = {
    'stable': '#677993', 'rc': '#147D70', 'cimoxide': '#BD6427',
    'veragrid': '#6D51A5', 'libcimpp': '#343434',
}


def save(fig, directory, name):
    save_figure(fig, directory, name)
    path = directory / (name + '.svg')
    path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines()) + '\n')


def main(directory):
    report = json.loads((directory/'comparison.json').read_text())
    for entry in report['raw_manifest']:
        assert hashlib.sha256((directory/'raw'/entry['file']).read_bytes()).hexdigest() == entry['sha256']
    participants = report['participants']
    rows = {(r['dataset'], r['query_mode'], r['participant']): r for r in report['rows']}
    graphs = directory/'graphs'
    graphs.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'svg.hashsalt': 'cim-bench-linux-lifecycle-v1'})
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for i, (dataset, title) in enumerate(DATASETS.items()):
        available = [p for p in participants if (dataset, 'all', p) in rows]
        for j, (metric, scale, ylabel) in enumerate([
            ('load_to_use_ns', 1e6, 'Load + four first queries (ms, log scale)'),
            ('peak_rss_bytes_after_warm', 2**20, 'Process high-water RSS (MiB)'),
        ]):
            ax = axes[i, j]
            for k, kind in enumerate(available):
                point(ax, rows[dataset, 'all', kind]['metrics'][metric], k, scale, COLORS[kind])
            ax.set_xticks(range(len(available)), [LABELS[p].replace(' ', '\n', 1) for p in available])
            ax.set_title(title)
            ax.set_ylabel(ylabel)
            ax.grid(axis='y', alpha=0.2)
            if j == 0:
                ax.set_yscale('log')
            else:
                ax.set_ylim(bottom=0)
    fig.suptitle('Linux ARM64 native-model lifecycle · seven independent processes per group', fontsize=13)
    fig.text(.5, .01, 'Points: independent runs; bars: pointwise 95% bootstrap median intervals.\nlibcimpp CGMES 3 is unmeasured: the pinned image implements CIM16. Native counts are not equivalent across tools.',
             ha='center', fontsize=9)
    fig.tight_layout(rect=(0, .065, 1, .96))
    save(fig, graphs, 'lifecycle_comparison')

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for i, (dataset, title) in enumerate(DATASETS.items()):
        available = [p for p in participants if (dataset, 'all', p) in rows]
        for j, stage in enumerate(('first', 'warm')):
            ax = axes[i, j]
            for k, query in enumerate(QUERIES):
                for p, kind in enumerate(available):
                    point(ax, rows[dataset, query, kind]['metrics'][f'{query}_{stage}_ns'],
                          k, 1000, COLORS[kind], (p-(len(available)-1)/2)*.15)
            ax.set_xticks(range(len(QUERIES)), QUERIES)
            ax.set_title(f'{title} · {stage} query')
            ax.set_ylabel('Microseconds per call (log scale)')
            ax.set_yscale('log')
            ax.grid(axis='y', alpha=.2)
    handles = [plt.Line2D([], [], color=COLORS[p], marker='o', linestyle='', label=LABELS[p]) for p in participants]
    fig.legend(handles=handles, loc='upper center', bbox_to_anchor=(.5, .96), ncol=3)
    fig.suptitle('Isolated first queries and warm calls · one selected query per fresh process', fontsize=13)
    fig.text(.5, .01, 'Warm samples reduce nine calibrated batches to one median per process; timer and loop overhead remain.\nCached scalar access, scans and native model construction are different work; all raw counts accompany this figure.',
             ha='center', fontsize=9)
    fig.tight_layout(rect=(0, .065, 1, .87))
    save(fig, graphs, 'first_warm_queries')

    lines = ['# Linux ARM64 native lifecycle comparison', '',
        'This cohort contains all 315 planned independent processes: seven repeats, five query modes, two datasets for four participants, and RealGrid for the CIM16 libcimpp image. All invocations succeeded. The interrupted earlier harness attempt is retained separately and is not a tool failure or part of these timings.', '',
        f"Harness: `{report['harness_commit']}`. PowerIO sources: stable `{report['builds']['stable']['source_commit']}` and historical RC `{report['builds']['rc']['source_commit']}`.", '',
        'The RC head changed to `4dcd881266b943f4405351e9e4f2aef30039a8b1` during measurement. This cohort does not qualify that newer head.', '',
        'PowerIO builds use the same immutable builder, release mode, locked dependencies, default features plus `gridfm`, and Rust 1.99.0. All runtime images use Python 3.14.6. Every participant uses a pinned image in the same Linux ARM64 Podman VM, with eight CPUs and 16,714,772,480 bytes of RAM. Each run uses a new container, no network, and the same read-only inputs. Filesystem caches are uncontrolled; no CPU affinity is set. The comparison does not establish matched compiler optimizations across different competitors.', '',
        report['method'], '',
        '![Lifecycle timing and memory](graphs/lifecycle_comparison.svg)', '',
        'The historical RC regresses on Svedala. RealGrid does not establish an improvement over stable. Ratios below are paired within repeat blocks; values above one are slower.', '',
        '| Case | Query mode | RC / stable load-to-use | Pointwise 95% interval |',
        '|---|---|---:|---:|']
    for entry in report['paired_rc_stable']:
        if entry['metric'] == 'load_to_use_ns':
            low, high = entry['bootstrap_paired_median_95pct']
            lines.append(f"| {DATASETS[entry['dataset']]} | {entry['query_mode']} | {entry['median_ratio']:.4f} | [{low:.4f}, {high:.4f}] |")
    lines += ['', '![First and warm query latency](graphs/first_warm_queries.svg)', '',
        'Each single-query mode measures its first call on a freshly loaded model. Earlier calls may initialize later queries in `all` mode. Load-to-use sums load and the selected first calls; import-to-use also includes adapter import/construction. Neither includes instrumentation between stages or container/process startup.', '',
        '## Counts and applicability', '',
        '| Case | Participant | Lines | Generators | Loads | Substations |', '|---|---|---:|---:|---:|---:|']
    for dataset in DATASETS:
        for kind in participants:
            row = rows.get((dataset, 'all', kind))
            counts = ' | '.join('/'.join(map(str, row['counts'][q])) for q in QUERIES) if row else 'unmeasured | unmeasured | unmeasured | unmeasured'
            lines.append(f'| {DATASETS[dataset]} | {LABELS[kind]} | {counts} |')
    lines += ['', 'PowerIO includes equivalent injections in its load table. Svedala counts disagree across participants; matching RealGrid counts alone does not prove equivalent fields or work. These observations do not prove a cross-tool ranking or universal first place.', '',
        'libcimpp on Svedala is a coverage gap in this pinned CIM16 build, not evidence that every libcimpp configuration lacks CGMES 3 support. PyPowSyBl was measured in the separate native macOS cohort; its pinned Linux ARM64 wheel is unavailable. RDF/triplestore, CLI, fresh-export and other platform groups are outside this cohort.', '',
        '## Provenance and limitations', '',
        'Image IDs and installed package inventories are recorded for every participant. The libcimpp adapter reports `2.2.0` as a literal; that string alone does not independently verify its upstream source revision. Competitor source-build reproducibility remains incomplete even though the exact executable images are pinned. Missing Git inside libcimpp is recorded as a provenance-observation error after timing and does not discard its measurements.', '']
    lines += ['- '+item for item in report['limitations']]
    lines += ['', '## Raw results and reproduction', '',
        '- [Comparison JSON](comparison.json) preserves all process samples and descriptive uncertainty.',
        '- [Plan](raw/plan.json) records image identities, source commits, random seed, exclusions, timeout and order. `raw/*-packages.json` records installed package versions.',
        '- `raw/` contains each result, invocation receipt and losslessly compressed stdout/stderr log. [The manifest](manifest.json) hashes every artifact; `.log.gz` files decompress to the original log bytes.',
        '- [Reproduction scripts](reproduce/) preserve the original runner and reducer. Configure local paths and obtain the exact input and image identities before repeating; cached image identities are not a portable source-build recipe.',
        '- Regenerate figures with `python tools/generate_linux_lifecycle_report.py results-native-lifecycle/2026-11-10-linux-arm64` using `matplotlib==3.10.8`.', '',
        'The earlier interrupted attempt is retained in `superseded-attempt/`; it demonstrates the harness failure and is excluded by provenance, never by measured speed.', '']
    (directory/'comparison_summary.md').write_text('\n'.join(lines))
    manifest = [dict(file=str(p.relative_to(directory)), bytes=p.stat().st_size,
                     sha256=hashlib.sha256(p.read_bytes()).hexdigest())
                for p in sorted(directory.rglob('*')) if p.is_file() and p.name != 'manifest.json']
    (directory/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(directory/'comparison_summary.md')


if __name__ == '__main__':
    main(Path(sys.argv[1]))
