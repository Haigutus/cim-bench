"""PowerIO fresh-load, native-count, and fresh-export measurements."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))
from powerio_adapter import PowerIOAdapter
from benchmark_template import create_benchmarks

create_benchmarks(PowerIOAdapter(), "realgrid_cgmes_2_4", "powerio", "realgrid")
