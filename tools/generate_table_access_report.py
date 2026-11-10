"""Render the narrow Python table-access experiment, including empty tables."""
import hashlib
import json
from pathlib import Path
import statistics
import sys

from generate_lifecycle_report import plt, point, save


def main(directory):
    report=json.loads((directory/'comparison.json').read_text())
    for entry in report['raw_manifest']:
        assert hashlib.sha256((directory/'raw'/entry['file']).read_bytes()).hexdigest()==entry['sha256']
    cases=['case14.m','case2869pegase.m','t_case9_dcline.m']
    tables=['hvdc','storage','static_var_compensators','transformers_3w','areas']
    labels=['HVDC','Storage','SVC','3-winding','Areas']
    rows={(r['case'],r['table']):r for r in report['rows']}
    graphs=directory/'graphs';graphs.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'svg.hashsalt':'powerio-table-access-v1'})
    fig,axes=plt.subplots(3,2,figsize=(12,10))
    for i,case in enumerate(cases):
        for j,metric in enumerate(['first_ns','warm_ns']):
            ax=axes[i,j]
            for k,table in enumerate(tables):
                for kind,offset,color in [('stable',-.12,'#677993'),('candidate',.12,'#147D70')]:
                    m=rows[case,table]['metrics'][metric][kind]
                    point(ax,{**m,'bootstrap_median_95pct':m['median_95pct']},k,1000,color,offset)
            ax.set_title(case+' · '+('first call' if j==0 else 'warm calls'))
            ax.set_xticks(range(5),labels)
            ax.set_yscale('log');ax.set_ylabel('Microseconds / call (log scale)');ax.grid(axis='y',alpha=.2)
    fig.suptitle('Python table getters · matched release builds · seven independent processes',fontsize=13)
    fig.legend(handles=[plt.Line2D([],[],color=c,marker='o',linestyle='',label=l) for c,l in [('#677993','Baseline da32f73e'),('#147D70','Candidate 148e16f4')]],loc='upper center',bbox_to_anchor=(.5,.965),ncol=2)
    fig.text(.5,.01,'14 of 15 table/case groups are empty; the dcline fixture has four HVDC rows.\nPoints: independent processes. Intervals: pointwise 95% bootstrap medians. No parser or competitor ranking.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.06,1,.92));save(fig,graphs,'table_access')
    svg=graphs/'table_access.svg';svg.write_text('\n'.join(x.rstrip()for x in svg.read_text().splitlines())+'\n')
    lines=['# Python table-access experiment','',
        'This is a narrow accessor experiment: 14 of the 15 table/case groups return empty tables, and one returns four HVDC rows. It tests removal of unrelated whole-network serialization. It does not benchmark distribution table performance or establish a parser/competitor ranking. All 210 planned fresh-process invocations succeeded; every group returned byte-equivalent canonical JSON across both versions.', '',
        f"PowerIO commits: baseline `{report['source_commits']['stable']}`, candidate `{report['source_commits']['candidate']}`. Both release wheels use Rust 1.98.1, maturin 1.16.0, locked dependencies, default features plus `gridfm`, and native macOS ARM64 with Python 3.13.18. Build records and full source-file hashes are in `raw/plan.json`.", '',
        report['method'],'','![First and warm calls](graphs/table_access.svg)','',
        '| Case | Table (rows) | First call, µs: baseline → candidate | Warm, µs: baseline → candidate | Load-to-use candidate / baseline [95% interval] | Peak RSS MiB: baseline → candidate |',
        '|---|---|---:|---:|---:|---:|']
    for r in report['rows']:
        first=r['metrics']['first_ns'];warm=r['metrics']['warm_ns'];ratio=r['metrics']['load_to_use_ns']['paired_candidate_over_stable']
        lo,hi=ratio['median_95pct'];peak=[statistics.median(r['memory'][k]['after_warm']['peak_rss_bytes'])/2**20 for k in ['stable','candidate']]
        lines.append(f"| {r['case']} | {r['table']} ({r['table_rows']}) | {first['stable']['median']/1000:.3f} → {first['candidate']['median']/1000:.3f} | {warm['stable']['median']/1000:.3f} → {warm['candidate']['median']/1000:.3f} | {ratio['median']:.4f} [{lo:.4f}, {hi:.4f}] | {peak[0]:.2f} → {peak[1]:.2f} |")
    lines += ['', 'All observed groups reduce first-call and warm-call time. The very large empty-table gains should not be extrapolated to large populated tables: output still requires copying every requested row. Load, import, first-call, warm batches and four RSS phases remain separate in the raw results; model parse time was not changed by this patch.', '', '## Limits', '']
    lines += ['- '+x for x in report['limitations']]
    lines += ['', '## Reproduction and provenance', '',
        '- [Raw comparison](comparison.json) contains every reduced sample, paired ratio, field fingerprint and memory phase.',
        '- [Plan](raw/plan.json) pins wheel/source identities, compiler/options, probe hash, seed and all 210 invocations. `raw/` retains the original receipts and losslessly compressed logs; package binaries are referenced by wheel SHA rather than vendored.',
        '- [Manifest](manifest.json) hashes all packaged files. `reproduce/` contains the runner, probe, reducer and native build script; configure paths and obtain the exact fixture/source commits before repeating.',
        '- Regenerate this report with `python tools/generate_table_access_report.py results-native-lifecycle/2026-11-10-python-table-access` and matplotlib 3.10.8.', '']
    (directory/'comparison_summary.md').write_text('\n'.join(lines))
    manifest=[{'file':str(p.relative_to(directory)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(directory.rglob('*')) if p.is_file()and p.name!='manifest.json']
    (directory/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(directory/'comparison_summary.md')


if __name__=='__main__':
    main(Path(sys.argv[1]))
