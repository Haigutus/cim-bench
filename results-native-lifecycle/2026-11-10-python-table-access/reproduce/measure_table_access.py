"""One fresh-process table-access observation; no query runs before first_ns."""
import hashlib
import json
from pathlib import Path
import platform
import resource
import statistics
import sys
import time

import psutil

case, table, output = sys.argv[1:]
start = time.perf_counter_ns()
import powerio
import_ns = time.perf_counter_ns()-start
proc = psutil.Process()
memory = lambda: {'rss_bytes':proc.memory_info().rss,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
before = memory()
start = time.perf_counter_ns()
module = powerio.parse(case)
value = module.value
load_ns = time.perf_counter_ns()-start
loaded = memory()
start = time.perf_counter_ns()
rows = getattr(value,table)
first_ns = time.perf_counter_ns()-start
first_memory = memory()
fingerprint = hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
iterations = 1
while True:
    start = time.perf_counter_ns()
    for _ in range(iterations):
        current = getattr(value,table)
    elapsed = time.perf_counter_ns()-start
    if elapsed>=20_000_000 or iterations>=2**18:
        break
    iterations *= 2
batches=[]
for _ in range(9):
    start = time.perf_counter_ns()
    for _ in range(iterations):
        current = getattr(value,table)
    batches.append(time.perf_counter_ns()-start)
assert current==rows
record={'case':Path(case).name,'case_sha256':hashlib.sha256(Path(case).read_bytes()).hexdigest(),
        'table':table,'table_rows':len(rows),'table_sha256':fingerprint,'import_ns':import_ns,
        'load_ns':load_ns,'first_ns':first_ns,'load_to_use_ns':load_ns+first_ns,
        'iterations_per_batch':iterations,'warm_batches_ns':batches,
        'warm_ns':statistics.median(batches)/iterations,
        'before':before,'after_load':loaded,'after_first':first_memory,'after_warm':memory(),
        'python':sys.version,'platform':platform.platform(),'machine':platform.machine(),
        'package_path':powerio.__file__,'powerio_version':powerio.__version__,
        'notes':'Native macOS ru_maxrss is bytes; RSS includes interpreter/imports. First query precedes calibration. Timing includes Python getattr and returned independent row copies. Filesystem caches uncontrolled.'}
Path(output).write_text(json.dumps(record,indent=2)+'\n')
