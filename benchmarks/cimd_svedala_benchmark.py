"""cimd benchmarks on Svedala dataset (7.3 MB, CGMES 3.0)."""

import sys
from pathlib import Path

import pytest

# Benchmarks require ALL CGMES profiles to be loaded. cimd v0.4.0 takes a
# single file per invocation (multiple args rejected; a multi-profile ZIP
# reads only the EQ profile - verified via FullModel count) and `convert`
# has no SV input, so no cimd operation can cover the full dataset.
pytest.skip("cimd cannot load all CGMES profiles in one invocation",
            allow_module_level=True)

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimd_adapter import COLOR, DISPLAY_NAME, convert_cmd, get_cimd_bin, types_cmd
from cli_benchmark_template import create_cli_benchmarks

create_cli_benchmarks(
    tool_name="cimd",
    display_name=DISPLAY_NAME,
    color=COLOR,
    binary=get_cimd_bin(),
    operations={"types": types_cmd, "convert": convert_cmd},
    dataset_key="svedala_igm_cgmes_3",
    dataset_name="svedala",
    tags=["validator", "serializer", "zig"],
)
