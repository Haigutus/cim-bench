import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from graphdb_adapter import GraphDBAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=GraphDBAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="graphdb",
    dataset_name="realgrid"
)
