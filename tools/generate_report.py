#!/usr/bin/env python
"""
Generate benchmark report from pytest-benchmark JSON results.

Usage:
    python tools/generate_report.py results/triplets_benchmark.json
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


def generate_markdown_report(json_file):
    """Generate markdown report from benchmark JSON."""
    with open(json_file) as f:
        content = f.read()
    if not content.strip():
        return None
    data = json.loads(content)

    report = []
    report.append("# Benchmark Report\n")
    report.append(f"**Generated from**: `{json_file}`\n")

    # Machine info
    machine = data["machine_info"]
    report.append("## Environment\n")
    report.append(f"- **CPU**: {machine['cpu'].get('brand_raw', 'Unknown')}")
    report.append(f"- **Cores**: {machine['cpu']['count']}")
    report.append(f"- **Python**: {machine['python_version']}")
    report.append(f"- **System**: {machine['system']} {machine['release']}\n")

    # Benchmarks
    report.append("## Results\n")

    for bench in data["benchmarks"]:
        name = bench["name"].replace("test_", "").replace("_", " ").title()
        stats = bench["stats"]
        extra = bench.get("extra_info", {})

        report.append(f"### {name}\n")
        report.append(f"- **Mean time**: {format_time(stats['mean'])}")
        report.append(f"- **Min time**: {format_time(stats['min'])}")
        report.append(f"- **Max time**: {format_time(stats['max'])}")
        report.append(f"- **Std dev**: {format_time(stats['stddev'])}")
        report.append(f"- **Rounds**: {stats['rounds']}")

        if extra:
            report.append("\n**Metrics**:")
            for key, value in extra.items():
                key_display = key.replace("_", " ").title()
                report.append(f"- {key_display}: {value}")

        report.append("")

    return "\n".join(report)


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/generate_report.py <benchmark_json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    if not Path(json_file).exists():
        print(f"Error: File not found: {json_file}")
        sys.exit(1)

    report = generate_markdown_report(json_file)
    if report is None:
        print(f"Skipping empty JSON file: {json_file}")
        sys.exit(0)
    print(report)

    # Optionally save to file
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
        with open(output_file, "w") as f:
            f.write(report)
        print(f"\nReport saved to: {output_file}")


if __name__ == "__main__":
    main()
