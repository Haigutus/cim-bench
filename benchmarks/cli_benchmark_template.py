"""
Benchmark template generator for CLI-only tools.

CLI tools run as subprocesses: no in-process object, no query tests, and
peak RSS of the child process instead of an in-process memory delta.
Their results are tagged extra_info["tool_type"] = "cli" so reports and
graphs keep them in a separate family (not comparable with libraries).

Usage in benchmark file:
    from cimgo_adapter import DISPLAY_NAME, COLOR, get_cimgo_bin, validate_cmd, convert_cmd
    from cli_benchmark_template import create_cli_benchmarks

    create_cli_benchmarks(
        tool_name="cimgo",
        display_name=DISPLAY_NAME,
        color=COLOR,
        binary=get_cimgo_bin(),
        operations={"validate": validate_cmd, "convert": convert_cmd},
        dataset_key="svedala_igm_cgmes_3",
        dataset_name="svedala",
    )

Each operation is a callable (binary, files, tmp_dir) -> list[str] command.
"""

import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from datasets import DATASETS
from subprocess_memory import measure_peak_rss_mb


def resolve_dataset_files(dataset_key):
    """Return (list[Path], temp_dir_or_None) for a dataset.

    Extracts ZIP if needed. Caller must call temp_dir.cleanup() when done.
    """
    dataset = DATASETS[dataset_key]

    if "ZIP" in dataset:
        temp_dir = tempfile.TemporaryDirectory()
        zipfile.ZipFile(dataset["ZIP"]).extractall(temp_dir.name)
        files = list(Path(temp_dir.name).rglob("*.xml"))
        return files, temp_dir

    files = [Path(v) for k, v in dataset.items() if "_metadata" not in k.lower()]
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


def run_command(cmd):
    """Run a CLI command, discarding output (return code intentionally ignored:
    e.g. `cimgo validate` exits 1 when violations are found)."""
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def create_cli_benchmarks(tool_name, display_name, color, binary, operations, dataset_key, dataset_name, tags=None):
    """
    Create one benchmark test per CLI operation and inject them into the
    caller's module namespace (mirrors benchmark_template.create_benchmarks).

    Args:
        tool_name: Short name (e.g. "cimgo")
        display_name: Name shown in graphs/reports
        color: Hex color for graphs
        binary: Resolved binary path (or None - tests will fail with a clear message)
        operations: dict of {operation_name: build_cmd(binary, files, tmp_dir) -> list[str]}
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

    def make_test(operation, build_cmd):
        def test_operation(benchmark, dataset_files):
            assert binary, f"{tool_name} binary not found on PATH and env var is unset"

            with tempfile.TemporaryDirectory() as tmp:
                cmd = build_cmd(binary, dataset_files, Path(tmp))
                peak_mb = measure_peak_rss_mb(cmd)
                benchmark(run_command, cmd)

            benchmark.extra_info["tool_type"] = "cli"
            benchmark.extra_info["tags"] = tags
            benchmark.extra_info["library"] = tool_name
            benchmark.extra_info["operation"] = operation
            benchmark.extra_info["dataset"] = dataset_name
            benchmark.extra_info["dataset_size_mb"] = metadata["size_mb"]
            benchmark.extra_info["cgmes_version"] = metadata["cgmes_version"]
            benchmark.extra_info["display_name"] = display_name
            benchmark.extra_info["color"] = color
            benchmark.extra_info["binary"] = binary
            benchmark.extra_info["memory_mb"] = f"{peak_mb:.1f}"
            if version:
                benchmark.extra_info["library_version"] = version

        test_operation.__name__ = f"test_{tool_name}_{operation}_{dataset_name}"
        return test_operation

    for operation, build_cmd in operations.items():
        test = make_test(operation, build_cmd)
        caller_globals[test.__name__] = test
