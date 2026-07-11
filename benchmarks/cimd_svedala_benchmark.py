"""cimd benchmarks on Svedala dataset (7.3 MB, CGMES 3.0)."""

import sys
from pathlib import Path

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
