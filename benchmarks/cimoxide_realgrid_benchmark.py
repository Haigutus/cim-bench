import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimoxide_adapter import CimoxideAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=CimoxideAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="cimoxide",
    dataset_name="realgrid"
)
