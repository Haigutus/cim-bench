"""Summarize independent process samples, retaining every declared participant."""
import hashlib
import json
import math
from pathlib import Path
import random
import statistics

ROOT = Path('/Users/samuel/datasets/powerio-rc-2026-11-10')
RAW = ROOT/'linux-native-lifecycle-ea54449'


def interval(samples, seed=627):
    rng = random.Random(seed)
    bootstrap = sorted(statistics.median(rng.choices(samples, k=len(samples))) for _ in range(10000))
    return [bootstrap[249], bootstrap[9749]]


def summary(samples):
    return {'n_processes': len(samples), 'samples': samples,
            'median': statistics.median(samples), 'min': min(samples), 'max': max(samples),
            'bootstrap_median_95pct': interval(samples)}


def main():
    plan = json.loads((RAW/'plan.json').read_text())
    receipts = sorted(RAW.glob('*-invocation.json'))
    assert len(receipts) == len(plan['samples']), 'Do not summarize a partial experiment'
    groups = {}
    failures = []
    manifests = []
    for p in receipts:
        inv = json.loads(p.read_text())
        result_path = p.with_name(p.name.replace('-invocation.json','.json'))
        manifests.append({'file': p.name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
        if inv['status'] != 0:
            failures.append({'file': p.name, 'invocation': inv})
            continue
        d = json.loads(result_path.read_text())
        assert d['status'] == 'success'
        assert hashlib.sha256(result_path.read_bytes()).hexdigest() == inv['result_sha256']
        manifests.append({'file': result_path.name, 'sha256': inv['result_sha256']})
        groups.setdefault((inv['dataset'],inv['query'],inv['kind']),[]).append((inv['repeat'],d,inv))
    rows = []
    for (dataset, query, kind), samples in sorted(groups.items()):
        samples.sort()
        assert len(samples) == 7
        metrics = {key: summary([d[key] for _,d,_ in samples]) for key in
                   ('import_and_adapter_ns','load_ns','load_to_use_ns','import_to_use_ns')}
        metrics['peak_rss_bytes_after_warm'] = summary([d['memory_after_warm']['peak_rss_bytes'] for _,d,_ in samples])
        metrics['held_rss_bytes_after_load'] = summary([d['memory_after_load']['rss_bytes'] for _,d,_ in samples])
        for name in samples[0][1]['queries']:
            metrics[name+'_first_ns'] = summary([d['queries'][name]['first_ns'] for _,d,_ in samples])
            metrics[name+'_warm_ns'] = summary([statistics.median(d['queries'][name]['warm']['batch_elapsed_ns']) /
                                               d['queries'][name]['warm']['iterations_per_batch'] for _,d,_ in samples])
        rows.append({'dataset':dataset,'query_mode':query,'participant':kind,'metrics':metrics,
                     'counts':{name:sorted(set(d['queries'][name]['count'] for _,d,_ in samples))
                               for name in samples[0][1]['queries']},
                     'ambient_cpu_percent':[inv['ambient_before']['cpu_percent'] for _,_,inv in samples]})
    paired = []
    for dataset, query in sorted({(d,q) for d,q,_ in groups}):
        rc = sorted(groups[(dataset,query,'rc')]); stable = sorted(groups[(dataset,query,'stable')])
        for metric in ('load_ns','load_to_use_ns'):
            ratios=[r[1][metric]/s[1][metric] for r,s in zip(rc,stable)]
            paired.append({'dataset':dataset,'query_mode':query,'metric':metric,
                           'rc_over_stable_ratios':ratios,'median_ratio':statistics.median(ratios),
                           'bootstrap_paired_median_95pct':interval(ratios)})
    report = {'schema':'powerio-native-lifecycle-comparison','schema_version':1,
              'builds':{kind: {'tool': value[0], 'image_id': value[1], 'source_commit': value[2]} for kind,value in plan['participants'].items()},
              'platform_label':'Linux ARM64 Podman VM', 'participants': ['stable','rc','cimoxide','veragrid','libcimpp'],'harness_commit':plan['harness_commit'],
              'raw_directory':str(RAW),'raw_manifest':manifests,'failures':failures,
              'method':'Seven independently launched processes per participant/case/query mode; blocked randomized order with fixed seed202611101. Warm medians are reduced per process before uncertainty estimation.10,000 percentile bootstrap resamples across processes; paired ratios use the repeat block.',
              'limitations':['Small n; pointwise bootstrap intervals are descriptive and do not control familywise error across all groups.',
                'Shared Linux ARM64 VM on macOS;8vCPUs and16GiB memory; no CPU affinity, uncontrolled filesystem caches. Import excluded from load; reported separately.',
                'Native models and count semantics differ across participants; no cross-tool win is inferred without semantic equivalence.',
                'This covers a Linux ARM64 native-model library cohort, not fresh export, RDF/triplestore/CLI families or all registered competitors. libcimpp CGMES3 is unsupported by the pinned image; PyPowSyBl has no pinned Linux ARM64 wheel.',
                'Candidate3abeee34 was superseded by4dcd8812 while measuring; these historical measurements cannot qualify the final RC head.',
                'Process RSS includes interpreter/imports and excludes children; it is not model allocation volume.'],
              'universal_performance_criterion_satisfied':False,'rows':rows,'paired_rc_stable':paired}
    (ROOT/'linux-native-lifecycle-summary.json').write_text(json.dumps(report,indent=2)+'\n')
    for row in rows:
        if row['query_mode']=='all':
            print(row['dataset'],row['participant'],
                  'load-to-use ms',round(row['metrics']['load_to_use_ns']['median']/1e6,3),
                  'peak MiB',round(row['metrics']['peak_rss_bytes_after_warm']['median']/2**20,2),
                  'counts',row['counts'])
    print('Failures:', len(failures))


if __name__=='__main__':
    main()
