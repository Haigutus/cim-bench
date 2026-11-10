"""Exercise the real native reader/writer with small generated CGMES profiles."""

import io
from pathlib import Path
import sys

import pytest
import powerio

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "parsers"), str(ROOT / "benchmarks")]
from benchmark_template import export_files, prepare_export_output
from datasets import DATASETS
from parser_adapter import IncompleteLoadError
from powerio_adapter import PowerIOAdapter

CASE = """function mpc = case2
mpc.version = '2';
mpc.baseMVA = 100;
mpc.bus = [1 3 0 0 0 0 1 1 0 230 1 1.1 0.9; 7 1 10 2 0 0 1 1 0 230 1 1.1 0.9];
mpc.gen = [1 10 2 50 -50 1 100 1 100 0];
mpc.branch = [1 7 0.01 0.1 0 100 100 100 0 0 1 -360 360];
"""


@pytest.fixture
def dataset(tmp_path, monkeypatch):
    module = powerio.parse(io.StringIO(CASE), format="matpower")
    output = tmp_path / "input"
    powerio.emit(module, "cgmes", output)
    files = {path.stem: path for path in output.rglob("*.xml")}
    assert len(files) == 4
    files["_metadata"] = {"cgmes_version": "3.0", "size_mb": 0.01}
    monkeypatch.setitem(DATASETS, "synthetic", files)
    return files


def test_missing_registered_profile_never_produces_a_partial_load(dataset):
    path = next(value for key, value in dataset.items() if not key.startswith("_"))
    path.unlink()
    with pytest.raises(IncompleteLoadError, match="missing registered inputs"):
        PowerIOAdapter().load("synthetic")


def test_independent_loads_and_repeated_fresh_export(dataset, tmp_path):
    adapter = PowerIOAdapter()
    first = adapter.load("synthetic")
    second = adapter.load("synthetic")
    assert first is not second
    assert first.network.n_lines == second.network.n_lines == 1
    assert first.network.n_generators == second.network.n_generators == 1
    output = tmp_path / "output" / "export.xml"
    for _ in range(2):
        prepare_export_output(output)
        adapter.export(first, output)
        assert len(export_files(output)) == 4
        metrics = adapter.get_export_metrics(first, output)
        assert metrics["fresh_export_reparse_counts"]["lines"] == 1
        assert metrics["independent_consumer"] == "not_run_by_this_benchmark"
    assert first.network.n_loads == 1
