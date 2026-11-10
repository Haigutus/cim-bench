"""Serial randomized Linux ARM64 native-model lifecycle cohort; retain all attempts."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import random
import subprocess
import time

ROOT = Path('/Users/samuel/datasets/powerio-rc-2026-11-10')
OUT = ROOT/'linux-native-lifecycle-ea54449'
HARNESS = Path('/private/tmp/cim-perf/harness-ea54449')
DATA = Path('/Users/samuel/research/cim-bench/data')
COMMIT = 'ea5444916ef4d038ebf514b4617ec078f83914da'
PARTICIPANTS = {
    'stable': ('powerio','34a0348d86919fbc054d04b2019be41a35f6d11aface0800f9d3660ef5a73725','da32f73ea3d9beb283b7d84530985e44eba90741'),
    'rc': ('powerio','9e3edaff79d8159d6fc0e25d18fb29b76b8eee8733586c931654001af7377926','3abeee34e3c8fc0dc913526d40da27db37041ee6'),
    'cimoxide': ('cimoxide','79fd136ba50dce59250c23412a3a79aed95dc4c55fbff42b273eca06a15d1124',''),
    'veragrid': ('veragrid','96a89fe5f7d31243b98d5b724dd5e88f71a91adb57b478765c3711c7520ec600',''),
    'libcimpp': ('libcimpp','cb880fd874d5e371807176f2b52578c0453fc6f9f7e23c387014ac9bca0f63ab',''),
}


def main():
    assert not OUT.exists(), 'Never overwrite a prior experiment'
    OUT.mkdir()
    packages = 'import importlib.metadata as m,json,platform,sys; print(json.dumps(dict(python=sys.version,platform=platform.platform(),packages=sorted((d.metadata["Name"],d.version) for d in m.distributions()))))'
    for kind, (_, image, _) in PARTICIPANTS.items():
        observed = subprocess.check_output(['podman','image','inspect',image,'--format','{{.Id}}'],text=True).strip()
        assert observed == image
        record = subprocess.check_output(['podman','run','--rm','--network=none',image,'python','-c',packages],text=True)
        (OUT/(kind+'-packages.json')).write_text(record)
    host = json.loads(subprocess.check_output(['podman','info','--format','{{json .Host}}'],text=True))
    (OUT/'vm-resources.json').write_text(json.dumps({k:host[k] for k in
        ('arch','cpus','memTotal','kernel','os','distribution')},indent=2)+'\n')
    rng = random.Random(202611101)
    plan = []
    for repeat in range(1,8):
        groups = [(case,query) for case in ('svedala_igm_cgmes_3','realgrid_cgmes_2_4')
                  for query in ('all','lines','generators','loads','substations')]
        rng.shuffle(groups)
        for case, query in groups:
            kinds = list(PARTICIPANTS)
            # The pinned libcimpp image is compiled for CIM16/CGMES2.4.15.
            # Svedala's CGMES3 European extensions are an inventoried unsupported build.
            if case=='svedala_igm_cgmes_3': kinds.remove('libcimpp')
            rng.shuffle(kinds)
            plan.extend(dict(repeat=repeat,dataset=case,query=query,kind=k) for k in kinds)
    (OUT/'plan.json').write_text(json.dumps(dict(seed=202611101,harness_commit=COMMIT,participants=PARTICIPANTS,
        samples=plan,independent_repeats=7,timeout_seconds=180,
        platform='Linux ARM64 Podman VM on the same macOS host; serial containers; no affinity or cache flush',
        exclusions={'libcimpp/svedala':'Pinned image implements CGMES2.4.15 only; CGMES3 build rejection retained in prior inventory',
                    'pypowsybl':'No Linux ARM64 wheel in the pinned tool build; macOS cohort is separate'},
        scope='Native-model library cohort; all RDF/triplestore and CLI groups remain separately inventoried and unmeasured here'),indent=2)+'\n')
    for i, task in enumerate(plan):
        tool,image,source = PARTICIPANTS[task['kind']]
        stem = f'{i:03d}-{task["kind"]}-{task["dataset"]}-{task["query"]}-r{task["repeat"]}'
        name = 'pio-lifecycle-'+str(i)
        command = ['podman','run','--rm','--network=none','--name',name,
            '-v',f'{HARNESS}:/harness:ro','-v',f'{DATA}:/harness/data:ro','-v',f'{OUT}:/output',
            '-w','/harness','-e','PYTHONDONTWRITEBYTECODE=1',
            '-e',f'CIM_BENCH_RUN_ID={stem}','-e',f'CIM_BENCH_COMMIT={COMMIT}',
            '-e',f'CIM_BENCH_IMAGE_ID={image}','-e',f'CIM_BENCH_TOOL_COMMIT={source}',
            image,'python','/harness/tools/measure_lifecycle.py',tool,task['dataset'],f'/output/{stem}.json','--query',task['query']]
        ambient = json.loads(subprocess.check_output(['/private/tmp/cim-perf/mac-venv/bin/python','-c',
            'import json,os,psutil;print(json.dumps(dict(cpu_percent=psutil.cpu_percent(interval=.2),load_average=os.getloadavg(),available_memory_bytes=psutil.virtual_memory().available)))'],text=True))
        record=dict(**task,command=command,image=image,source_commit=source,started_at=datetime.now(timezone.utc).isoformat(),ambient_before=ambient)
        start=time.monotonic()
        with (OUT/(stem+'.log')).open('w') as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT)
            try: status=process.wait(timeout=180)
            except subprocess.TimeoutExpired:
                status='timeout'
                subprocess.run(['podman','stop','-t','3',name],capture_output=True)
                try: process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill();process.wait()
        result=OUT/(stem+'.json')
        record.update(status=status,elapsed_seconds=time.monotonic()-start,
                      result_sha256=hashlib.sha256(result.read_bytes()).hexdigest() if result.exists() else None)
        (OUT/(stem+'-invocation.json')).write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(dict(index=i,total=len(plan),**task,status=status)),flush=True)


if __name__=='__main__': main()
