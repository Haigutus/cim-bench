#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

echo "========================================"
echo "Building cim-bench Docker images"
echo "========================================"

# Build base image (hardcoded)
echo ""
echo "[1/N] Building base image..."
podman build -f docker/base.dockerfile -t cim-bench/base:latest .

# Extract unique tool names from docker-compose.yml
echo ""
echo "Discovering tools from docker-compose.yml..."
TOOL_NAMES=$(podman-compose -f docker/docker-compose.yml config | \
    grep 'image:' | \
    awk '{print $2}' | \
    grep 'cim-bench/' | \
    grep -v 'cim-bench/base' | \
    sed 's|cim-bench/||' | \
    sed 's|:.*||' | \
    sort -u)

# Count unique tools
TOTAL_TOOLS=$(echo "$TOOL_NAMES" | wc -l)
echo "Found $TOTAL_TOOLS unique tools: $(echo $TOOL_NAMES | tr '\n' ' ')"

CURRENT=1

# Build each tool image
for tool in $TOOL_NAMES; do
    CURRENT=$((CURRENT + 1))
    echo ""
    echo "[$CURRENT/$((TOTAL_TOOLS + 1))] Building $tool image..."
    podman build -f "docker/tools/${tool}.dockerfile" -t "cim-bench/${tool}:latest" .
done

echo ""
echo "========================================"
echo "✓ All images built successfully"
echo "========================================"
echo ""
podman images | grep "cim-bench"
