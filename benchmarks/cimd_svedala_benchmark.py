"""cimd benchmark on Svedala EQ.

Times `cimd types` on the Svedala EQ profile. This parses the CGMES XML and
emits per-type object counts — comparable in scope to the load+index step
other adapters measure.

cimd is a standalone CLI, so the adapter/template machinery doesn't apply
(no shared in-memory model across calls). The `cimd` binary is expected on
PATH (set by the container) or overridable via the CIMD_BIN environment
variable for native runs.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))
from datasets import DATASETS  # noqa: E402
from cimd_memory import measure_peak_rss_mb  # noqa: E402

EQ_PATH = DATASETS["svedala_igm_cgmes_3"]["EQ"]
CIMD_BIN = os.environ.get("CIMD_BIN") or shutil.which("cimd")


def cimd_types(eq):
    result = subprocess.run(
        [CIMD_BIN, "types", str(eq)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"cimd types failed: {result.stderr}")
    return result.stdout


def test_cimd_load_svedala(benchmark):
    """Benchmark `cimd types` on Svedala EQ (named `load` to slot into the
    cross-tool import comparison chart)."""
    assert CIMD_BIN, "cimd binary not found on PATH and CIMD_BIN env var is unset"
    assert EQ_PATH.exists(), f"Svedala EQ missing: {EQ_PATH}"

    peak_mb = measure_peak_rss_mb([CIMD_BIN, "types", str(EQ_PATH)])
    output = benchmark(cimd_types, EQ_PATH)

    benchmark.extra_info["library"] = "cimd"
    benchmark.extra_info["dataset"] = "svedala"
    benchmark.extra_info["display_name"] = "cimd"
    benchmark.extra_info["color"] = "#f39c12"
    benchmark.extra_info["operation"] = "types"
    benchmark.extra_info["type_count"] = sum(1 for line in output.splitlines() if line.strip())
    benchmark.extra_info["memory_mb"] = f"{peak_mb:.1f}"
    benchmark.extra_info["binary"] = CIMD_BIN


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "--benchmark-only", "-v"]))
