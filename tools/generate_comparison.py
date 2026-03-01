#!/usr/bin/env python
"""
Generate comparison report from multiple benchmark JSON results.

Usage:
    python tools/generate_comparison.py file1.json file2.json [file3.json ...] output.md
"""

import json
import sys
from pathlib import Path


def format_time(seconds):
    """Format time in appropriate unit."""
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.1f} μs"
    elif seconds < 1:
        return f"{seconds * 1000:.1f} ms"
    else:
        return f"{seconds:.2f} s"


def get_library_name(benchmark_data, json_file):
    """Extract library name and dataset from benchmark data."""
    # Read from extra_info in JSON (preferred method)
    if benchmark_data["benchmarks"]:
        first_bench = benchmark_data["benchmarks"][0]
        extra_info = first_bench.get("extra_info", {})

        if "library" in extra_info and "dataset" in extra_info:
            library = extra_info["library"]
            dataset = extra_info["dataset"].capitalize()
            return f"{library} ({dataset})"

    # Fallback: Extract from filename
    filename = Path(json_file).stem.replace("_benchmark", "")
    parts = filename.split("_")

    if len(parts) >= 2:
        library = parts[0]
        dataset = parts[1].capitalize()
        return f"{library} ({dataset})"

    return "Unknown"


def extract_load_benchmark(benchmarks):
    """Find the main load/import benchmark."""
    for bench in benchmarks:
        name = bench["name"].lower()
        if "load_full" in name or "load_network" in name:
            return bench
    return benchmarks[0] if benchmarks else None


def generate_comparison_report(json_files):
    """Generate markdown comparison report."""
    report = []
    report.append("# Benchmark Comparison Report\n")

    # Load all benchmark data
    benchmark_data = []
    for json_file in json_files:
        try:
            with open(json_file) as f:
                data = json.load(f)
                if not data or "benchmarks" not in data or not data["benchmarks"]:
                    print(f"⚠️  Skipping {json_file}: empty or missing benchmarks")
                    continue
                lib_name = get_library_name(data, json_file)
                benchmark_data.append((lib_name, data))
        except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
            print(f"⚠️  Skipping {json_file}: {e}")
            continue

    # Environment (use first one)
    machine = benchmark_data[0][1]["machine_info"]
    report.append("## Environment\n")
    report.append(f"- **CPU**: {machine['cpu'].get('brand_raw', 'Unknown')}")
    report.append(f"- **Cores**: {machine['cpu']['count']}")
    report.append(f"- **Python**: {machine['python_version']}")
    report.append(f"- **System**: {machine['system']} {machine['release']}\n")

    # Comparison table
    report.append("## Performance Comparison\n")
    report.append("### Load Performance\n")
    report.append("| Library | Load Time (mean) | Memory (MB) | Elements | Notes |")
    report.append("|---------|------------------|-------------|----------|-------|")

    for lib_name, data in benchmark_data:
        load_bench = extract_load_benchmark(data["benchmarks"])
        if load_bench:
            mean_time = format_time(load_bench["stats"]["mean"])
            extra = load_bench.get("extra_info", {})

            memory = extra.get("memory_mb", "N/A")
            if isinstance(memory, str) and memory != "N/A":
                memory = f"{memory} MB"

            # Extract element counts
            elements = []
            if "lines" in extra:
                elements.append(f"{extra['lines']} lines")
            if "generators" in extra:
                elements.append(f"{extra['generators']} gen")
            if "loads" in extra:
                elements.append(f"{extra['loads']} loads")
            if "substations" in extra:
                elements.append(f"{extra['substations']} subs")
            elements_str = ", ".join(elements) if elements else "N/A"

            notes = ""
            # Prefer dataset_size_mb (for zipped datasets) over total_size_mb
            if "dataset_size_mb" in extra:
                notes = f"Dataset: {extra['dataset_size_mb']} MB"
            elif "total_size_mb" in extra:
                notes = f"Dataset: {extra['total_size_mb']} MB"

            report.append(f"| {lib_name} | {mean_time} | {memory} | {elements_str} | {notes} |")

    report.append("")

    # Query performance comparison
    report.append("### Query Performance\n")

    # Find query benchmarks
    query_benchmarks = {}
    for lib_name, data in benchmark_data:
        queries = {}
        for bench in data["benchmarks"]:
            name = bench["name"].lower()
            if "query" in name or "get_" in name:
                query_type = bench.get("extra_info", {}).get("query_type", bench["name"])
                queries[query_type] = format_time(bench["stats"]["mean"])
        if queries:
            query_benchmarks[lib_name] = queries

    if query_benchmarks:
        # Get all unique query types
        all_query_types = set()
        for queries in query_benchmarks.values():
            all_query_types.update(queries.keys())

        report.append("| Query Type | " + " | ".join(query_benchmarks.keys()) + " |")
        report.append("|------------|" + "|".join(["---" for _ in query_benchmarks]) + "|")

        for query_type in sorted(all_query_types):
            row = [query_type]
            for lib_name in query_benchmarks.keys():
                row.append(query_benchmarks[lib_name].get(query_type, "N/A"))
            report.append("| " + " | ".join(row) + " |")

        report.append("")

    # Detailed results
    report.append("## Detailed Results\n")

    for lib_name, data in benchmark_data:
        report.append(f"### {lib_name}\n")

        for bench in data["benchmarks"]:
            name = bench["name"].replace("test_", "").replace("_", " ").title()
            stats = bench["stats"]

            report.append(f"#### {name}\n")
            report.append(f"- **Mean**: {format_time(stats['mean'])}")
            report.append(f"- **Min**: {format_time(stats['min'])}")
            report.append(f"- **Max**: {format_time(stats['max'])}")
            report.append(f"- **Rounds**: {stats['rounds']}\n")

    return "\n".join(report)


def main():
    if len(sys.argv) < 3:
        print("Usage: python tools/generate_comparison.py <benchmark1.json> <benchmark2.json> [...] <output.md>")
        sys.exit(1)

    json_files = sys.argv[1:-1]
    output_file = sys.argv[-1]

    # Validate input files
    for json_file in json_files:
        if not Path(json_file).exists():
            print(f"Error: File not found: {json_file}")
            sys.exit(1)

    report = generate_comparison_report(json_files)

    # Save to file
    with open(output_file, "w") as f:
        f.write(report)

    print(f"Comparison report saved to: {output_file}")


if __name__ == "__main__":
    main()
