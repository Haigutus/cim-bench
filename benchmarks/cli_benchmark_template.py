"""
Benchmark template generator for CLI-only tools.

CLI tools run as subprocesses: no in-process object, no query tests, and
peak RSS of the child process instead of an in-process memory delta.
Their results are tagged extra_info["tool_type"] = "cli" so reports and
graphs keep them in a separate family (not comparable with libraries).

Usage in benchmark file:
    from cimgo_adapter import DISPLAY_NAME, COLOR, get_cimgo_bin, convert_cmd
    from cli_benchmark_template import CliOperation, create_cli_benchmarks

    create_cli_benchmarks(
        tool_name="cimgo",
        display_name=DISPLAY_NAME,
        color=COLOR,
        binary=get_cimgo_bin(),
        operations={"convert": CliOperation(convert_cmd, "CGMES to JSON", output_files=("output.json",))},
        dataset_key="svedala_igm_cgmes_3",
        dataset_name="svedala",
    )

Use CliOperation to declare status/output contracts for each command builder.
Builders receive (binary, files, tmp_dir) and return list[str].
"""

from dataclasses import dataclass
from collections.abc import Callable
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from datasets import DATASETS
from subprocess_memory import measure_peak_rss_mb


@dataclass(frozen=True)
class CliOperation:
    """Command contract, including expected outputs and meaningful nonzero exits."""

    build_cmd: Callable
    description: str
    output_files: tuple[str, ...] = ()
    accepted_returncodes: tuple[int, ...] = (0,)
    inspect_result: Callable | None = None


def check_result(result, operation, directory):
    assert result.returncode in operation.accepted_returncodes, (
        f"CLI exited {result.returncode}; expected {operation.accepted_returncodes}"
    )
    outputs = [directory / name for name in operation.output_files]
    for output in outputs:
        assert output.is_file() and output.stat().st_size > 0, f"missing nonempty output: {output.name}"
    evidence = {"output_file_count": len(outputs),
                "output_bytes": sum(path.stat().st_size for path in outputs)}
    if operation.inspect_result:
        evidence.update(operation.inspect_result(result))
    return evidence


def resolve_dataset_files(dataset_key):
    """Return (list[Path], temp_dir_or_None) for a dataset.

    Extracts ZIP if needed. Caller must call temp_dir.cleanup() when done.
    """
    dataset = DATASETS[dataset_key]

    if "ZIP" in dataset:
        assert len([key for key in dataset if not key.startswith("_")]) == 1, (
            "ZIP inputs with external companions need an explicit merged dataset"
        )
        temp_dir = tempfile.TemporaryDirectory()
        try:
            with zipfile.ZipFile(dataset["ZIP"]) as archive:
                archive.extractall(temp_dir.name)
            files = sorted(Path(temp_dir.name).rglob("*.xml"))
            assert files, "CLI dataset ZIP contains no XML profiles"
        except Exception:
            temp_dir.cleanup()
            raise
        return files, temp_dir

    files = [Path(v) for k, v in dataset.items() if not k.startswith("_")]
    assert files and all(path.is_file() for path in files), "missing registered CLI dataset inputs"
    return files, None


def get_binary_version(binary):
    """Best-effort version from `binary --version` (None if unsupported)."""
    try:
        result = subprocess.run([binary, "--version"], capture_output=True, text=True, timeout=10)
        output = (result.stdout or result.stderr).strip()
        if result.returncode != 0 or not output or output.lower().startswith("usage"):
            return None
        return output.splitlines()[0]
    except (OSError, subprocess.TimeoutExpired):
        return None


def run_command(cmd, capture_stdout=False):
    """Return actual command status/output for untimed contract verification."""
    return subprocess.run(cmd, stdout=subprocess.PIPE if capture_stdout else subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)


def create_cli_benchmarks(tool_name, display_name, color, binary, operations, dataset_key, dataset_name, tags=None):
    """
    Create one benchmark test per CLI operation and inject them into the
    caller's module namespace (mirrors benchmark_template.create_benchmarks).

    Args:
        tool_name: Short name (e.g. "cimgo")
        display_name: Name shown in graphs/reports
        color: Hex color for graphs
        binary: Resolved binary path (or None - tests will fail with a clear message)
        operations: dict of {operation_name: CliOperation}; bare command builders
            remain supported with successful-exit-only checks.
        dataset_key: Key in DATASETS dict
        dataset_name: Short name for dataset (e.g. "svedala")
        tags: Capability/language tags for site filtering ("cli" always included)
    """
    import inspect
    caller_globals = inspect.currentframe().f_back.f_globals

    metadata = DATASETS[dataset_key]["_metadata"]
    version = get_binary_version(binary) if binary else None
    tags = list(dict.fromkeys(["cli"] + (tags or [])))

    @pytest.fixture(scope="module")
    def dataset_files():
        files, temp_dir = resolve_dataset_files(dataset_key)
        yield files
        if temp_dir:
            temp_dir.cleanup()

    caller_globals["dataset_files"] = dataset_files

    def make_test(operation, spec):
        if not isinstance(spec, CliOperation):
            spec = CliOperation(spec, operation)

        def test_operation(benchmark, dataset_files, pytestconfig, request):
            executions = []
            request.node.user_properties.append(("cim_bench_cli", {
                "operation": operation, "description": spec.description,
                "accepted_returncodes": list(spec.accepted_returncodes),
                "expected_output_files": list(spec.output_files), "executions": executions,
            }))
            benchmark.extra_info.update({
                "tool_type": "cli", "tags": tags, "library": tool_name,
                "operation": operation, "operation_description": spec.description,
                "dataset": dataset_name, "dataset_key": dataset_key,
                "dataset_size_mb": metadata["size_mb"], "cgmes_version": metadata["cgmes_version"],
                "display_name": display_name, "color": color,
                "binary": Path(binary).name if binary else None,
                "accepted_returncodes": list(spec.accepted_returncodes),
                "expected_output_files": list(spec.output_files),
                "timing_method": "one_subprocess_per_round_with_fresh_destination",
                "preparation_and_verification_timed": False,
                "stdout_capture_timed": spec.inspect_result is not None,
                "memory_method": "polled_direct_child_RSS_peak_single_untimed_command",
                "memory_is_exact_peak": False, "memory_includes_startup": True,
                "memory_includes_descendants": False,
                "independent_consumer": "not_run_by_this_benchmark",
            })
            if version:
                benchmark.extra_info["library_version"] = version
            assert binary, f"{tool_name} binary not found on PATH and env var is unset"

            with tempfile.TemporaryDirectory() as tmp:
                directory = Path(tmp) / "operation"

                def prepare_round():
                    if directory.exists():
                        shutil.rmtree(directory)
                    directory.mkdir()
                    cmd = spec.build_cmd(binary, dataset_files, directory)
                    return (cmd,), {}

                (cmd,), _ = prepare_round()
                preflight = run_command(cmd, spec.inspect_result is not None)
                executions.append({"phase": "preflight", "returncode": preflight.returncode})
                benchmark.extra_info["preflight_returncode"] = preflight.returncode
                benchmark.extra_info.update(check_result(preflight, spec, directory))

                (cmd,), _ = prepare_round()
                with tempfile.TemporaryFile() as stdout:
                    peak_mb, memory_returncode = measure_peak_rss_mb(cmd, stdout=stdout)
                    stdout.seek(0)
                    memory_result = subprocess.CompletedProcess(cmd, memory_returncode, stdout=stdout.read())
                executions.append({"phase": "memory", "returncode": memory_returncode})
                benchmark.extra_info["memory_mb"] = peak_mb
                benchmark.extra_info["memory_returncode"] = memory_returncode
                check_result(memory_result, spec, directory)

                last_result = None

                def run_once(cmd):
                    nonlocal last_result
                    last_result = run_command(cmd, spec.inspect_result is not None)
                    return last_result

                def verify_round(cmd):
                    executions.append({"phase": "timed", "returncode": last_result.returncode})
                    benchmark.extra_info.update(check_result(last_result, spec, directory))

                result = benchmark.pedantic(run_once, setup=prepare_round, teardown=verify_round,
                                            rounds=pytestconfig.getoption("benchmark_min_rounds"), iterations=1)
                benchmark.extra_info["timed_last_returncode"] = result.returncode

        test_operation.__name__ = f"test_{tool_name}_{operation}_{dataset_name}"
        test_operation._cim_bench_dataset_key = dataset_key
        return test_operation

    for operation, build_cmd in operations.items():
        test = make_test(operation, build_cmd)
        caller_globals[test.__name__] = test
