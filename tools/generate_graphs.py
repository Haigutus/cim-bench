#!/usr/bin/env python
"""Generate performance comparison graphs from benchmark results."""

import sys
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pathlib import Path

from benchmark_data import load_benchmarks, dataset_label

matplotlib.use('Agg')


def plot_dataset(dataset_name, tools_data, output_dir):
    """Generate comparison and detailed charts for a dataset."""
    for tool in sorted(tools_data):
        if "load" not in tools_data[tool]:
            print(f"   ⚠️  {tool}: no load benchmark - skipped in {dataset_name} charts")

    tools = sorted(t for t in tools_data if "load" in tools_data[t])
    if len(tools) < 2:
        return
    colors = [tools_data[t].get("color", "#999999") for t in tools]

    # Comparison chart
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    load_times = [tools_data[t]["load"]["time"] for t in tools]
    ax1.bar(tools, load_times, color=colors)
    ax1.set_ylabel('Load Time (seconds)', fontsize=11)
    ax1.set_title(f'{dataset_name} - Loading Performance', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    for i, v in enumerate(load_times):
        ax1.text(i, v, f'{v:.3f}s', ha='center', va='bottom', fontsize=9)

    memory = [tools_data[t]["load"]["memory"] for t in tools]
    ax2.bar(tools, memory, color=colors)
    ax2.set_ylabel('Memory (MB)', fontsize=11)
    ax2.set_title(f'{dataset_name} - Memory Consumption', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    for i, v in enumerate(memory):
        ax2.text(i, v, f'{v:.1f} MB', ha='center', va='bottom', fontsize=9)

    query_times = [np.mean(list(tools_data[t].get("queries", {}).values()) or [0]) for t in tools]
    ax3.bar(tools, query_times, color=colors)
    ax3.set_ylabel('Average Query Time (ms, log scale)', fontsize=11)
    ax3.set_title(f'{dataset_name} - Query Performance', fontsize=12, fontweight='bold')
    ax3.set_yscale('log')
    ax3.grid(axis='y', alpha=0.3, which='both')
    for i, v in enumerate(query_times):
        if v > 0:
            ax3.text(i, v, f'{v:.2f} ms', ha='center', va='bottom', fontsize=9)

    # Tilt tool names so they don't overlap
    for ax in fig.get_axes():
        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    plt.tight_layout()
    plt.savefig(output_dir / f"{dataset_name.lower()}_comparison.svg", format='svg', bbox_inches='tight')
    print(f"   → {dataset_name.lower()}_comparison.svg")

    # Detailed chart
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    ax1.bar(tools, load_times, color=colors)
    ax1.set_ylabel('Load Time (seconds)', fontsize=11)
    ax1.set_title('Loading Performance', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    for i, v in enumerate(load_times):
        ax1.text(i, v, f'{v:.3f}', ha='center', va='bottom', fontsize=9)

    ax2.bar(tools, memory, color=colors)
    ax2.set_ylabel('Memory (MB)', fontsize=11)
    ax2.set_title('Memory Consumption', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    for i, v in enumerate(memory):
        ax2.text(i, v, f'{v:.1f}', ha='center', va='bottom', fontsize=9)

    lines = [tools_data[t]["load"]["lines"] for t in tools]
    ax3.bar(tools, lines, color=colors)
    ax3.set_ylabel('Line Count', fontsize=11)
    ax3.set_title('Lines Parsed', fontsize=12, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    for i, v in enumerate(lines):
        ax3.text(i, v, f'{v:,}', ha='center', va='bottom', fontsize=9)

    generators = [tools_data[t]["load"]["generators"] for t in tools]
    ax4.bar(tools, generators, color=colors)
    ax4.set_ylabel('Generator Count', fontsize=11)
    ax4.set_title('Generators Parsed', fontsize=12, fontweight='bold')
    ax4.grid(axis='y', alpha=0.3)
    for i, v in enumerate(generators):
        ax4.text(i, v, f'{v:,}', ha='center', va='bottom', fontsize=9)

    # Tilt tool names so they don't overlap
    for ax in fig.get_axes():
        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    plt.suptitle(f'{dataset_name} Dataset - Detailed Comparison', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_dir / f"{dataset_name.lower()}_detailed.svg", format='svg', bbox_inches='tight')
    print(f"   → {dataset_name.lower()}_detailed.svg")


def plot_cross_dataset(data, dataset_sizes, output_dir):
    """Generate cross-dataset comparison charts with separate subplots per dataset."""
    # Sort datasets by size (smaller first)
    datasets = sorted(data.keys(), key=lambda ds: dataset_sizes.get(ds, 0))

    if len(datasets) < 2:
        return

    tools = sorted(set(t for ds in data.values() for t in ds.keys()))

    # Get colors from first available dataset
    colors = {}
    for t in tools:
        for ds in datasets:
            if t in data[ds]:
                colors[t] = data[ds][t].get("color", "#999999")
                break

    # Import comparison - separate subplots per dataset (independent y-axis scales)
    fig, axes = plt.subplots(len(datasets), 1, figsize=(12, 5 * len(datasets)), sharex=False)
    if len(datasets) == 1:
        axes = [axes]

    for idx, ds in enumerate(datasets):
        ax = axes[idx]
        ds_label = dataset_label(ds, dataset_sizes)

        entries = []
        for tool in tools:
            time = data[ds].get(tool, {}).get("load", {}).get("time", 0)
            if time > 0:
                entries.append((tool, time, colors.get(tool, "#999999")))

        entries.sort(key=lambda x: x[1])
        labels = [e[0] for e in entries]
        values = [e[1] for e in entries]
        bar_colors = [e[2] for e in entries]

        bars = ax.barh(labels, values, color=bar_colors)
        ax.set_xlabel('Import Time (seconds)', fontsize=12)
        ax.set_title(ds_label, fontsize=12, fontweight='bold')

        # Auto-scale x-axis independently per dataset
        if values:
            max_time_ds = max(values)
            ax.set_xlim(0, max_time_ds * 1.15)

        ax.grid(axis='x', alpha=0.3)

        for i, (bar, val) in enumerate(zip(bars, values)):
            ax.text(val, i, f' {val:.3f}s', va='center', fontsize=10)

    fig.suptitle('Import Performance Comparison', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_dir / "import_comparison.svg", format='svg', bbox_inches='tight')
    print("   → import_comparison.svg")
    plt.close()

    # Memory comparison - separate subplots per dataset (independent y-axis scales)
    fig, axes = plt.subplots(len(datasets), 1, figsize=(12, 5 * len(datasets)), sharex=False)
    if len(datasets) == 1:
        axes = [axes]

    for idx, ds in enumerate(datasets):
        ax = axes[idx]
        ds_label = dataset_label(ds, dataset_sizes)

        entries = []
        for tool in tools:
            memory = data[ds].get(tool, {}).get("load", {}).get("memory", 0)
            if memory > 0:
                entries.append((tool, memory, colors.get(tool, "#999999")))

        entries.sort(key=lambda x: x[1])
        labels = [e[0] for e in entries]
        values = [e[1] for e in entries]
        bar_colors = [e[2] for e in entries]

        bars = ax.barh(labels, values, color=bar_colors)
        ax.set_xlabel('Memory Usage (MB)', fontsize=12)
        ax.set_title(ds_label, fontsize=12, fontweight='bold')

        # Auto-scale x-axis independently per dataset
        if values:
            max_memory_ds = max(values)
            ax.set_xlim(0, max_memory_ds * 1.15)

        ax.grid(axis='x', alpha=0.3)

        for i, (bar, val) in enumerate(zip(bars, values)):
            ax.text(val, i, f' {val:.1f} MB', va='center', fontsize=10)

    fig.suptitle('Memory Consumption Comparison', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_dir / "memory_comparison.svg", format='svg', bbox_inches='tight')
    print("   → memory_comparison.svg")
    plt.close()

    # Query comparison - separate subplots per dataset (independent y-axis scales)
    fig, axes = plt.subplots(len(datasets), 1, figsize=(12, 5 * len(datasets)), sharex=False)
    if len(datasets) == 1:
        axes = [axes]

    for idx, ds in enumerate(datasets):
        ax = axes[idx]
        ds_label = dataset_label(ds, dataset_sizes)

        entries = []
        for tool in tools:
            query_time = np.mean(list(data[ds].get(tool, {}).get("queries", {}).values()) or [0])
            if query_time > 0:
                entries.append((tool, query_time, colors.get(tool, "#999999")))

        entries.sort(key=lambda x: x[1])
        labels = [e[0] for e in entries]
        values = [e[1] for e in entries]
        bar_colors = [e[2] for e in entries]

        bars = ax.barh(labels, values, color=bar_colors)
        ax.set_xlabel('Average Query Time (ms, log scale)', fontsize=12)
        ax.set_title(ds_label, fontsize=12, fontweight='bold')
        ax.set_xscale('log')
        ax.grid(axis='x', alpha=0.3, which='both')

        for i, (bar, val) in enumerate(zip(bars, values)):
            ax.text(val, i, f' {val:.3f} ms', va='center', fontsize=10)

    fig.suptitle('Query Performance Comparison', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_dir / "query_comparison.svg", format='svg', bbox_inches='tight')
    print("   → query_comparison.svg")
    plt.close()


def plot_cross_dataset_export(data, dataset_sizes, output_dir):
    """Generate export performance comparison chart with separate subplots per dataset."""
    datasets = sorted(data.keys(), key=lambda ds: dataset_sizes.get(ds, 0))

    # Only include tools that have export data
    tools_with_export = set()
    for ds in datasets:
        for tool, tool_data in data[ds].items():
            if "export" in tool_data:
                tools_with_export.add(tool)

    if not tools_with_export:
        return

    # Get colors
    colors = {}
    for t in tools_with_export:
        for ds in datasets:
            if t in data[ds] and "export" in data[ds][t]:
                colors[t] = data[ds][t].get("color", "#999999")
                break

    fig, axes = plt.subplots(len(datasets), 1, figsize=(12, 5 * len(datasets)), sharex=False)
    if len(datasets) == 1:
        axes = [axes]

    for idx, ds in enumerate(datasets):
        ax = axes[idx]
        ds_label = dataset_label(ds, dataset_sizes)

        entries = []
        for tool in tools_with_export:
            time = data[ds].get(tool, {}).get("export", {}).get("time", 0)
            if time > 0:
                entries.append((tool, time, colors.get(tool, "#999999")))

        entries.sort(key=lambda x: x[1])
        labels = [e[0] for e in entries]
        values = [e[1] for e in entries]
        bar_colors = [e[2] for e in entries]

        bars = ax.barh(labels, values, color=bar_colors)
        ax.set_xlabel('Export Time (seconds)', fontsize=12)
        ax.set_title(ds_label, fontsize=12, fontweight='bold')

        if values:
            ax.set_xlim(0, max(values) * 1.15)

        ax.grid(axis='x', alpha=0.3)

        for i, (bar, val) in enumerate(zip(bars, values)):
            label = f' {val*1000:.1f} ms' if val < 1 else f' {val:.3f}s'
            ax.text(val, i, label, va='center', fontsize=10)

    fig.suptitle('Export Performance Comparison', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_dir / "export_comparison.svg", format='svg', bbox_inches='tight')
    print("   → export_comparison.svg")
    plt.close()


def plot_cli(cli_data, dataset_sizes, output_dir):
    """
    Generate charts for CLI tools (separate family - subprocess measurements
    are not comparable with in-process libraries). One bar per tool+operation,
    one subplot per dataset; plots even with a single tool.
    """
    datasets = sorted(cli_data.keys(), key=lambda ds: dataset_sizes.get(ds, 0))

    charts = [
        ("time", "Time (seconds)", "cli_time_comparison.svg", "CLI Tools - Execution Time"),
        ("memory", "Peak RSS (MB)", "cli_memory_comparison.svg", "CLI Tools - Peak Memory"),
    ]

    for metric, xlabel, filename, title in charts:
        fig, axes = plt.subplots(len(datasets), 1, figsize=(12, 4 * len(datasets)), sharex=False)
        if len(datasets) == 1:
            axes = [axes]

        for idx, ds in enumerate(datasets):
            ax = axes[idx]

            entries = []
            for tool in sorted(cli_data[ds]):
                color = cli_data[ds][tool].get("color", "#999999")
                for operation, values in sorted(cli_data[ds][tool].get("operations", {}).items()):
                    if values[metric] > 0:
                        entries.append((f"{tool} ({operation})", values[metric], color))

            entries.sort(key=lambda x: x[1])
            labels = [e[0] for e in entries]
            values = [e[1] for e in entries]
            bar_colors = [e[2] for e in entries]

            ax.barh(labels, values, color=bar_colors)
            ax.set_xlabel(xlabel, fontsize=12)
            ax.set_title(dataset_label(ds, dataset_sizes), fontsize=12, fontweight='bold')
            if values:
                ax.set_xlim(0, max(values) * 1.15)
            ax.grid(axis='x', alpha=0.3)

            for i, val in enumerate(values):
                text = f' {val:.3f}s' if metric == "time" else f' {val:.1f} MB'
                ax.text(val, i, text, va='center', fontsize=10)

        fig.suptitle(title, fontsize=14, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(output_dir / filename, format='svg', bbox_inches='tight')
        print(f"   → {filename}")
        plt.close()


def main(results_dir=None):
    if results_dir is None:
        results_dir = Path("results")
    else:
        results_dir = Path(results_dir)

    graphs_dir = results_dir / "graphs"
    graphs_dir.mkdir(exist_ok=True)

    print("📊 Generating performance graphs...")

    data, cli_data, dataset_sizes, _meta = load_benchmarks(results_dir)

    for dataset, tools_data in sorted(data.items()):
        print(f"   {dataset.capitalize()} dataset:")
        plot_dataset(dataset.capitalize(), tools_data, graphs_dir)

    if len(data) >= 2:
        print("   Cross-dataset comparisons:")
        plot_cross_dataset(data, dataset_sizes, graphs_dir)

    # Generate export comparison if any export data exists
    has_export = any("export" in td for ds in data.values() for td in ds.values())
    if has_export:
        print("   Export comparisons:")
        plot_cross_dataset_export(data, dataset_sizes, graphs_dir)

    if cli_data:
        print("   CLI tools (separate family):")
        plot_cli(cli_data, dataset_sizes, graphs_dir)

    print(f"\n✅ Graph generation complete!\n   Location: {graphs_dir}/")


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
