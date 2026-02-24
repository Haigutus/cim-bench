"""Benchmark for cimpy library - RealGrid dataset (86.5MB).

KNOWN ISSUE: cimpy v1.1.0 has a parsing bug with this dataset.
Error: ValueError: invalid literal for int() with base 10: '60.000000'
The parser tries to convert float values to integers during attribute setting.
Fails in cimimport.py:271 during _set_attributes() phase.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimpy_adapter import CimpyAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=CimpyAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="cimpy",
    dataset_name="realgrid"
)
