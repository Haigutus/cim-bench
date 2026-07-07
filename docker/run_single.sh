#!/bin/bash

set -e

# Usage: ./docker/run_single.sh <tool> <dataset> [--rebuild]
# Example: ./docker/run_single.sh triplets svedala
#   --rebuild  Force rebuild of the base image (otherwise built only if missing)

if [ $# -lt 2 ]; then
    echo "Usage: $0 <tool> <dataset> [--rebuild]"
    echo "Example: $0 triplets svedala"
    echo ""
    echo "Available tools:"
    ls docker/tools/*.dockerfile 2>/dev/null | sed 's|docker/tools/||' | sed 's|.dockerfile||' | sed 's/^/  - /'
    echo ""
    echo "Available datasets: svedala, realgrid"
    exit 1
fi

TOOL=$1
DATASET=$2
REBUILD=false
[ "$3" = "--rebuild" ] && REBUILD=true

# Validate tool
TOOL_DOCKERFILE="docker/tools/${TOOL}.dockerfile"
if [ ! -f "$TOOL_DOCKERFILE" ]; then
    echo "Error: Tool '$TOOL' not found. No dockerfile at $TOOL_DOCKERFILE"
    exit 1
fi

# Validate dataset
if [ "$DATASET" != "svedala" ] && [ "$DATASET" != "realgrid" ]; then
    echo "Error: Dataset must be 'svedala' or 'realgrid'"
    exit 1
fi

# Create output directory
mkdir -p results-docker

echo "================================"
echo "Building and running: $TOOL / $DATASET"
echo "================================"

# Build base image (only if missing, unless --rebuild)
if [ "$REBUILD" = true ] || ! podman image exists cim-bench/base:latest; then
    echo ""
    echo "Building base image..."
    podman build -f docker/base.dockerfile -t cim-bench/base:latest .
else
    echo ""
    echo "Base image exists - skipping build (use --rebuild to force)"
fi

# Build tool image (fast when layer cache is warm)
echo ""
echo "Building $TOOL image..."
podman build -f "$TOOL_DOCKERFILE" -t "cim-bench/${TOOL}:latest" .

# Run benchmark
# Replace hyphens with underscores in tool name for file paths
TOOL_UNDERSCORE=$(echo "$TOOL" | tr '-' '_')

# Auto-detect benchmark file naming convention
# Some tools use docker_* prefix, others don't - check which exists
BENCHMARK_FILE="${TOOL_UNDERSCORE}_${DATASET}_benchmark.py"
DOCKER_BENCHMARK_FILE="docker_${TOOL_UNDERSCORE}_${DATASET}_benchmark.py"

if [ -f "benchmarks/$DOCKER_BENCHMARK_FILE" ]; then
    BENCHMARK_FILE="$DOCKER_BENCHMARK_FILE"
elif [ -f "benchmarks/$BENCHMARK_FILE" ]; then
    BENCHMARK_FILE="$BENCHMARK_FILE"
else
    echo "Error: No benchmark file found for $TOOL / $DATASET"
    echo "Tried:"
    echo "  - benchmarks/$BENCHMARK_FILE"
    echo "  - benchmarks/$DOCKER_BENCHMARK_FILE"
    exit 1
fi

OUTPUT_FILE="results-docker/${TOOL_UNDERSCORE}_${DATASET}_benchmark.json"

echo ""
echo "Running benchmark: $BENCHMARK_FILE"
echo "Output: $OUTPUT_FILE"
echo ""

# Source dirs mounted over the copies baked into the images, so code
# changes don't require image rebuilds (granular iteration)
podman run --rm \
    -v "$(pwd)/benchmarks:/benchmarks:ro,z" \
    -v "$(pwd)/parsers:/benchmarks/parsers:ro,z" \
    -v "$(pwd)/data:/benchmarks/data:ro,z" \
    -v "$(pwd)/temp:/benchmarks/temp:z" \
    -v "$(pwd)/results-docker:/output:z" \
    "cim-bench/${TOOL}:latest" \
    pytest "$BENCHMARK_FILE" --benchmark-only --benchmark-json="/output/${TOOL_UNDERSCORE}_${DATASET}_benchmark.json"

echo ""
echo "================================"
echo "Benchmark complete!"
echo "Results saved to: $OUTPUT_FILE"
echo "================================"

# Refresh reports, comparison and graphs with all existing results included
./docker/generate_outputs.sh results-docker
