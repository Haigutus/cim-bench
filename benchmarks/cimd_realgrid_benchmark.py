"""cimd benchmarks on RealGrid dataset (86.5 MB, CGMES 2.4.15).

Only the `types` operation: `cimd convert` (v0.4.0) panics on the RealGrid
EQ profile (Zig panic in topology/resolve.zig, with or without TP/SSH).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimd_adapter import COLOR, DISPLAY_NAME, get_cimd_bin, types_cmd
from cli_benchmark_template import create_cli_benchmarks

create_cli_benchmarks(
    tool_name="cimd",
    display_name=DISPLAY_NAME,
    color=COLOR,
    binary=get_cimd_bin(),
    operations={"types": types_cmd},
    dataset_key="realgrid_cgmes_2_4",
    dataset_name="realgrid",
    tags=["validator", "serializer", "zig"],
)
