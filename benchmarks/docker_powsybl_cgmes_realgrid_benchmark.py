import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from powsybl_cgmes_adapter import PowsyblCgmesAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=PowsyblCgmesAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="powsybl_cgmes",
    dataset_name="realgrid"
)
