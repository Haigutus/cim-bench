"""Capture complete IR, replay, diagnostics and fresh output before/after cache."""
import hashlib
import json
from pathlib import Path
import sys

import powerio

BUILD = Path('/private/tmp/cim-perf')
ROOT = Path('/Users/samuel/datasets/powerio-rc-2026-11-10')
sys.path.insert(0, str(BUILD / 'harness-ea54449/parsers'))
from datasets import DATASETS


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files(folder):
    return {str(p.relative_to(folder)): digest(p) for p in sorted(folder.rglob('*')) if p.is_file()}


kind = sys.argv[1]
root = ROOT / 'namespace-2d570215-semantics-v2' / kind
root.mkdir(parents=True)
records = []
for case, source in [
    ('svedala', BUILD / 'cgmes-profile-4dcd8812/svedala-input'),
    ('realgrid', Path(DATASETS['realgrid_cgmes_2_4']['ZIP'])),
]:
    out = root / case
    out.mkdir()
    module = powerio.parse(source, format='cgmes')
    powerio.serialize(module, out / 'network.pio.json')
    replay = powerio.emit(module, 'cgmes', out / 'replay')
    fresh = powerio.emit(module.sever_source(), 'cgmes', out / 'fresh')
    restored = powerio.deserialize(out / 'network.pio.json')
    powerio.emit(restored, 'cgmes', out / 'restored')
    assert files(out / 'fresh') == files(out / 'restored')
    record = {'case': case, 'source': str(source), 'ir_sha256': digest(out / 'network.pio.json'),
              'replay': files(out / 'replay'), 'fresh': files(out / 'fresh'),
              'restored': files(out / 'restored'),
              'read_diagnostics': [(d.code, d.message) for d in module.diagnostics],
              'emit_diagnostics': [(d.code, d.message) for d in fresh.diagnostics]}
    records.append(record)
(root / 'receipt.json').write_text(json.dumps(records, indent=2) + '\n')
print(json.dumps({'kind': kind, 'cases': [{k: v for k, v in row.items() if k in ('case', 'ir_sha256')} for row in records]}))
