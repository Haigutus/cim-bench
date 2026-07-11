"""pocket-rdf benchmarks on RealGrid dataset (86.5 MB, CGMES 2.4.15)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from pocket_rdf_adapter import COLOR, DISPLAY_NAME, get_pocket_rdf_bin, query_cmd, serialize_cmd
from cli_benchmark_template import create_cli_benchmarks

create_cli_benchmarks(
    tool_name="pocket_rdf",
    display_name=DISPLAY_NAME,
    color=COLOR,
    binary=get_pocket_rdf_bin(),
    operations={"serialize": serialize_cmd, "query": query_cmd},
    dataset_key="realgrid_cgmes_2_4",
    dataset_name="realgrid",
    tags=["serializer", "query", "sparql", "python"],
)
