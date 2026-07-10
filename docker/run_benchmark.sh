#!/usr/bin/env bash
set -e

# Run containerized benchmarks sequentially (parallel execution is not
# supported - concurrent tools would skew each other's measurements).
#
# Usage: ./docker/run_benchmark.sh [--tools t1,t2] [--skip-existing] [--quick]
#   --tools t1,t2     Run only the listed tools (compose service prefixes,
#                     e.g. triplets,powsybl-cgmes)
#   --skip-existing   Skip benchmarks whose JSON already exists in results-docker/

cd "$(dirname "$0")/.."

RESULTS_DIR="results-docker"
QUICK_MODE=false
SKIP_EXISTING=false
TOOLS=""
FAILED_SERVICES=()

while [ $# -gt 0 ]; do
    case "$1" in
        --quick) QUICK_MODE=true ;;
        --skip-existing) SKIP_EXISTING=true ;;
        --tools) TOOLS="$2"; shift ;;
        --tools=*) TOOLS="${1#--tools=}" ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
    shift
done

mkdir -p "$RESULTS_DIR"

echo "========================================"
echo "cim-bench Containerized Benchmarks"
echo "Tools: ${TOOLS:-all}"
echo "Skip existing: $SKIP_EXISTING"
echo "========================================"
echo ""

if [ "$QUICK_MODE" = true ]; then
    echo "⚠️  Quick mode not yet supported via podman-compose"
    echo "    Use native execution: ./run_benchmarks.sh --quick"
    echo ""
fi

echo "Running benchmarks sequentially using podman-compose..."
echo ""

# Get all service names from docker-compose.yml (named {tool}-{dataset})
services=$(podman-compose -f docker/docker-compose.yml config --services)

for service in $services; do
    tool="${service%-svedala}"
    tool="${tool%-realgrid}"
    dataset="${service##*-}"

    if [ -n "$TOOLS" ] && ! echo ",$TOOLS," | grep -q ",$tool,"; then
        continue
    fi

    json_file="$RESULTS_DIR/$(echo "$tool" | tr '-' '_')_${dataset}_benchmark.json"
    if [ "$SKIP_EXISTING" = true ] && [ -f "$json_file" ]; then
        echo "⏭  Skipping $service (found $(basename "$json_file"))"
        continue
    fi

    echo "Running $service..."
    # A failing tool must not abort the rest of the sequential suite
    if podman-compose -f docker/docker-compose.yml run --rm "$service"; then
        echo "✓ $service complete"
    else
        echo "✗ $service FAILED - continuing with remaining benchmarks"
        FAILED_SERVICES+=("$service")
    fi
    echo ""
done

if [ ${#FAILED_SERVICES[@]} -gt 0 ]; then
    echo "⚠️  Failed benchmarks: ${FAILED_SERVICES[*]}"
    echo ""
fi

./docker/generate_outputs.sh "$RESULTS_DIR"

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
