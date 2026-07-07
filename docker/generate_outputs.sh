#!/usr/bin/env bash
set -e

# Regenerate reports, comparison summary and graphs from all benchmark JSONs.
# Usage: ./docker/generate_outputs.sh [results-dir]   (default: results-docker)

cd "$(dirname "$0")/.."

RESULTS_DIR="${1:-results-docker}"

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
    uv run python tools/generate_graphs.py "$RESULTS_DIR"
    echo "   → Graphs saved to $RESULTS_DIR/graphs/"
else
    echo "⚠️  Matplotlib not installed - skipping graph generation"
    echo "   Install with: uv sync --extra visualization"
fi
echo ""

# Generate the results site (published via GitHub Pages from docs/)
echo "🌐 Generating results site..."
uv run python tools/generate_site.py "$RESULTS_DIR" docs
echo ""
