import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from jena_adapter import JenaAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=JenaAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="jena",
    dataset_name="realgrid"
)
