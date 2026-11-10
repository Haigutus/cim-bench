"""The lifecycle probe must expose deferred work and preserve failed attempts."""
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest

SPEC = importlib.util.spec_from_file_location(
    "measure_lifecycle", Path(__file__).parents[1] / "tools/measure_lifecycle.py")
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


def run_probe(monkeypatch, tmp_path, adapter, *options):
    output = tmp_path / "sample.json"
    monkeypatch.setitem(sys.modules, "powerio_adapter", SimpleNamespace(
        PowerIOAdapter=adapter, __file__=__file__))
    monkeypatch.setattr(sys, "argv", ["probe", "powerio", "svedala_igm_cgmes_3",
                                    str(output), "--warm-rounds", "2",
                                    "--warm-target-ms", "0.001", *options])
    status = probe.main()
    return status, json.loads(output.read_text()), output


@pytest.mark.parametrize("git_present", [True, False])
def test_first_query_precedes_warm_work_and_never_reads_load_metrics(monkeypatch, tmp_path, git_present):
    if not git_present:
        def missing_git(*args, **kwargs):
            raise FileNotFoundError("git is not installed")
        monkeypatch.setattr(probe.subprocess, "run", missing_git)
    events = []

    class Adapter:
        def load(self, dataset):
            events.append("load")
            return {"ready": False}

        def get_loads_count(self, loaded):
            events.append("warm" if loaded["ready"] else "first")
            loaded["ready"] = True
            return 3

        def get_load_metrics(self, *args):
            raise AssertionError("metrics must not precompute the query")

        def get_version(self):
            return "synthetic"

        def get_measurement_notes(self):
            return {"query_family": "synthetic"}

    status, result, output = run_probe(monkeypatch, tmp_path, Adapter, "--query", "loads")
    assert status == 0
    assert events[:2] == ["load", "first"]
    assert events.count("load") == events.count("first") == 1
    assert set(result["queries"]) == {"loads"}
    assert result["queries"]["loads"]["count"] == 3
    assert len(result["queries"]["loads"]["warm"]["batch_elapsed_ns"]) == 2
    assert result["load_to_use_ns"] >= result["load_ns"]
    if not git_present:
        assert result["observed_harness_commit"] is None
        assert result["observed_harness_dirty"] is None
        assert result["harness_observation_error"]["type"] == "FileNotFoundError"
    before = output.read_bytes()
    with pytest.raises(SystemExit):
        probe.main()
    assert output.read_bytes() == before


@pytest.mark.parametrize("git_present", [True, False])
def test_failed_load_is_a_preserved_result(monkeypatch, tmp_path, git_present):
    if not git_present:
        def missing_git(*args, **kwargs):
            raise FileNotFoundError("git is not installed")
        monkeypatch.setattr(probe.subprocess, "run", missing_git)
    class Adapter:
        def load(self, dataset):
            raise ValueError("synthetic incomplete input")

        def get_lines_count(self, loaded):
            raise AssertionError("failed load cannot be queried")

    status, result, _ = run_probe(monkeypatch, tmp_path, Adapter, "--query", "lines")
    assert status == 1
    assert result["status"] == "failed"
    assert result["error"] == {"type": "ValueError", "message": "synthetic incomplete input"}
    assert result["queries"] == {}
    assert "load_to_use_ns" not in result
    if not git_present:
        assert result["observed_harness_commit"] is None
        assert result["observed_harness_dirty"] is None
        assert result["harness_observation_error"]["type"] == "FileNotFoundError"


def test_warm_queries_cannot_silently_change_results():
    with pytest.raises(ValueError, match="query changed"):
        probe.warm_query(lambda _: 2, None, expected=1, rounds=2, target_ns=1000)
