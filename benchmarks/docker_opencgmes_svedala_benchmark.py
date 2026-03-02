import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from opencgmes_adapter import OpenCGMESAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=OpenCGMESAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="opencgmes",
    dataset_name="svedala"
)
