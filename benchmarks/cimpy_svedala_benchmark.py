"""Benchmark for cimpy library - Svedala IGM dataset (7.3MB).

KNOWN ISSUE: cimpy v1.1.0 does not support CGMES 3.0.
Only cgmes_v2_4_15 module is available, so all classes show as "not implemented".
This results in empty topology with 0 element counts.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimpy_adapter import CimpyAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=CimpyAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="cimpy",
    dataset_name="svedala"
)
