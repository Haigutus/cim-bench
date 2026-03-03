import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from libcimpp_adapter import LibCIMppAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=LibCIMppAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="libcimpp",
    dataset_name="svedala"
)
