"""Build an immutable source into matched native and Linux artifacts for the 2026-11-10 comparison."""
import hashlib
import json
import os
import pathlib
import subprocess
import sys

root = pathlib.Path('/private/tmp/cim-perf')
repo = pathlib.Path('/Users/samuel/eigenergy/powerio/.claude/worktrees/pr-821')
commit = sys.argv[1]
resume = '--resume' in sys.argv[2:]
assert len(commit) == 40 and all(c in '0123456789abcdef' for c in commit)
assert subprocess.check_output(['git', '-C', str(repo), 'rev-parse', commit], text=True).strip() == commit
source = root / ('source-' + commit[:8])
archive = root / ('source-' + commit[:8] + '.tar')
if resume:
    assert source.is_dir() and archive.is_file(), 'Only resume an existing immutable source'
    expected = subprocess.check_output(['git', '-C', str(repo), 'archive', commit])
    assert hashlib.sha256(expected).digest() == hashlib.sha256(archive.read_bytes()).digest()
else:
    assert not source.exists() and not archive.exists(), 'Do not overwrite prior source artifacts'
    with archive.open('wb') as output:
        subprocess.run(['git', '-C', str(repo), 'archive', commit], stdout=output, check=True)
    source.mkdir()
    subprocess.run(['tar', '-xf', str(archive), '-C', str(source)], check=True)
source_files = []
for path in sorted(source.rglob('*')):
    if path.is_file():
        content = path.read_bytes()
        source_files.append({'path': str(path.relative_to(source)), 'bytes': len(content),
                             'sha256': hashlib.sha256(content).hexdigest()})
inputs = root / ('matched-20261110-' + commit[:8] + '-source-files.json')
if resume:
    recorded_inputs = json.loads(inputs.read_text())
    assert recorded_inputs['source_commit'] == commit and recorded_inputs['files'] == source_files
else:
    inputs.write_text(json.dumps({'source_commit': commit, 'basis': 'All files in the immutable git archive, hashed before either build, including runtime sources, build metadata, tests and documentation.',
                                'files': source_files}, indent=2) + '\n')
native = root / 'mac-wheels' / commit[:8]
linux = root / 'final-wheels' / ('matched-20261110-' + commit[:8])
native.mkdir(parents=True, exist_ok=resume)
linux.mkdir(parents=True, exist_ok=resume)
env = dict(os.environ, CARGO_TARGET_DIR=str(root / 'allocation-target'),
           PYO3_PYTHON='/private/tmp/powerio-821-py/bin/python')
if not resume or not list(native.glob('*.whl')):
    subprocess.run(['/private/tmp/powerio-821-py/bin/maturin', 'build', '--release', '--locked',
                    '--features', 'gridfm', '-i', env['PYO3_PYTHON'], '-o', str(native)],
                   cwd=source, env=env, check=True)
assert len(list(native.glob('*.whl'))) == 1
builder = 'localhost/cim-bench/powerio-builder:327d81e1'
builder_id = subprocess.check_output(['podman', 'image', 'inspect', builder, '--format', '{{.Id}}'], text=True).strip()
container = 'cim-powerio-matched-20261110-' + commit[:8]
if not resume or not list(linux.glob('*.whl')):
    subprocess.run(['podman', 'run', '--network=none', '--name', container, '-v', f'{source}:/input-rc:ro',
                    '-v', f'{linux}:/out', builder, 'sh', '-c',
                    'cd /input-rc && CARGO_TARGET_DIR=/src/target PYO3_PYTHON=/tmp/build-venv/bin/python '
                    '/tmp/build-venv/bin/maturin build --release --locked --features gridfm '
                    '-i /tmp/build-venv/bin/python -o /out'], check=True)
subprocess.run([sys.executable, str(root / 'build_runtime.py'), 'matched-20261110-' + commit[:8], commit], check=True)
wheels = list(native.glob('*.whl')) + list(linux.glob('*.whl'))
assert len(wheels) == 2
record = {'source_commit': commit, 'source_tree': subprocess.check_output(
    ['git', '-C', str(repo), 'rev-parse', commit + '^{tree}'], text=True).strip(),
    'archive': str(archive), 'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
    'build_source': 'git archive of exact immutable commit; no live worktree files',
    'linux_builder_image': builder_id,
    'build_options': {'release': True, 'locked': True, 'features': ['gridfm'], 'default_features': True},
    'environment_overrides': {key: os.environ.get(key) for key in ['RUSTFLAGS', 'CARGO_ENCODED_RUSTFLAGS', 'MACOSX_DEPLOYMENT_TARGET', 'CARGO_BUILD_TARGET', 'CARGO_PROFILE_RELEASE_LTO', 'CARGO_PROFILE_RELEASE_CODEGEN_UNITS']},
    'native_rustc': subprocess.check_output(['rustc', '-Vv'], cwd=source, env=env, text=True),
    'native_maturin': subprocess.check_output(['/private/tmp/powerio-821-py/bin/maturin', '--version'], text=True).strip(),
    'native_build_python': subprocess.check_output([env['PYO3_PYTHON'], '--version'], text=True).strip(),
    'linux_rustc': subprocess.check_output(['podman', 'run', '--rm', '--network=none', builder, 'rustc', '-Vv'], text=True),
    'wheels': [{'file': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in wheels]}
for item in source_files:
    assert hashlib.sha256((source / item['path']).read_bytes()).hexdigest() == item['sha256'], item['path']
record['source_file_manifest'] = {'file': str(inputs), 'sha256': hashlib.sha256(inputs.read_bytes()).hexdigest()}
path = root / ('matched-20261110-' + commit[:8] + '-build.json')
path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record), flush=True)
