"""Native PowSyBl field oracle after CGMES re-import, using synthetic phase taps.

The expected physical parameters are computed from the synthetic input, not
from PowerIO's own re-import. Both before and after cache wheels run this.
"""
import hashlib
import io
import json
import math
from pathlib import Path
import sys
import traceback
import xml.etree.ElementTree as ET
import zipfile

import powerio
import pypowsybl as pp

ROOT = Path('/Users/samuel/datasets/powerio-rc-2026-11-10')


def load(profiles):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as archive:
        for name, contents in profiles.items():
            archive.writestr(name, contents)
    buffer.seek(0)
    return pp.network.load_from_binary_buffers([buffer])


def check():
    kind = sys.argv[1]
    output = ROOT / 'namespace-2d570215-native-oracle-v2' / kind
    output.mkdir(parents=True)
    rows, failures = [], []
    for kv in (20.0, 220.0):
        for tap in (0.9, 1.0, 1.05, 1.2):
            for shift in (-10.0, 10.0, 25.0):
                index = len(rows)
                folder = output / str(index)
                folder.mkdir()
                source = folder / 'case.m'
                source.write_text(f"""function mpc = case_phase
mpc.version = '2';
mpc.baseMVA = 100;
mpc.bus = [1 3 0 0 0 0 1 1 0 220 1 1.1 0.9;
           2 1 10 2 0 0 1 1 0 {kv} 1 1.1 0.9];
mpc.gen = [1 10 2 100 -100 1 100 1 100 0];
mpc.branch = [1 2 0.01 0.1 0 150 150 150 {tap} {shift} 1 -360 360];
mpc.gencost = [2 0 0 2 1 0];
""")
                row = dict(kv=kv, tap=tap, shift=shift, input_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
                try:
                    original = powerio.parse(source)
                    powerio.emit(original, 'cgmes', folder / 'original')
                    imported = powerio.parse(folder / 'original', format='cgmes')
                    powerio.emit(imported.sever_source(), 'cgmes', folder / 'fresh')
                    observed = {}
                    for stage in ('original', 'fresh'):
                        profiles = {p.name: p.read_bytes() for p in (folder / stage).glob('*.xml')}
                        native = load(profiles)
                        transformers = native.get_2_windings_transformers()
                        assert len(transformers) == 1
                        transformer = transformers.iloc[0]
                        assert math.isclose(transformer.x, 0.1 * kv ** 2 / 100, rel_tol=1e-10)
                        assert math.isclose(transformer.r, 0.01 * kv ** 2 / 100, rel_tol=1e-10)
                        assert math.isclose(transformer.rated_u1, 220 * tap, rel_tol=1e-10)
                        assert math.isclose(transformer.rated_u2, kv, rel_tol=1e-10)
                        steps = native.get_phase_tap_changer_steps()
                        assert len(steps) == 3
                        for field in ('r', 'x', 'g', 'b'):
                            assert (steps[field].abs() < 1e-9).all(), (stage, field, steps.to_dict())
                        assert sorted(steps.alpha) == sorted((0, -shift, -2 * shift))
                        observed[stage] = dict(r=float(transformer.r), x=float(transformer.x),
                                               rated_u1=float(transformer.rated_u1), rated_u2=float(transformer.rated_u2),
                                               steps={str(k): list(map(float, steps[k])) for k in ('r', 'x', 'g', 'b', 'alpha')})
                        if tap != 1 and shift > 0:
                            mutated = dict(profiles)
                            changes = 0
                            for name, data in profiles.items():
                                if name.endswith('_EQ.xml'):
                                    xml = ET.fromstring(data)
                                    for element in xml.iter():
                                        if element.tag.rsplit('}', 1)[-1] in ('PhaseTapChangerLinear.xMin', 'PhaseTapChangerLinear.xMax'):
                                            element.text = str(0.1 * 220 ** 2 / 100)
                                            changes += 1
                                        if stage == 'fresh' and element.tag.rsplit('}', 1)[-1] == 'TapChangerTablePoint.x':
                                            element.text = '5'
                                            changes += 1
                                    mutated[name] = ET.tostring(xml)
                            assert changes > 0, (stage, 'negative control did not change an input')
                            wrong = load(mutated).get_phase_tap_changer_steps()
                            expected = 100 * (1 / tap ** 2 - 1) if stage == 'original' else 5.0
                            assert all(math.isclose(value, expected, abs_tol=1e-9) for value in wrong.x), (stage, expected, list(wrong.x))
                            observed[stage]['negative_control'] = dict(changed_fields=changes, expected_x_percent=expected, observed_x_percent=list(map(float, wrong.x)))
                    row.update(status='pass', observed=observed)
                except Exception as error:
                    row.update(status='failed', error=dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc()))
                    failures.append(row.copy())
                rows.append(row)
    report = dict(kind=kind, powerio_version=powerio.__version__, pypowsybl_version=pp.__version__,
                  scope='24 synthetic phase-tap/base cases, native imported parameters before and after PowerIO CGMES read/fresh emit; negative controls recreate known wrong voltage base. No power flow solve or comprehensive CGMES conformance claim.',
                  rows=rows, failures=failures)
    (output / 'receipt.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(dict(kind=kind, cases=len(rows), failures=len(failures), pypowsybl=pp.__version__)))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(check())
