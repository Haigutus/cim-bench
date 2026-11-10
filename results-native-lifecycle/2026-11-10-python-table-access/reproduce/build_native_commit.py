"""Build a frozen commit with the native lifecycle cohort's exact settings."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path('/private/tmp/cim-perf')
repo = Path('/Users/samuel/.codex/worktrees/pandapower-dcline-cost/powerio')
commit = sys.argv[1]
assert len(commit)==40 and all(c in '0123456789abcdef' for c in commit)
assert subprocess.check_output(['git','rev-parse',commit],cwd=repo,text=True).strip()==commit
source = root/('source-'+commit[:8])
archive = root/('source-'+commit[:8]+'.tar')
assert not source.exists() and not archive.exists()
with archive.open('wb') as output:
    subprocess.run(['git','archive',commit],cwd=repo,stdout=output,check=True)
source.mkdir()
subprocess.run(['tar','-xf',str(archive),'-C',str(source)],check=True)
inputs = [{'path':str(p.relative_to(source)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
          for p in sorted(source.rglob('*')) if p.is_file()]
native = root/'mac-wheels'/commit[:8]
native.mkdir()
env = dict(os.environ, CARGO_TARGET_DIR=str(root/'allocation-target'),
           PYO3_PYTHON='/private/tmp/powerio-821-py/bin/python', RUSTUP_TOOLCHAIN='1.98.1')
for key in ['CARGO_INCREMENTAL','CARGO_PROFILE_DEV_DEBUG','CARGO_PROFILE_TEST_DEBUG']:
    env.pop(key,None)
baseline = json.loads((root/'matched-20261110-da32f73e-build.json').read_text())
rustc = subprocess.check_output(['rustc','-Vv'],cwd=source,env=env,text=True)
assert rustc==baseline['native_rustc'],(rustc,baseline['native_rustc'])
subprocess.run(['/private/tmp/powerio-821-py/bin/maturin','build','--release','--locked',
                '--features','gridfm','-i',env['PYO3_PYTHON'],'-o',str(native)],
               cwd=source,env=env,check=True)
for entry in inputs:
    assert hashlib.sha256((source/entry['path']).read_bytes()).hexdigest()==entry['sha256']
wheels = list(native.glob('*.whl'))
assert len(wheels)==1
record = {'source_commit':commit,'source_tree':subprocess.check_output(['git','rev-parse',commit+'^{tree}'],cwd=repo,text=True).strip(),
          'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
          'native_rustc':rustc,'native_maturin':subprocess.check_output(['/private/tmp/powerio-821-py/bin/maturin','--version'],text=True).strip(),
          'native_build_python':subprocess.check_output([env['PYO3_PYTHON'],'--version'],text=True).strip(),
          'build_options':baseline['build_options'],
          'environment_overrides':{key:env.get(key) for key in baseline['environment_overrides']},
          'source_files':inputs,'wheels':[{'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in wheels]}
(root/('native-20261110-'+commit[:8]+'-build.json')).write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({key:val for key,val in record.items() if key!='source_files'}))
