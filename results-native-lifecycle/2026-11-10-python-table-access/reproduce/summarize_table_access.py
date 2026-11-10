"""Reduce seven independent processes per group and verify identical tables."""
import hashlib
import json
from pathlib import Path
import random
import statistics

root=Path('/Users/samuel/datasets/powerio-rc-2026-11-10')
raw=root/'python-table-access-148e16f4'
plan=json.loads((raw/'plan.json').read_text())
groups={}
failures=[]
manifest=[]
for p in sorted(raw.glob('*-invocation.json')):
    inv=json.loads(p.read_text())
    if inv['status']!=0:
        failures.append(inv);continue
    result=p.with_name(p.name.replace('-invocation.json','.json'))
    assert hashlib.sha256(result.read_bytes()).hexdigest()==inv['result_sha256']
    d=json.loads(result.read_text())
    groups.setdefault((inv['case'],inv['table'],inv['kind']),[]).append((inv['repeat'],d))
    manifest.append({'file':result.name,'sha256':inv['result_sha256']})
assert len(list(raw.glob('*-invocation.json')))==len(plan['samples'])==210

def interval(samples):
    rng=random.Random(202611104)
    b=sorted(statistics.median(rng.choices(samples,k=len(samples)))for _ in range(10000))
    return [b[249],b[9749]]

rows=[]
for case,table in sorted({(c,t)for c,t,_ in groups}):
    stable=sorted(groups[case,table,'stable']);candidate=sorted(groups[case,table,'candidate'])
    assert len(stable)==len(candidate)==7
    fingerprints={d['table_sha256']for _,d in stable+candidate}
    assert len(fingerprints)==1,(case,table,fingerprints)
    assert len({d['case_sha256']for _,d in stable+candidate})==1
    metrics={}
    for metric in ['load_ns','first_ns','warm_ns','load_to_use_ns']:
        a=[d[metric]for _,d in stable];b=[d[metric]for _,d in candidate]
        ratios=[y/x for x,y in zip(a,b)]
        metrics[metric]={'stable':{'samples':a,'median':statistics.median(a),'median_95pct':interval(a)},
                         'candidate':{'samples':b,'median':statistics.median(b),'median_95pct':interval(b)},
                         'paired_candidate_over_stable':{'samples':ratios,'median':statistics.median(ratios),'median_95pct':interval(ratios)}}
    memory={kind:{stage:{key:[d[stage][key]for _,d in samples] for key in ['rss_bytes','peak_rss_bytes']}
                  for stage in ['before','after_load','after_first','after_warm']}
            for kind,samples in [('stable',stable),('candidate',candidate)]}
    rows.append({'case':case,'table':table,'table_rows':stable[0][1]['table_rows'],
                 'table_sha256':next(iter(fingerprints)),'metrics':metrics,'memory':memory})
report={'source_commits':{k:v['source_commit']for k,v in plan['builds'].items()},'raw_manifest':manifest,
        'failures':failures,'n_processes':210,'rows':rows,
        'method':'Seven randomized blocks, one fresh process per version/case/table in each block; nine warm batches reduce to one median per process; 10,000 bootstrap resamples; paired candidate/stable ratios within blocks.',
        'limitations':['Pointwise descriptive intervals, not simultaneous confidence over all groups.',
                       'Three balanced MATPOWER fixtures and five selected getters on native macOS ARM64 only; no parser or competitor ranking.',
                       'Empty table getters are included and identified, alongside one nonempty HVDC table.',
                       'Load includes parse and typed-handle construction; import is recorded separately; phase instrumentation and process startup excluded.',
                       'RSS includes interpreter and imports, is allocator-dependent, and is not allocation volume; no CPU affinity or cache flush.']}
(root/'python-table-access-summary.json').write_text(json.dumps(report,indent=2)+'\n')
for row in rows:
    m=row['metrics']['first_ns'];w=row['metrics']['warm_ns']
    print(row['case'],row['table'],'rows',row['table_rows'],'first us',m['stable']['median']/1e3,'->',m['candidate']['median']/1e3,'warm us',w['stable']['median']/1e3,'->',w['candidate']['median']/1e3)
print('Failures:',len(failures))
