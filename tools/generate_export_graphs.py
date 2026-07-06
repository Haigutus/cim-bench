#!/usr/bin/env python
"""Generate export performance comparison graphs in the same style as import graphs."""

import json
import sys
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pathlib import Path
from collections import defaultdict

matplotlib.use('Agg')


def load_export_benchmarks(results_dir):
    """Load export benchmark results and organize by dataset."""
    results_dir = Path(results_dir)
    data = defaultdict(lambda: defaultdict(dict))

    # Load the main export benchmarks file
    export_json = results_dir / "export_benchmarks.json"
    if not export_json.exists():
        return data

    json_files = [export_json]

    for json_file in json_files:
        try:
            with open(json_file) as f:
                content = json.load(f)
                if not content or "benchmarks" not in content:
                    print(f"⚠️  Skipping {json_file.name}: empty or missing benchmarks")
                    continue
                benchmarks = content["benchmarks"]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️  Skipping {json_file.name}: {e}")
            continue

        for bench in benchmarks:
            extra = bench.get("extra_info", {})
            if "dataset" not in extra or "display_name" not in extra:
                continue

            dataset = extra["dataset"]
            tool = extra["display_name"]

            # Store export data
            data[dataset][tool]["export"] = {
                "time": bench["stats"]["mean"],
                "color": extra.get("color", "#999999")
            }

    return data


def plot_export_comparison(data, output_dir):
    """Generate export performance comparison in the same style as import graphs."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    # Sort datasets by size (smaller first) - same as import graphs
    dataset_sizes = {'svedala': 7.3, 'realgrid': 86.5}
    datasets = sorted(data.keys(), key=lambda ds: dataset_sizes.get(ds, 0))

    if not datasets:
        print("⚠️  No export data found")
        return

    tools = sorted(set(t for ds in data.values() for t in ds.keys()))

    # Get colors from data
    colors = {}
    for t in tools:
        for ds in datasets:
            if t in data[ds]:
                colors[t] = data[ds][t].get("export", {}).get("color", "#999999")
                break

    # Export comparison - separate subplots per dataset (like import graphs)
    fig, axes = plt.subplots(len(datasets), 1, figsize=(12, 5 * len(datasets)), sharex=False)
    if len(datasets) == 1:
        axes = [axes]

    for idx, ds in enumerate(datasets):
        ax = axes[idx]
        ds_label = f"{ds.capitalize()} (7.3 MB)" if ds == 'svedala' else f"{ds.capitalize()} (86.5 MB)"

        entries = []
        for tool in tools:
            time = data[ds].get(tool, {}).get("export", {}).get("time", 0)
            if time > 0:
                entries.append((tool, time, colors.get(tool, "#999999")))

        # Sort by time (fastest first)
        entries.sort(key=lambda x: x[1])
        labels = [e[0] for e in entries]
        values = [e[1] for e in entries]
        bar_colors = [e[2] for e in entries]

        bars = ax.barh(labels, values, color=bar_colors)

        # Use linear scale for all datasets
        ax.set_xlabel('Export Time (seconds)', fontsize=12)
        # Auto-scale x-axis independently per dataset
        if values:
            max_time_ds = max(values)
            ax.set_xlim(0, max_time_ds * 1.15)
        ax.grid(axis='x', alpha=0.3)

        ax.set_title(ds_label, fontsize=12, fontweight='bold')

        # Add value labels on bars
        for i, (bar, val) in enumerate(zip(bars, values)):
            if val < 1:
                label = f' {val*1000:.1f} ms'
            else:
                label = f' {val:.3f}s'
            ax.text(val, i, label, va='center', fontsize=10)

    fig.suptitle('Export Performance Comparison', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    output_path = output_dir / 'export_comparison.svg'
    plt.savefig(output_path, format='svg', bbox_inches='tight')
    print(f"   → {output_path.name}")
    plt.close()


def main(results_dir=None):
    """Generate export performance graphs."""
    if results_dir is None:
        results_dir = Path("results")
    else:
        results_dir = Path(results_dir)

    graphs_dir = results_dir / "graphs"
    graphs_dir.mkdir(exist_ok=True)

    print("📊 Generating export performance graphs...")

    # Load export benchmarks
    data = load_export_benchmarks(results_dir)

    if not data:
        print("❌ No export benchmark data found")
        print("   Run: uv run pytest benchmarks/*_export_benchmark.py --benchmark-only --benchmark-json=results/export_benchmarks.json")
        return

    # Generate export comparison graph
    print("   Export comparisons:")
    plot_export_comparison(data, graphs_dir)

    print(f"\n✅ Export graph generation complete!")
    print(f"   Location: {graphs_dir}/")


if __name__ == "__main__":
    try:
        import matplotlib
    except ImportError:
        print("❌ Error: matplotlib not installed")
        print("   Install with: uv sync --extra visualization")
        sys.exit(1)

    # Accept optional results directory as command line argument
    results_dir = sys.argv[1] if len(sys.argv) > 1 else None
    main(results_dir)
