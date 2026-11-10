"""Seven blocked, randomized, independent native processes per library/case/mode."""
import hashlib
import json
import os
from pathlib import Path
import random
import subprocess
import sys
import time

ROOT = Path('/Users/samuel/datasets/powerio-rc-2026-11-10')
BUILD = Path('/private/tmp/cim-perf')
HARNESS = BUILD / 'harness-c00f8fe'
COMMIT = 'c00f8fe24ec2c27a3be8e63d5bccca7184b5e551'
PYTHON = BUILD / 'mac-venv/bin/python'
OUTPUT = ROOT / 'native-lifecycle-c00f8fe'
VERSIONS = {'stable': 'da32f73ea3d9beb283b7d84530985e44eba90741',
            'rc': '3abeee34e3c8fc0dc913526d40da27db37041ee6'}


def main():
    assert not OUTPUT.exists(), 'Never overwrite a previous experiment'
    OUTPUT.mkdir()
    records = {kind: json.loads((BUILD / f'matched-20261110-{sha[:8]}-build.json').read_text())
               for kind, sha in VERSIONS.items()}
    for key in ('native_rustc', 'native_maturin', 'native_build_python', 'build_options', 'environment_overrides'):
        assert records['stable'][key] == records['rc'][key], key
    targets = {}
    for kind, record in records.items():
        wheel = next(item for item in record['wheels'] if 'macosx' in item['file'])
        assert hashlib.sha256(Path(wheel['file']).read_bytes()).hexdigest() == wheel['sha256']
        target = OUTPUT / ('packages-' + kind)
        subprocess.run(['uv', 'pip', 'install', '--python', str(PYTHON), '--target', str(target),
                        '--no-deps', wheel['file']], check=True)
        targets[kind] = target
    subprocess.run(['uv', 'pip', 'freeze', '--python', str(PYTHON)], stdout=(OUTPUT/'packages.txt').open('w'), check=True)
    plan = []
    rng = random.Random(20261110)
    for repeat in range(1, 8):
        groups = [(dataset, query) for dataset in ('svedala_igm_cgmes_3', 'realgrid_cgmes_2_4')
                  for query in ('all', 'lines', 'generators', 'loads', 'substations')]
        rng.shuffle(groups)
        for dataset, query in groups:
            participants = ['stable', 'rc', 'pypowsybl']
            rng.shuffle(participants)
            for kind in participants:
                plan.append({'repeat': repeat, 'dataset': dataset, 'query': query, 'kind': kind})
    (OUTPUT/'plan.json').write_text(json.dumps({'seed': 20261110, 'independent_repeats': 7,
        'harness_commit': COMMIT, 'builds': records, 'samples': plan,
        'platform': 'native macOS ARM64; shared host; no CPU affinity or file-cache flush',
        'note': 'Every failure and timeout retained. No early stopping based on performance.'}, indent=2)+'\n')
    for index, task in enumerate(plan):
        stem = f'{index:03d}-{task["kind"]}-{task["dataset"]}-{task["query"]}-r{task["repeat"]}'
        destination = OUTPUT / (stem+'.json')
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', CIM_BENCH_RUN_ID=stem,
                   CIM_BENCH_COMMIT=COMMIT, CIM_BENCH_TOOL_COMMIT=VERSIONS.get(task['kind'], ''))
        env.pop('CIM_BENCH_IMAGE_ID', None)
        env['PYTHONPATH'] = str(targets[task['kind']]) if task['kind'] in targets else ''
        tool = 'pypowsybl' if task['kind'] == 'pypowsybl' else 'powerio'
        command = [str(PYTHON), str(HARNESS/'tools/measure_lifecycle.py'), tool, task['dataset'],
                   str(destination), '--query', task['query']]
        before = time.monotonic()
        started = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        ambient = subprocess.check_output([str(PYTHON), '-c',
            'import json,os,psutil; print(json.dumps(dict(cpu_percent=psutil.cpu_percent(interval=0.2),load_average=os.getloadavg(),available_memory_bytes=psutil.virtual_memory().available)))'], text=True)
        with (OUTPUT/(stem+'.log')).open('w') as log:
            try:
                status = subprocess.run(command, env=env, cwd=HARNESS, stdout=log, stderr=subprocess.STDOUT, timeout=180).returncode
            except subprocess.TimeoutExpired:
                status = 'timeout'
        receipt = {**task, 'command': command, 'pythonpath': env['PYTHONPATH'], 'started_at': started,
                   'status': status, 'elapsed_seconds': time.monotonic()-before,
                   'ambient_before': json.loads(ambient),
                   'result_sha256': hashlib.sha256(destination.read_bytes()).hexdigest() if destination.exists() else None}
        (OUTPUT/(stem+'-invocation.json')).write_text(json.dumps(receipt,indent=2)+'\n')
        print(json.dumps({'index': index, 'total': len(plan), **task, 'status': status}), flush=True)


if __name__ == '__main__':
    main()
