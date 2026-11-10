"""Matched release wheels; seven serial randomized blocks, every sample retained."""
import hashlib
import json
import os
from pathlib import Path
import random
import subprocess
import time

root=Path('/Users/samuel/datasets/powerio-rc-2026-11-10')
build=Path('/private/tmp/cim-perf')
python=build/'mac-venv/bin/python'
out=root/'python-table-access-148e16f4'
out.mkdir(exist_ok=False)
records={'stable':json.loads((build/'matched-20261110-da32f73e-build.json').read_text()),
         'candidate':json.loads((build/'native-20261110-148e16f4-build.json').read_text())}
for key in ['native_rustc','native_maturin','native_build_python','build_options','environment_overrides']:
    assert records['stable'][key]==records['candidate'][key],key
targets={}
for kind,record in records.items():
    wheel=next(x for x in record['wheels'] if 'macosx' in x['file'])
    assert hashlib.sha256(Path(wheel['file']).read_bytes()).hexdigest()==wheel['sha256']
    targets[kind]=out/('packages-'+kind)
    subprocess.run(['uv','pip','install','--python',str(python),'--target',str(targets[kind]),'--no-deps',wheel['file']],check=True)
plan=[]
rng=random.Random(202611103)
for repeat in range(1,8):
    block=[{'case':case,'table':table,'kind':kind,'repeat':repeat}
           for case in ['case14.m','case2869pegase.m','t_case9_dcline.m']
           for table in ['hvdc','storage','static_var_compensators','transformers_3w','areas']
           for kind in ['stable','candidate']]
    rng.shuffle(block);plan.extend(block)
probe=root/'scripts/measure_table_access.py'
(out/'plan.json').write_text(json.dumps({'seed':202611103,'repeats':7,'samples':plan,'builds':records,
    'probe_sha256':hashlib.sha256(probe.read_bytes()).hexdigest(),'warm_batches':9,
    'warm_target_ms':20,'scope':'Python balanced table getters only; not a parser ranking. No CPU affinity or cache control.'},indent=2)+'\n')
for index,task in enumerate(plan):
    stem=f'{index:03d}-{task["kind"]}-{task["case"]}-{task["table"]}-r{task["repeat"]}'
    result=out/(stem+'.json')
    case=build/'source-da32f73e/tests/data'/task['case']
    command=[str(python),str(probe),str(case),task['table'],str(result)]
    env=dict(os.environ,PYTHONPATH=str(targets[task['kind']]),PYTHONDONTWRITEBYTECODE='1')
    start=time.monotonic()
    with (out/(stem+'.log')).open('w') as log:
        try:
            status=subprocess.run(command,cwd='/private/tmp',env=env,stdout=log,stderr=subprocess.STDOUT,timeout=60).returncode
        except subprocess.TimeoutExpired:
            status='timeout'
    receipt={**task,'command':command,'status':status,'seconds':time.monotonic()-start,
             'result_sha256':hashlib.sha256(result.read_bytes()).hexdigest() if result.exists() else None}
    (out/(stem+'-invocation.json')).write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'index':index,'total':len(plan),**task,'status':status}),flush=True)
