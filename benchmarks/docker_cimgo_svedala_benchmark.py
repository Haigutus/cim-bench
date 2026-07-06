"""cimgo benchmarks on Svedala dataset (7.3 MB, CGMES 3.0).

Benchmarks validate and convert commands on ALL dataset files.
Requires the cimcli-linux-amd64 binary on PATH (set by container).
"""

import sys
import tempfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))
from cimgo_adapter import (
    COLOR,
    DISPLAY_NAME,
    convert_files,
    get_cimgo_bin,
    resolve_dataset_files,
    validate_files,
)
from subprocess_memory import measure_peak_rss_mb

DATASET_KEY = "svedala_igm_cgmes_3"
DATASET_NAME = "svedala"
CIMGO_BIN = get_cimgo_bin()


@pytest.fixture(scope="module")
def dataset_files():
    files, temp_dir = resolve_dataset_files(DATASET_KEY)
    yield files
    if temp_dir:
        temp_dir.cleanup()


def _set_extra_info(benchmark, operation, peak_mb=None):
    benchmark.extra_info["library"] = "cimgo"
    benchmark.extra_info["dataset"] = DATASET_NAME
    benchmark.extra_info["display_name"] = DISPLAY_NAME
    benchmark.extra_info["color"] = COLOR
    benchmark.extra_info["operation"] = operation
    benchmark.extra_info["binary"] = CIMGO_BIN
    if peak_mb is not None:
        benchmark.extra_info["memory_mb"] = f"{peak_mb:.1f}"


def test_cimgo_load_svedala(benchmark, dataset_files):
    """Benchmark cimgo validate on all Svedala files."""
    assert CIMGO_BIN, "cimgo binary not found on PATH and CIMGO_BIN is unset"

    peak_mb = measure_peak_rss_mb(
        [CIMGO_BIN, "validate", "-json"] + [str(f) for f in dataset_files]
    )
    benchmark(validate_files, CIMGO_BIN, dataset_files)
    _set_extra_info(benchmark, "validate", peak_mb)


def test_cimgo_convert_svedala(benchmark, dataset_files):
    """Benchmark cimgo convert (XML to JSON) on all Svedala files."""
    assert CIMGO_BIN, "cimgo binary not found on PATH and CIMGO_BIN is unset"

    with tempfile.TemporaryDirectory() as tmp:
        output_path = Path(tmp) / "output.json"

        peak_mb = measure_peak_rss_mb(
            [CIMGO_BIN, "convert", "-to", "json", "-out", str(output_path)]
            + [str(f) for f in dataset_files]
        )
        benchmark(convert_files, CIMGO_BIN, dataset_files, output_path)
        _set_extra_info(benchmark, "convert", peak_mb)
