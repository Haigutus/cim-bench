"""Predeclared paired native/Linux lifecycle experiment, serial fresh processes."""
from datetime import datetime, timezone
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
OUT = ROOT / 'namespace-2d570215-lifecycle'
HARNESS = BUILD / 'harness-ea54449'
HARNESS_COMMIT = 'ea5444916ef4d038ebf514b4617ec078f83914da'
PYTHON = BUILD / 'mac-venv/bin/python'
DATA = Path('/Users/samuel/research/cim-bench/data')
COMMITS = {'baseline': '4dcd881266b943f4405351e9e4f2aef30039a8b1',
           'candidate': '2d570215aea1b0dc7d0257e0b0909753869253fb'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert not OUT.exists(), 'Never overwrite a previous experiment'
    gates = json.loads((ROOT / 'namespace-2d570215-gates.json').read_text())
    assert len(gates) == 4 and all(x['returncode'] == 0 for x in gates)
    fidelity = json.loads((ROOT / 'namespace-2d570215-fidelity.json').read_text())
    assert fidelity['status'] == 'equal'
    sys.path.insert(0, str(HARNESS / 'parsers'))
    from datasets import DATASETS
    for dataset in DATASETS.values():
        for role, path in dataset.items():
            if not role.startswith('_'):
                assert Path(path).is_file(), path
    builds = {
        'baseline': json.loads((BUILD / 'matched-20261110-4dcd8812-verified-build.json').read_text()),
        'candidate': json.loads((BUILD / 'matched-20261110-2d570215-build.json').read_text()),
    }
    keys = ('build_options', 'environment_overrides', 'native_rustc', 'native_maturin',
            'native_build_python', 'linux_rustc', 'linux_builder_image')
    for key in keys:
        assert builds['baseline'][key] == builds['candidate'][key], key
    runtimes = {k: json.loads((BUILD / f'matched-20261110-{c[:8]}-runtime.json').read_text())
                for k, c in COMMITS.items()}
    OUT.mkdir()
    targets = {}
    for kind, record in builds.items():
        assert record['source_commit'] == COMMITS[kind]
        for wheel in record['wheels']:
            assert sha(Path(wheel['file'])) == wheel['sha256']
        wheel = next(w for w in record['wheels'] if 'macosx' in w['file'])
        target = OUT / ('packages-' + kind)
        subprocess.run(['uv', 'pip', 'install', '--python', str(PYTHON), '--target',
                        str(target), '--no-deps', wheel['file']], check=True)
        targets[kind] = target
        image = runtimes[kind]['image_id']
        assert subprocess.check_output(['podman', 'image', 'inspect', image, '--format',
                                        '{{.Id}}'], text=True).strip() == image
    host = json.loads(subprocess.check_output(['podman', 'info', '--format', '{{json .Host}}'], text=True))
    (OUT / 'vm-resources.json').write_text(json.dumps({k: host[k] for k in
        ('arch', 'cpus', 'memTotal', 'kernel', 'os', 'distribution')}, indent=2) + '\n')
    with (OUT / 'native-packages.txt').open('w') as output:
        subprocess.run(['uv', 'pip', 'freeze', '--python', str(PYTHON)], stdout=output, check=True)
    plan = []
    for platform, seed in [('native', 202611103), ('linux', 202611104)]:
        rng = random.Random(seed)
        for repeat in range(1, 8):
            groups = [(case, query) for case in ('svedala_igm_cgmes_3', 'realgrid_cgmes_2_4')
                      for query in ('all', 'lines', 'generators', 'loads', 'substations')]
            rng.shuffle(groups)
            for case, query in groups:
                kinds = list(COMMITS)
                rng.shuffle(kinds)
                plan.extend(dict(platform=platform, repeat=repeat, dataset=case,
                                 query=query, kind=kind) for kind in kinds)
    (OUT / 'plan.json').write_text(json.dumps({
        'seeds': {'native': 202611103, 'linux': 202611104}, 'independent_repeats': 7,
        'builds': builds, 'runtimes': runtimes, 'samples': plan,
        'harness_commit': HARNESS_COMMIT, 'timeout_seconds': 180,
        'scope': 'Same PowerIO API and operations, before/after namespace cache; no competitor ranking.',
        'platform': 'Native macOS ARM64 and Linux ARM64 VM, measured as separate groups, serially.',
        'caches': 'No CPU affinity or file-cache flush; fresh processes, warm host file caches.',
        'ambient_limitations': 'Shared desktop host; Codex/browser/window-manager activity persists. No owned builds or oracles run concurrently. Per-sample ambient CPU/load/memory are recorded; no samples are discarded for load.',
        'stopping': 'Run every declared sample, preserve errors/timeouts and unfavorable results.',
    }, indent=2) + '\n')
    ambient_command = [str(PYTHON), '-c', 'import json,os,psutil;print(json.dumps(dict(cpu_percent=psutil.cpu_percent(interval=.2),load_average=os.getloadavg(),available_memory_bytes=psutil.virtual_memory().available)))']
    for index, task in enumerate(plan):
        folder = OUT / task['platform']
        folder.mkdir(exist_ok=True)
        stem = f'{index:03d}-{task["kind"]}-{task["dataset"]}-{task["query"]}-r{task["repeat"]}'
        destination = folder / (stem + '.json')
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', CIM_BENCH_RUN_ID=stem,
                   CIM_BENCH_COMMIT=HARNESS_COMMIT, CIM_BENCH_TOOL_COMMIT=COMMITS[task['kind']])
        image = runtimes[task['kind']]['image_id']
        name = 'pio-namespace-' + str(index)
        if task['platform'] == 'native':
            env.pop('CIM_BENCH_IMAGE_ID', None)
            env['PYTHONPATH'] = str(targets[task['kind']])
            command = [str(PYTHON), str(HARNESS / 'tools/measure_lifecycle.py'), 'powerio',
                       task['dataset'], str(destination), '--query', task['query']]
        else:
            command = ['podman', 'run', '--rm', '--network=none', '--name', name,
                '-v', f'{HARNESS}:/harness:ro', '-v', f'{DATA}:/harness/data:ro', '-v', f'{folder}:/output',
                '-w', '/harness', '-e', 'PYTHONDONTWRITEBYTECODE=1',
                '-e', f'CIM_BENCH_RUN_ID={stem}', '-e', f'CIM_BENCH_COMMIT={HARNESS_COMMIT}',
                '-e', f'CIM_BENCH_TOOL_COMMIT={COMMITS[task["kind"]]}', '-e', f'CIM_BENCH_IMAGE_ID={image}',
                image, 'python', '/harness/tools/measure_lifecycle.py', 'powerio', task['dataset'],
                f'/output/{stem}.json', '--query', task['query']]
        ambient = json.loads(subprocess.check_output(ambient_command, text=True))
        record = dict(task, command=command, source_commit=COMMITS[task['kind']],
                      started_at=datetime.now(timezone.utc).isoformat(), ambient_before=ambient)
        start = time.monotonic()
        with (folder / (stem + '.log')).open('w') as output:
            process = subprocess.Popen(command, env=env, cwd=HARNESS, stdout=output, stderr=subprocess.STDOUT)
            try:
                status = process.wait(timeout=180)
            except subprocess.TimeoutExpired:
                status = 'timeout'
                if task['platform'] == 'linux':
                    subprocess.run(['podman', 'stop', '-t', '3', name], capture_output=True)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
        record.update(status=status, elapsed_seconds=time.monotonic() - start,
                      result_sha256=sha(destination) if destination.exists() else None)
        (folder / (stem + '-invocation.json')).write_text(json.dumps(record, indent=2) + '\n')
        print(json.dumps(dict(index=index, total=len(plan), **task, status=status)), flush=True)


if __name__ == '__main__':
    main()
