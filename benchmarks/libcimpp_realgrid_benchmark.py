import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from libcimpp_adapter import LibCIMppAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=LibCIMppAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="libcimpp",
    dataset_name="realgrid"
)
