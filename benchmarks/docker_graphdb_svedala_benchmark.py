import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from graphdb_adapter import GraphDBAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=GraphDBAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="graphdb",
    dataset_name="svedala"
)
