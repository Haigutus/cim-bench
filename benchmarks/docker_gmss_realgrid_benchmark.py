"""GMSS CIM (.NET via pythonnet) benchmarks on RealGrid dataset (86.5 MB, CGMES 2.4.15)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from gmss_adapter import GmssAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=GmssAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="gmss",
    dataset_name="realgrid"
)
