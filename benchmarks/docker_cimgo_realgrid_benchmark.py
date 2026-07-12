"""cimgo benchmarks on RealGrid dataset (86.5 MB, CGMES 2.4.15)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimgo_adapter import COLOR, DISPLAY_NAME, convert_cmd, get_cimgo_bin, validate_cmd
from cli_benchmark_template import create_cli_benchmarks

create_cli_benchmarks(
    tool_name="cimgo",
    display_name=DISPLAY_NAME,
    color=COLOR,
    binary=get_cimgo_bin(),
    operations={"validate": validate_cmd, "convert": convert_cmd},
    dataset_key="realgrid_cgmes_2_4",
    dataset_name="realgrid",
    tags=["validator", "serializer", "go"],
)
