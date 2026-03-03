import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from maplib_adapter import MaplibAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=MaplibAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="maplib",
    dataset_name="svedala"
)
