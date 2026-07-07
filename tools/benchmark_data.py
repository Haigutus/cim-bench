"""Shared loader for benchmark result JSONs.

Organizes pytest-benchmark output for the graph and site generators.
Library and CLI tools are separate families (extra_info["tool_type"] ==
"cli" marks CLI records; absence means library) - their measurements are
not comparable.
"""

import json
from collections import defaultdict
from pathlib import Path


def load_benchmarks(results_dir):
    """
    Load all benchmark JSONs and organize by dataset.

    Returns:
        (data, cli_data, dataset_sizes, meta):
            data[dataset][tool] = {
                "color", "tags", "version", "dependencies",
                "load": {"time", "memory", "lines", "generators", "loads", "substations"},
                "queries": {query_type: ms},
                "export": {"time"},
            }
            cli_data[dataset][tool] = {
                "color", "tags", "version", "binary",
                "operations": {operation: {"time", "memory"}},
            }
            dataset_sizes[dataset] = size in MB (from extra_info dataset_size_mb)
            meta = {"machine_info": ..., "datetime": ...} from the newest JSON
    """
    data = defaultdict(lambda: defaultdict(dict))
    cli_data = defaultdict(lambda: defaultdict(dict))
    dataset_sizes = {}
    meta = {}

    for json_file in sorted(Path(results_dir).glob("*_benchmark.json")):
        try:
            parsed = json.loads(json_file.read_text())
            if not parsed or "benchmarks" not in parsed:
                print(f"⚠️  Skipping {json_file.name}: missing benchmarks")
                continue
        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️  Skipping {json_file.name}: {e}")
            continue

        if parsed.get("datetime", "") > meta.get("datetime", ""):
            meta = {"machine_info": parsed.get("machine_info", {}), "datetime": parsed.get("datetime", "")}

        for bench in parsed["benchmarks"]:
            extra = bench.get("extra_info", {})
            if "dataset" not in extra or "display_name" not in extra:
                continue

            dataset = extra["dataset"]
            tool = extra["display_name"]
            mean = bench["stats"]["mean"]

            if "dataset_size_mb" in extra:
                dataset_sizes[dataset] = float(extra["dataset_size_mb"])

            if extra.get("tool_type") == "cli":
                entry = cli_data[dataset][tool]
                entry["color"] = extra.get("color", "#999999")
                entry["tags"] = extra.get("tags", ["cli"])
                entry.setdefault("version", extra.get("library_version"))
                entry.setdefault("binary", extra.get("binary"))
                entry.setdefault("operations", {})[extra.get("operation", bench["name"])] = {
                    "time": mean,
                    "memory": float(extra.get("memory_mb", 0)),
                }
                continue

            entry = data[dataset][tool]
            entry.setdefault("color", extra.get("color", "#999999"))
            entry.setdefault("tags", extra.get("tags") or ["parser"])

            if extra.get("operation") == "export":
                entry["export"] = {"time": mean}
            elif "load" in bench["name"].lower() and "get_" not in bench["name"].lower():
                entry["color"] = extra.get("color", "#999999")
                entry["tags"] = extra.get("tags") or ["parser"]
                entry["version"] = extra.get("library_version")
                entry["dependencies"] = extra.get("library_dependencies") or {}
                entry["load"] = {
                    "time": mean,
                    "memory": float(extra.get("memory_mb", 0)),
                    "lines": int(extra.get("lines", 0)),
                    "generators": int(extra.get("generators", 0)),
                    "loads": int(extra.get("loads", 0)),
                    "substations": int(extra.get("substations", 0)),
                }
            elif "get_" in bench["name"].lower():
                entry.setdefault("queries", {})[extra.get("query_type", bench["name"])] = mean * 1000

    return data, cli_data, dataset_sizes, meta


def dataset_label(dataset, dataset_sizes):
    """Human label for a dataset, with size when known."""
    if dataset in dataset_sizes:
        return f"{dataset.capitalize()} ({dataset_sizes[dataset]:g} MB)"
    return dataset.capitalize()


def format_time(seconds):
    """Format seconds in an appropriate unit."""
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.1f} μs"
    elif seconds < 1:
        return f"{seconds * 1000:.1f} ms"
    return f"{seconds:.2f} s"
