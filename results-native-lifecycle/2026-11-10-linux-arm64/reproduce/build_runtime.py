import hashlib
import json
import pathlib
import subprocess
import sys

root=pathlib.Path('/private/tmp/cim-perf')
kind,commit=sys.argv[1:]
folder=root/'final-wheels'/kind
wheels=list(folder.glob('*.whl'))
assert len(wheels)==1,wheels
wheel=wheels[0]
sha=hashlib.sha256(wheel.read_bytes()).hexdigest()
(folder/'Dockerfile').write_text(
    'FROM 4c4f6d476d4a\n'
    f'LABEL org.opencontainers.image.revision="{commit}"\n'
    f'LABEL powerio.wheel.sha256="{sha}"\n'
    f'COPY {wheel.name} /tmp/{wheel.name}\n'
    f'RUN uv pip install --python /app/.venv/bin/python --no-deps --reinstall /tmp/{wheel.name}\n')
tag=f'localhost/cim-bench/powerio:{kind}-{commit[:8]}'
subprocess.run(['podman','build','--network=none','-t',tag,str(folder)],check=True)
image=subprocess.check_output(['podman','image','inspect',tag,'--format','{{.Id}}'],text=True).strip()
(root/f'{kind}-runtime.json').write_text(json.dumps({'source_commit':commit,'wheel':str(wheel),'wheel_sha256':sha,'tag':tag,'image_id':image},indent=2)+'\n')
print(image)
