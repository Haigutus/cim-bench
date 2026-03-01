#!/usr/bin/env bash
#
# Run all CIM-bench benchmarks and generate reports (Python-only)
#
# This script runs ONLY native Python benchmarks. Docker-only benchmarks
# (prefixed with docker_*) require JPype+JVM and must be run via:
#   ./docker/run_benchmark.sh
#
# Usage:
#   ./run_benchmarks.sh [--quick] [--skip-existing]
#
# Options:
#   --quick           Run minimal rounds for faster iteration
#   --skip-existing   Skip benchmarks if JSON results already exist
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

RESULTS_DIR="results"
BENCHMARK_OPTS=""
SKIP_EXISTING=false

# Parse arguments
for arg in "$@"; do
    case "$arg" in
        --quick)
            BENCHMARK_OPTS="--benchmark-min-rounds=3"
            echo "Running in quick mode (minimal rounds)"
            ;;
        --skip-existing)
            SKIP_EXISTING=true
            echo "Skip mode enabled (existing results will be reused)"
            ;;
    esac
done

# Create results directory
mkdir -p "$RESULTS_DIR"

echo "=================================="
echo "CIM-bench Benchmark Suite"
echo "=================================="
echo ""

# Auto-discover all benchmark files
echo "📊 Discovering benchmarks..."
BENCHMARK_FILES=(benchmarks/*_benchmark.py)
echo "Found ${#BENCHMARK_FILES[@]} benchmark files"
echo ""

# Run each benchmark
for test_file in "${BENCHMARK_FILES[@]}"; do
    # Skip if not a file
    [[ -f "$test_file" ]] || continue

    # Skip test_ prefixed files (unit tests, not benchmarks)
    basename="${test_file##*/}"
    [[ "$basename" == test_* ]] && continue

    # Skip docker_ prefixed files (Docker-only benchmarks requiring JPype+JVM)
    [[ "$basename" == docker_* ]] && continue

    # Extract basename for output file
    output_json="$RESULTS_DIR/${basename%.py}.json"

    # Skip if results already exist and --skip-existing flag is set
    if [[ "$SKIP_EXISTING" == true && -f "$output_json" ]]; then
        echo "⏭️  Skipping ${basename} (results exist)"
        continue
    fi

    echo "📊 Running ${basename}..."
    uv run pytest "$test_file" \
        --benchmark-only \
        --benchmark-json="$output_json" \
        $BENCHMARK_OPTS
    echo "✅ ${basename} complete"
    echo ""
done

# Generate markdown reports from all JSON files
echo "📝 Generating markdown reports..."
for json_file in "$RESULTS_DIR"/*_benchmark.json; do
    [[ -f "$json_file" ]] || continue

    # Skip test_ and docker_ prefixed files
    basename_json="$(basename "$json_file")"
    [[ "$basename_json" == test_* ]] && continue
    [[ "$basename_json" == docker_* ]] && continue

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
if uv run python -c "import matplotlib" 2>/dev/null; then
    uv run python tools/generate_graphs.py
else
    echo "⚠️  Matplotlib not installed - skipping graph generation"
    echo "   Install with: uv sync --extra visualization"
    echo ""
fi

echo "=================================="
echo "✅ All benchmarks complete!"
echo "=================================="
echo ""
echo "Results available in: $RESULTS_DIR/"
echo ""
echo "Reports:"
for report in "$RESULTS_DIR"/*_report.md; do
    [[ -f "$report" ]] || continue

    # Skip test_ and docker_ prefixed files
    basename_report="$(basename "$report")"
    [[ "$basename_report" == test_* ]] && continue
    [[ "$basename_report" == docker_* ]] && continue

    echo "  - $basename_report"
done
echo ""
