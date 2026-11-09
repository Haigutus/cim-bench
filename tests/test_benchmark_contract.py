"""Failure cases that must not produce successful benchmark evidence."""

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "parsers"), str(ROOT / "benchmarks")]
from benchmark_template import export_files, prepare_export_output

pytest_plugins = ["pytester"]


def test_fresh_export_cannot_reuse_a_previous_round(tmp_path):
    output = tmp_path / "output" / "export.xml"
    prepare_export_output(output)
    output.write_text("old result")
    prepare_export_output(output)
    with pytest.raises(AssertionError, match="no nonempty"):
        export_files(output)
    (output.parent / "profiles").mkdir()
    (output.parent / "profiles" / "EQ.xml").write_text("fresh profile")
    assert [p.name for p in export_files(output)] == ["EQ.xml"]


def test_input_evidence_hashes_bytes_without_absolute_paths(tmp_path):
    spec = importlib.util.spec_from_file_location("benchmark_evidence", ROOT / "benchmarks" / "conftest.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    source = tmp_path / "EQ.xml"
    source.write_bytes(b"profile bytes")
    evidence = module.input_evidence({"EQ": source, "SSH": tmp_path / "missing.xml",
                                      "_metadata": {"cgmes_version": "3.0"}})
    assert evidence["inputs"][0] == {"role": "EQ", "name": "EQ.xml", "present": True,
                                    "sha256": hashlib.sha256(b"profile bytes").hexdigest(), "bytes": 13}
    assert evidence["inputs"][1]["present"] is False
    assert str(tmp_path) not in str(evidence)


def test_generated_benchmark_records_fresh_rounds_and_provenance(pytester):
    pytester.makeconftest((ROOT / "benchmarks" / "conftest.py").read_text())
    source = pytester.path / "EQ.xml"
    source.write_text("synthetic profile")
    pytester.makepyfile(f'''
import sys
from pathlib import Path
sys.path[:0] = [{str(ROOT / "parsers")!r}, {str(ROOT / "benchmarks")!r}]
from parser_adapter import ParserAdapter
from datasets import DATASETS
from benchmark_template import create_benchmarks
DATASETS["synthetic"] = {{"EQ": Path({str(source)!r}), "_metadata": {{"cgmes_version": "3.0", "size_mb": 0.01}}}}
class Adapter(ParserAdapter):
    @classmethod
    def get_display_name(cls): return "Synthetic"
    @classmethod
    def get_color(cls): return "#123456"
    def load(self, key): return object()
    def get_load_metrics(self, value, memory): return {{"memory_mb": memory}}
    def get_lines_count(self, value): return 1
    def get_generators_count(self, value): return 1
    def get_loads_count(self, value): return 1
    def get_substations_count(self, value): return 1
    def export(self, value, output):
        target = output.parent / "profiles"
        target.mkdir()  # A repeated write without fresh setup would fail.
        (target / "EQ.xml").write_text("fresh profile")
create_benchmarks(Adapter(), "synthetic", "synthetic", "synthetic")
''')
    result = pytester.runpytest("--benchmark-min-rounds=2", "--benchmark-max-time=0.01",
                              "--benchmark-json=report.json", "-q")
    result.assert_outcomes(passed=6)
    report = json.loads((pytester.path / "report.json").read_text())
    export = next(item for item in report["benchmarks"] if item["extra_info"].get("operation") == "export")
    assert export["stats"]["rounds"] == 2
    assert export["stats"]["iterations"] == 1
    assert export["extra_info"]["export_file_count"] == 1
    evidence = report["cim_bench_evidence"]
    assert evidence["datasets"]["synthetic"]["inputs"][0]["sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert len(evidence["tests"]) == 6
