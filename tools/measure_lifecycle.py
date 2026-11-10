"""Measure one fresh library load and its first/warm queries in a fresh process.

Run this command separately for every independent sample. It never calls load
metrics before the first query. Each invocation performs one load only. Select
a single query to isolate its deferred work, or `all` to measure the documented
ordered load-to-use sequence. This complements, rather than replaces, pytest's
calibrated benchmarks and does not establish equivalent cross-tool semantics.
"""

import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

ADAPTERS = {
    "powerio": "PowerIOAdapter", "cimoxide": "CimoxideAdapter",
    "veragrid": "VeragridAdapter", "triplets": "TripletsAdapter",
    "maplib": "MaplibAdapter", "rdflib": "RDFlibAdapter",
    "pypowsybl": "PypowsyblAdapter", "libcimpp": "LibCIMppAdapter",
    "powsybl_cgmes": "PowsyblCgmesAdapter", "opencgmes": "OpenCGMESAdapter",
    "jena": "JenaAdapter", "graphdb": "GraphDBAdapter",
    "gmss": "GmssAdapter", "cimgraph": "CIMGraphAdapter",
}
QUERIES = ("lines", "generators", "loads", "substations")
ROOT = Path(__file__).resolve().parents[1]


def timed_batch(function, loaded, iterations):
    start = time.perf_counter_ns()
    result = None
    for _ in range(iterations):
        result = function(loaded)
    return time.perf_counter_ns() - start, result


def warm_query(function, loaded, expected, rounds, target_ns):
    iterations = 1
    calibration = []
    while True:
        elapsed, result = timed_batch(function, loaded, iterations)
        if result != expected:
            raise ValueError(f"query changed from {expected!r} to {result!r}")
        calibration.append({"iterations": iterations, "elapsed_ns": elapsed})
        if elapsed >= target_ns or iterations >= 1_048_576:
            break
        iterations *= 2
    samples = []
    for _ in range(rounds):
        elapsed, result = timed_batch(function, loaded, iterations)
        if result != expected:
            raise ValueError(f"query changed from {expected!r} to {result!r}")
        samples.append(elapsed)
    return {"iterations_per_batch": iterations, "batch_elapsed_ns": samples,
            "calibration": calibration, "timer_and_python_loop_overhead_subtracted": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tool", choices=ADAPTERS)
    parser.add_argument("dataset", choices=("svedala_igm_cgmes_3", "realgrid_cgmes_2_4"))
    parser.add_argument("output", type=Path)
    parser.add_argument("--query", choices=(*QUERIES, "all"), default="all")
    parser.add_argument("--warm-rounds", type=int, default=9)
    parser.add_argument("--warm-target-ms", type=float, default=5)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output already exists; preserve previous attempts")
    if args.warm_rounds < 1 or args.warm_target_ms <= 0:
        parser.error("warm rounds and target must be positive")
    sys.path.insert(0, str(ROOT / "parsers"))
    import psutil
    process = psutil.Process()
    rss_factor = 1 if sys.platform == "darwin" else 1024

    def memory():
        return {"rss_bytes": process.memory_info().rss,
                "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * rss_factor,
                "children": len(process.children(recursive=True))}

    record = {"schema": "cim-bench-lifecycle", "schema_version": 1,
              "tool": args.tool, "dataset": args.dataset, "query_selection": args.query,
              "query_order": list(QUERIES) if args.query == "all" else [args.query],
              "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "pid": os.getpid(), "python": sys.version, "platform": platform.platform(),
              "clock": vars(time.get_clock_info("perf_counter")),
              "declared_build": {key: os.environ.get(key) for key in
                                 ("CIM_BENCH_RUN_ID", "CIM_BENCH_COMMIT", "CIM_BENCH_IMAGE_ID", "CIM_BENCH_TOOL_COMMIT")},
              "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "memory_scope": "OS process RSS/high-water mark; excludes child-process memory; includes interpreter and imports",
              "load_to_use_scope": "adapter.load plus first selected query calls; excludes instrumentation between calls",
              "first_query_scope": ("one call including timer and invocation overhead; no prior load metrics; "
                                    "earlier selected queries can initialize later ones in all mode"),
              "os_file_cache": "uncontrolled warm host cache; fresh process is not cold disk",
              "cross_tool_semantics": "unverified; returned counts and adapter semantics require separate audit",
              "memory_before_import": memory(), "queries": {}, "status": "started"}
    adapter = None
    try:
        start = time.perf_counter_ns()
        module = importlib.import_module(args.tool + "_adapter")
        adapter = getattr(module, ADAPTERS[args.tool])()
        record["import_and_adapter_ns"] = time.perf_counter_ns() - start
        record["memory_before_load"] = memory()
        # Bind methods before loading so this metadata lookup cannot trigger
        # deferred work on the returned model or enter first-query timing.
        methods = {query: getattr(adapter, f"get_{query}_count") for query in record["query_order"]}
        start = time.perf_counter_ns()
        loaded = adapter.load(args.dataset)
        record["load_ns"] = time.perf_counter_ns() - start
        record["memory_after_load"] = memory()
        for query, function in methods.items():
            start = time.perf_counter_ns()
            count = function(loaded)
            elapsed = time.perf_counter_ns() - start
            record["queries"][query] = {"count": count, "first_ns": elapsed,
                                        "memory_after_first": memory()}
        record["load_to_use_ns"] = record["load_ns"] + sum(q["first_ns"] for q in record["queries"].values())
        record["import_to_use_ns"] = record["import_and_adapter_ns"] + record["load_to_use_ns"]
        for query, function in methods.items():
            record["queries"][query]["warm"] = warm_query(
                function, loaded, record["queries"][query]["count"],
                args.warm_rounds, int(args.warm_target_ms * 1_000_000))
        record["memory_after_warm"] = memory()
        record["tool_version"] = adapter.get_version()
        record["measurement_notes"] = adapter.get_measurement_notes()
        record["adapter_sha256"] = hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
        record["status"] = "success"
    except Exception as error:
        record["status"] = "failed"
        record["error"] = {"type": type(error).__name__, "message": str(error)}
    finally:
        if adapter is not None and hasattr(adapter, "cleanup"):
            try:
                adapter.cleanup()
            except Exception as error:
                record["cleanup_error"] = {"type": type(error).__name__, "message": str(error)}
                record["status"] = "failed"
        from datasets import DATASETS
        record["inputs"] = []
        for role, path in DATASETS[args.dataset].items():
            if role.startswith("_"):
                continue
            path = Path(path)
            item = {"role": role, "name": path.name, "present": path.is_file()}
            if path.is_file():
                with path.open("rb") as stream:
                    item.update(bytes=path.stat().st_size,
                                sha256=hashlib.file_digest(stream, "sha256").hexdigest())
            record["inputs"].append(item)
        record["observed_harness_commit"] = None
        record["observed_harness_dirty"] = None
        try:
            git = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True)
            record["observed_harness_commit"] = git.stdout.strip() if git.returncode == 0 else None
            dirty = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"], capture_output=True, text=True)
            record["observed_harness_dirty"] = bool(dirty.stdout.strip()) if dirty.returncode == 0 else None
        except OSError as error:
            # Minimal tool images need not install Git. Missing provenance
            # tooling must not discard either a measurement or a failed load.
            record["harness_observation_error"] = {"type": type(error).__name__, "message": str(error)}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x") as output:
            json.dump(record, output, indent=2)
            output.write("\n")
    return 0 if record["status"] == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
