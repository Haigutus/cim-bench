"""Reduce every predeclared sample; uncertainty uses independent process pairs."""
import hashlib
import json
from pathlib import Path
import random
import statistics

ROOT = Path('/Users/samuel/datasets/powerio-rc-2026-11-10')
RAW = ROOT / 'namespace-2d570215-lifecycle'


def interval(values):
    rng = random.Random(202611105)
    samples = sorted(statistics.median(rng.choices(values, k=len(values))) for _ in range(10000))
    return [samples[249], samples[9749]]


def summarize(values):
    return dict(n=len(values), samples=values, median=statistics.median(values),
                minimum=min(values), maximum=max(values), bootstrap_median_95pct=interval(values))


def metrics(result):
    values = {key: result[key] for key in
              ('import_and_adapter_ns', 'load_ns', 'load_to_use_ns', 'import_to_use_ns')}
    for stage in ('before_load', 'after_load', 'after_warm'):
        for kind in ('rss_bytes', 'peak_rss_bytes'):
            values[f'{stage}_{kind}'] = result[f'memory_{stage}'][kind]
    for query, record in result['queries'].items():
        values[f'{query}_first_ns'] = record['first_ns']
        warm = record['warm']
        values[f'{query}_warm_ns'] = statistics.median(warm['batch_elapsed_ns']) / warm['iterations_per_batch']
    return values


def main():
    plan = json.loads((RAW / 'plan.json').read_text())
    receipts = sorted(RAW.glob('*/*-invocation.json'))
    assert len(receipts) == len(plan['samples']) == 280, 'Do not summarize a partial experiment'
    grouped, failures, observed, inputs, manifest = {}, [], [], {}, []
    for path in receipts:
        inv = json.loads(path.read_text())
        observed.append({key: inv[key] for key in ('platform', 'repeat', 'dataset', 'query', 'kind')})
        result_path = path.with_name(path.name.replace('-invocation.json', '.json'))
        manifest.append(dict(file=str(path.relative_to(RAW)), sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        if inv['status'] != 0:
            failures.append(dict(file=str(path.relative_to(RAW)), invocation=inv))
            continue
        raw = result_path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == inv['result_sha256']
        result = json.loads(raw)
        assert result['status'] == 'success'
        assert result['declared_build']['CIM_BENCH_TOOL_COMMIT'] == inv['source_commit']
        assert result['declared_build']['CIM_BENCH_COMMIT'] == plan['harness_commit']
        fingerprint = [{k: x[k] for k in ('role', 'name', 'bytes', 'sha256')} for x in result['inputs']]
        if inv['dataset'] in inputs:
            assert inputs[inv['dataset']] == fingerprint
        else:
            inputs[inv['dataset']] = fingerprint
        manifest.append(dict(file=str(result_path.relative_to(RAW)), sha256=inv['result_sha256']))
        grouped.setdefault((inv['platform'], inv['dataset'], inv['query'], inv['kind']), []).append((inv['repeat'], result, inv))
    normalize = lambda items: sorted(json.dumps(x, sort_keys=True) for x in items)
    assert normalize(observed) == normalize(plan['samples'])
    rows, comparisons = [], []
    for key, samples in sorted(grouped.items()):
        samples.sort()
        assert [repeat for repeat, _, _ in samples] == list(range(1, 8))
        counts = [{q: d['count'] for q, d in result['queries'].items()} for _, result, _ in samples]
        assert all(c == counts[0] for c in counts)
        values = [metrics(d) for _, d, _ in samples]
        rows.append(dict(platform=key[0], dataset=key[1], query=key[2], participant=key[3], counts=counts[0],
                         metrics={name: summarize([x[name] for x in values]) for name in values[0]},
                         ambient_cpu_percent=[inv['ambient_before']['cpu_percent'] for _, _, inv in samples]))
    for platform, dataset, query in sorted({k[:3] for k in grouped}):
        baseline = sorted(grouped[(platform, dataset, query, 'baseline')])
        candidate = sorted(grouped[(platform, dataset, query, 'candidate')])
        for b, c in zip(baseline, candidate):
            assert b[0] == c[0]
            assert {k: x['count'] for k, x in b[1]['queries'].items()} == {k: x['count'] for k, x in c[1]['queries'].items()}
        ratios = {}
        for name in metrics(baseline[0][1]):
            values = [metrics(c[1])[name] / metrics(b[1])[name] for b, c in zip(baseline, candidate)]
            ratios[name] = summarize(values)
        comparisons.append(dict(platform=platform, dataset=dataset, query=query, candidate_over_baseline=ratios))
    report = dict(schema='powerio-cgmes-namespace-lifecycle', schema_version=1, plan='plan.json',
                  builds=plan['builds'], harness_commit=plan['harness_commit'], inputs=inputs,
                  raw_manifest=manifest, failures=failures, rows=rows, paired=comparisons,
                  method='Seven independently launched process pairs per platform/case/query, blocked randomized order; per-process warm batch medians. 10,000 percentile bootstrap resamples of independent pairs; same fixed resampling seed for reproducibility.',
                  limitations=[
                      'Pointwise descriptive bootstrap intervals with only seven independent pairs; no familywise or selection correction.',
                      'Two CGMES cases and count queries only. No export timing, other formats, or competitor ranking.',
                      'Shared desktop activity and warm uncontrolled filesystem caches; no CPU affinity. Native and VM results are separate groups.',
                      'RSS includes interpreter/imports and excludes children. It does not measure allocation volume or transient object lifetimes.',
                      'All query mode measures the ordered sequence; single-query groups isolate the first use of that query.',
                      'Equal counts are supplemented by complete before/after IR/replay/fresh-output/diagnostic comparison; that comparison is not an independent format oracle.',
                      'Commit 2d570215 is a candidate branch; future RC integration needs final-commit qualification.'
                  ], universal_performance_criterion_satisfied=False)
    (ROOT / 'namespace-2d570215-summary.json').write_text(json.dumps(report, indent=2) + '\n')
    for row in comparisons:
        if row['query'] == 'all':
            ratio = row['candidate_over_baseline']['load_to_use_ns']
            print(row['platform'], row['dataset'], ratio['median'], ratio['bootstrap_median_95pct'])
    print('successful samples', len(receipts) - len(failures), 'failures', len(failures))


if __name__ == '__main__':
    main()
