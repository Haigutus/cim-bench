"""cimd benchmark on Realgrid EQ.

Times `cimd types` on the Realgrid EQ profile. The Realgrid dataset ships
as a single ZIP; we extract it once at module scope and select the EQ XML.

The `cimd` binary is expected on PATH (set by the container) or overridable
via the CIMD_BIN environment variable for native runs.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))
from datasets import DATASETS  # noqa: E402
from cimd_memory import measure_peak_rss_mb  # noqa: E402

ZIP_PATH = DATASETS["realgrid_cgmes_2_4"]["ZIP"]
CIMD_BIN = os.environ.get("CIMD_BIN") or shutil.which("cimd")


@pytest.fixture(scope="module")
def eq_path():
    tmp_dir = tempfile.TemporaryDirectory()
    zipfile.ZipFile(ZIP_PATH).extractall(tmp_dir.name)
    eq = next((p for p in Path(tmp_dir.name).rglob("*.xml") if "EQ" in p.stem), None)
    if eq is None:
        raise RuntimeError(f"No EQ profile found in {ZIP_PATH}")
    yield eq
    tmp_dir.cleanup()


def cimd_types(eq):
    result = subprocess.run(
        [CIMD_BIN, "types", str(eq)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"cimd types failed: {result.stderr}")
    return result.stdout


def test_cimd_load_realgrid(benchmark, eq_path):
    """Benchmark `cimd types` on Realgrid EQ (named `load` to slot into the
    cross-tool import comparison chart)."""
    assert CIMD_BIN, "cimd binary not found on PATH and CIMD_BIN env var is unset"
    assert ZIP_PATH.exists(), f"Realgrid ZIP missing: {ZIP_PATH}"

    peak_mb = measure_peak_rss_mb([CIMD_BIN, "types", str(eq_path)])
    output = benchmark(cimd_types, eq_path)

    benchmark.extra_info["library"] = "cimd"
    benchmark.extra_info["dataset"] = "realgrid"
    benchmark.extra_info["display_name"] = "cimd"
    benchmark.extra_info["color"] = "#f39c12"
    benchmark.extra_info["operation"] = "types"
    benchmark.extra_info["type_count"] = sum(1 for line in output.splitlines() if line.strip())
    benchmark.extra_info["memory_mb"] = f"{peak_mb:.1f}"
    benchmark.extra_info["binary"] = CIMD_BIN


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "--benchmark-only", "-v"]))
