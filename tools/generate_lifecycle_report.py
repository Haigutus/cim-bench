"""Render lifecycle JSON as separate Markdown/SVG evidence, never pytest rankings.

Usage: python tools/generate_lifecycle_report.py COHORT_DIRECTORY
Requires matplotlib==3.10.8. The cohort contains comparison.json and raw/.
"""
import hashlib
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PARTICIPANTS = ('stable', 'rc', 'pypowsybl')
LABELS = {'stable': 'PowerIO da32f73e', 'rc': 'PowerIO 3abeee34', 'pypowsybl': 'PyPowSyBl 1.16.1'}
COLORS = {'stable': '#677993', 'rc': '#147D70', 'pypowsybl': '#BD6427'}
DATASETS = {'svedala_igm_cgmes_3': 'Svedala · CGMES 3.0', 'realgrid_cgmes_2_4': 'RealGrid · CGMES 2.4.15'}
QUERIES = ('lines', 'generators', 'loads', 'substations')


def point(ax, metric, position, scale, color, offset=0):
    samples = metric['samples']
    x = [position + offset + (i - (len(samples)-1)/2)*0.017 for i in range(len(samples))]
    ax.scatter(x, [v/scale for v in samples], color=color, s=14, alpha=0.4)
    mid = metric['median']/scale
    low, high = [x/scale for x in metric['bootstrap_median_95pct']]
    ax.errorbar(position+offset, mid, yerr=[[mid-low], [high-mid]], fmt='o',
                color=color, capsize=4, markersize=5, linewidth=1.5)


def save(fig, graphs, stem):
    fig.savefig(graphs/(stem+'.svg'), bbox_inches='tight', metadata={'Date': None})
    fig.savefig(graphs/(stem+'.png'), bbox_inches='tight', dpi=140)
    plt.close(fig)


def main(directory):
    report = json.loads((directory/'comparison.json').read_text())
    for entry in report['raw_manifest']:
        assert hashlib.sha256((directory/'raw'/entry['file']).read_bytes()).hexdigest() == entry['sha256']
    rows = {(r['dataset'], r['query_mode'], r['participant']): r for r in report['rows']}
    graphs = directory/'graphs'
    graphs.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'svg.hashsalt': 'cim-bench-lifecycle-v1'})
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.5))
    for i, (dataset, title) in enumerate(DATASETS.items()):
        for j, (metric, scale, ylabel) in enumerate([
            ('load_to_use_ns', 1e6, 'Load + four first queries (ms, log scale)'),
            ('peak_rss_bytes_after_warm', 2**20, 'Process high-water RSS (MiB)'),
        ]):
            ax = axes[i, j]
            for k, kind in enumerate(PARTICIPANTS):
                point(ax, rows[dataset, 'all', kind]['metrics'][metric], k, scale, COLORS[kind])
            ax.set_xticks(range(3), [LABELS[p].replace(' ', '\n', 1) for p in PARTICIPANTS])
            ax.set_title(title)
            ax.set_ylabel(ylabel)
            ax.grid(axis='y', alpha=0.2)
            if j == 0:
                ax.set_yscale('log')
            else:
                ax.set_ylim(bottom=0)
    fig.suptitle('Native macOS ARM64 lifecycle · seven independent processes per group', fontsize=13)
    fig.text(0.5, 0.01, 'Dots: process samples; bars: pointwise 95% bootstrap median intervals.\nNative models/counts differ; timings do not establish equivalent cross-tool work or a ranking.',
             ha='center', fontsize=9)
    fig.tight_layout(rect=(0, 0.065, 1, 0.96))
    save(fig, graphs, 'lifecycle_comparison')

    fig, axes = plt.subplots(2, 2, figsize=(11, 7.5))
    for i, (dataset, title) in enumerate(DATASETS.items()):
        for j, stage in enumerate(('first', 'warm')):
            ax = axes[i, j]
            for k, query in enumerate(QUERIES):
                for offset, kind in zip((-0.2, 0, 0.2), PARTICIPANTS):
                    point(ax, rows[dataset, query, kind]['metrics'][f'{query}_{stage}_ns'],
                          k, 1000, COLORS[kind], offset)
            ax.set_xticks(range(4), QUERIES)
            ax.set_title(f'{title} · {stage} query')
            ax.set_yscale('log')
            ax.set_ylabel('Microseconds per call (log scale)')
            ax.grid(axis='y', alpha=0.2)
    handles = [plt.Line2D([], [], color=COLORS[p], marker='o', linestyle='', label=LABELS[p]) for p in PARTICIPANTS]
    fig.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, 0.96), ncol=3)
    fig.suptitle('Isolated first queries and warm calls · one selected query per fresh process', fontsize=13)
    fig.text(0.5, 0.01, 'Warm observations are per-process medians of nine calibrated batches; first calls include invocation/timer overhead.\nScalar cached access and table materialization are different operations. Counts and all samples accompany this figure.',
             ha='center', fontsize=9)
    fig.tight_layout(rect=(0, 0.065, 1, 0.90))
    save(fig, graphs, 'first_warm_queries')

    text = ['# Native lifecycle comparison', '',
            'This cohort records 210 fresh processes on macOS ARM64: seven repeats × two datasets × five query modes × three participants. It supplements the calibrated pytest benchmark; it does not establish universal first place.', '',
            f"Harness: `{report['harness_commit']}`. PowerIO sources: stable `{report['builds']['stable']['source_commit']}` and RC `{report['builds']['rc']['source_commit']}`. PyPowSyBl: `1.16.1`.", '',
            'Matched PowerIO builds use release mode, the locked dependencies, default features plus `gridfm`, Rust 1.98.1, maturin 1.16.0 and Python 3.13.18. The shared host is an Apple M5 Pro with 18 CPU cores and 64 GiB RAM; caches were uncontrolled and no affinity was set.', '',
            report['method'], '',
            '![Lifecycle timing and memory](graphs/lifecycle_comparison.svg)', '',
            'The RC is slower on Svedala and faster on RealGrid in this experiment. The following ratios pair each RC sample with its stable sample in the same repeat block; ratios above one are slower.', '',
            '| Case | Mode | RC / stable load-to-use | Pointwise 95% interval |',
            '|---|---|---:|---:|']
    for entry in report['paired_rc_stable']:
        if entry['metric'] == 'load_to_use_ns':
            lo, hi = entry['bootstrap_paired_median_95pct']
            text.append(f"| {DATASETS[entry['dataset']]} | {entry['query_mode']} | {entry['median_ratio']:.4f} | [{lo:.4f}, {hi:.4f}] |")
    text += ['', '![First and warm query latency](graphs/first_warm_queries.svg)', '',
             'Each single-query mode measures its first call on a newly loaded model. In `all` mode, earlier queries may initialize later ones. Load-to-use sums the load and first calls, excluding measurement instrumentation between stages. Import-to-use adds import/adapter construction; it is not end-to-end process wall time.', '',
             '## Native counts and comparability', '',
             '| Case | Participant | Lines | Generators | Loads | Substations |', '|---|---|---:|---:|---:|---:|']
    for dataset in DATASETS:
        for kind in PARTICIPANTS:
            row = rows[dataset, 'all', kind]
            counts = ' | '.join('/'.join(map(str, row['counts'][q])) for q in QUERIES)
            text.append(f'| {DATASETS[dataset]} | {LABELS[kind]} | {counts} |')
    text += ['', 'PowerIO includes equivalent injections in load counts and retains source/boundary substations. PyPowSyBl converts equipment into its native network and materializes queried tables. The count mismatches require a field-level audit; equal counts alone would not prove equivalent work.', '',
             '## Limits', ''] + ['- '+item for item in report['limitations']]
    text += ['', '## Raw evidence and reproduction', '',
             '- [Comparison JSON](comparison.json) includes every mode, raw process-level samples and uncertainty.',
             '- [Raw plan](raw/plan.json), [installed packages](raw/packages.txt), and [SHA-256 manifest](manifest.json) retain inputs, compiler/build identities, wheel hashes, invocation order, environment observations and every result.',
             '- [Reproduction scripts](reproduce/) retain the original build, run and reduction commands. Their paths describe the recorded host; configure equivalent local paths and the pinned dataset checkouts when repeating.',
             '- Regenerate figures and Markdown with `python tools/generate_lifecycle_report.py results-native-lifecycle/2026-11-10-macos-arm64` using `matplotlib==3.10.8`.', '',
             f"Recorded failures: {len(report['failures'])}. No measurements were omitted based on speed. Linux, export and remaining competitors still require matched repeated measurements.", '']
    (directory/'comparison_summary.md').write_text('\n'.join(text))
    manifest = [dict(file=str(path.relative_to(directory)), bytes=path.stat().st_size,
                     sha256=hashlib.sha256(path.read_bytes()).hexdigest())
                for path in sorted(directory.rglob('*'))
                if path.is_file() and path.name != 'manifest.json']
    (directory/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(directory/'comparison_summary.md')


if __name__ == '__main__':
    main(Path(sys.argv[1]))
