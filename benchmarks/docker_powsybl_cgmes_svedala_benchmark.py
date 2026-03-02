import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from powsybl_cgmes_adapter import PowsyblCgmesAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=PowsyblCgmesAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="powsybl_cgmes",
    dataset_name="svedala"
)
