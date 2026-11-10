"""A fast CLI, a broken CLI and an empty exporter must yield different evidence."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "parsers"), str(ROOT / "benchmarks")]
from cimgo_adapter import inspect_validation
from cli_benchmark_template import CliOperation, check_result, run_command

pytest_plugins = ["pytester"]


def test_crashed_cli_and_unstructured_validation_error_fail(tmp_path):
    crashed = run_command([sys.executable, "-c", "raise SystemExit(139)"])
    with pytest.raises(AssertionError, match="exited 139"):
        check_result(crashed, CliOperation(lambda: None, "synthetic"), tmp_path)
    with pytest.raises(json.JSONDecodeError):
        inspect_validation(subprocess.CompletedProcess([], 1, stdout=b""))
    with pytest.raises(AssertionError, match="disagrees"):
        inspect_validation(subprocess.CompletedProcess([], 1, stdout=b"[]"))
    report = json.dumps([{"Severity": "sh:Violation"}]).encode()
    assert inspect_validation(subprocess.CompletedProcess([], 1, stdout=report)) == {
        "validation_report_entries": 1, "validation_violation_count": 1,
        "validation_outcome": "violations_reported"}


def test_cli_success_failure_empty_output_and_input_provenance(pytester):
    pytester.makeconftest((ROOT / "benchmarks" / "conftest.py").read_text())
    source = pytester.path / "EQ.xml"
    source.write_text("synthetic CLI input")
    validation_code = "print(" + repr(json.dumps([{"Severity": "sh:Violation"}])) + "); raise SystemExit(1)"
    # Separate generated files avoid fixture names colliding across tools.
    for mode in ["success", "failed", "empty", "vanishing", "violations"]:
        pytester.makepyfile(**{f"test_{mode}": f'''
import sys
from pathlib import Path
sys.path[:0] = [{str(ROOT / "parsers")!r}, {str(ROOT / "benchmarks")!r}]
from datasets import DATASETS
from cimgo_adapter import inspect_validation
from cli_benchmark_template import CliOperation, create_cli_benchmarks
DATASETS["synthetic_cli"] = {{"EQ": Path({str(source)!r}), "_metadata": {{"cgmes_version": "3.0", "size_mb": 0.01}}}}
calls = 0
def command(binary, files, directory):
    global calls
    calls += 1
    if {mode!r} == "failed": code = "raise SystemExit(7)"
    elif {mode!r} == "violations": code = {validation_code!r}
    elif {mode!r} == "empty" or ({mode!r} == "vanishing" and calls > 2): code = "pass"
    else:
        # Exclusive creation proves every preflight/memory/timed run is fresh.
        code = "from pathlib import Path; Path(" + repr(str(directory / "output.xml")) + ").open('x').write('fresh')"
    return [binary, "-c", code]
spec = (CliOperation(command, "synthetic validation", accepted_returncodes=(0,1), inspect_result=inspect_validation)
        if {mode!r} == "violations" else CliOperation(command, "synthetic serialization", output_files=("output.xml",)))
create_cli_benchmarks({mode!r}, "Synthetic", "#123456", sys.executable,
                      {{"operation": spec}}, "synthetic_cli", "synthetic")
'''})
    result = pytester.runpytest("--benchmark-min-rounds=2", "--benchmark-json=report.json", "-q")
    result.assert_outcomes(passed=2, failed=3)
    report = json.loads((pytester.path / "report.json").read_text())
    evidence = report["cim_bench_evidence"]
    assert evidence["run"]["exit_status"] == 1
    assert len(evidence["tests"]) == 5
    assert evidence["datasets"]["synthetic_cli"]["inputs"][0]["sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    success = next(row for row in report["benchmarks"] if row["extra_info"]["library"] == "success")
    assert success["stats"]["rounds"] == 2
    assert success["stats"]["iterations"] == 1
    assert success["extra_info"]["timed_last_returncode"] == 0
    assert success["extra_info"]["output_bytes"] == 5
    assert success["extra_info"]["memory_includes_descendants"] is False
    violations = next(row for row in report["benchmarks"] if row["extra_info"]["library"] == "violations")
    assert violations["extra_info"]["validation_outcome"] == "violations_reported"

    # If every preflight fails, the requested report must not be absent or stale.
    (pytester.path / "failed.json").write_text('{"stale": true}')
    failed = pytester.runpytest("test_failed.py", "--benchmark-json=failed.json", "-q")
    failed.assert_outcomes(failed=1)
    report = json.loads((pytester.path / "failed.json").read_text())
    assert report["benchmarks"] == []
    assert report["incomplete_run"] is True
    assert report["cim_bench_evidence"]["run"]["exit_status"] == 1
    assert "synthetic_cli" in report["cim_bench_evidence"]["datasets"]
    assert report["cim_bench_evidence"]["tests"][0]["cli"]["executions"] == [
        {"phase": "preflight", "returncode": 7}]
