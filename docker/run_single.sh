#!/bin/bash

set -e

# Usage: ./docker/run_single.sh <tool> <dataset>
# Example: ./docker/run_single.sh triplets svedala

if [ $# -ne 2 ]; then
    echo "Usage: $0 <tool> <dataset>"
    echo "Example: $0 triplets svedala"
    echo ""
    echo "Available tools: triplets, pypowsybl, veragrid, cimgraph, rdflib, jena, opencgmes, powsybl-cgmes"
    echo "Available datasets: svedala, realgrid"
    exit 1
fi

TOOL=$1
DATASET=$2

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

# Build base image
echo ""
echo "Building base image..."
podman build -f docker/base.dockerfile -t cim-bench/base:latest .

# Build tool image
echo ""
echo "Building $TOOL image..."
podman build -f "$TOOL_DOCKERFILE" -t "cim-bench/${TOOL}:latest" .

# Run benchmark
BENCHMARK_FILE="${TOOL}_${DATASET}_benchmark.py"
OUTPUT_FILE="results-docker/${TOOL}_${DATASET}_benchmark.json"

echo ""
echo "Running benchmark: $BENCHMARK_FILE"
echo "Output: $OUTPUT_FILE"
echo ""

podman run --rm \
    -v "$(pwd)/data:/benchmarks/data:ro,z" \
    -v "$(pwd)/results-docker:/output:z" \
    "cim-bench/${TOOL}:latest" \
    pytest "$BENCHMARK_FILE" --benchmark-only --benchmark-json="/output/${TOOL}_${DATASET}_benchmark.json"

echo ""
echo "================================"
echo "Benchmark complete!"
echo "Results saved to: $OUTPUT_FILE"
echo "================================"
