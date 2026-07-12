"""GMSS CIM (.NET via pythonnet) benchmarks on Svedala dataset (7.3 MB, CGMES 3.0)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from gmss_adapter import GmssAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=GmssAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="gmss",
    dataset_name="svedala"
)
