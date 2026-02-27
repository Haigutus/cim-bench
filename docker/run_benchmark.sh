#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

RESULTS_DIR="results-docker"
QUICK_MODE=false
PARALLEL=false

for arg in "$@"; do
    case "$arg" in
        --quick) QUICK_MODE=true ;;
        --parallel) PARALLEL=true ;;
    esac
done

mkdir -p "$RESULTS_DIR"

echo "========================================"
echo "cim-bench Containerized Benchmarks"
echo "Quick mode: $QUICK_MODE"
echo "Parallel: $PARALLEL"
echo "========================================"
echo ""

if [ "$QUICK_MODE" = true ]; then
    echo "⚠️  Quick mode not yet supported via docker-compose"
    echo "    Use native execution: ./run_benchmarks.sh --quick"
    echo ""
fi

if [ "$QUICK_MODE" = true ]; then
    echo "⚠️  Quick mode not yet supported via podman-compose"
    echo "    Use native execution: ./run_benchmarks.sh --quick"
    echo ""
fi

if [ "$PARALLEL" = true ]; then
    echo "Running all benchmarks in parallel using podman-compose..."
    echo ""
    podman-compose -f docker/docker-compose.yml up
else
    echo "Running benchmarks sequentially using podman-compose..."
    echo ""
    # Get all service names from docker-compose.yml
    services=$(podman-compose -f docker/docker-compose.yml config --services)

    for service in $services; do
        echo "Running $service..."
        podman-compose -f docker/docker-compose.yml run --rm "$service"
        echo "✓ $service complete"
        echo ""
    done
fi

echo ""
echo "========================================"
echo "Generating reports and visualizations..."
echo "========================================"
echo ""

# Generate markdown reports from all JSON files
echo "📝 Generating markdown reports..."
for json_file in "$RESULTS_DIR"/*_benchmark.json; do
    [[ -f "$json_file" ]] || continue

    report_file="${json_file%.json}_report.md"
    uv run python tools/generate_report.py "$json_file" "$report_file"
    echo "   → $(basename "$report_file")"
done
echo ""

# Generate comparison summary
BENCHMARK_JSONS=("$RESULTS_DIR"/*_benchmark.json)
if [ ${#BENCHMARK_JSONS[@]} -gt 1 ]; then
    echo "📊 Generating comparison summary..."
    uv run python tools/generate_comparison.py "${BENCHMARK_JSONS[@]}" "$RESULTS_DIR/comparison_summary.md"
    echo "   → comparison_summary.md"
    echo ""
fi

# Generate visualizations (if matplotlib available)
echo "📈 Generating graphs..."
if uv run python -c "import matplotlib" 2>/dev/null; then
    # Pass results directory to generate_graphs.py
    uv run python tools/generate_graphs.py "$RESULTS_DIR"
    echo "   → Graphs saved to $RESULTS_DIR/graphs/"
else
    echo "⚠️  Matplotlib not installed - skipping graph generation"
    echo "   Install with: uv sync --extra visualization"
fi
echo ""

echo "========================================"
echo "✓ All benchmarks complete!"
echo "========================================"
echo ""
echo "Results available in: $RESULTS_DIR/"
echo ""
echo "Reports:"
for report in "$RESULTS_DIR"/*_report.md; do
    [[ -f "$report" ]] || continue
    echo "  - $(basename "$report")"
done

if [ -d "$RESULTS_DIR/graphs" ]; then
    echo ""
    echo "Graphs:"
    for graph in "$RESULTS_DIR/graphs"/*.svg; do
        [[ -f "$graph" ]] || continue
        echo "  - $(basename "$graph")"
    done
fi
echo ""
