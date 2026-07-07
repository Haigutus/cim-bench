#!/usr/bin/env bash
set -e

# Build benchmark images.
# Usage: ./docker/setup.sh [--rebuild] [tool ...]
#   No args: build base + all tools discovered from docker-compose.yml
#   tool ...: build base (only if missing) + just the named tools
#   --rebuild: force base image rebuild

cd "$(dirname "$0")/.."

REBUILD=false
TOOL_ARGS=()
for arg in "$@"; do
    case "$arg" in
        --rebuild) REBUILD=true ;;
        *) TOOL_ARGS+=("$arg") ;;
    esac
done

echo "========================================"
echo "Building cim-bench Docker images"
echo "========================================"

# Build base image only if missing (it contains no source; --rebuild to force)
if [ "$REBUILD" = true ] || ! podman image exists cim-bench/base:latest; then
    echo ""
    echo "[1/N] Building base image..."
    podman build -f docker/base.dockerfile -t cim-bench/base:latest .
else
    echo ""
    echo "Base image exists - skipping build (use --rebuild to force)"
fi

if [ ${#TOOL_ARGS[@]} -gt 0 ]; then
    TOOL_NAMES="${TOOL_ARGS[*]}"
else
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
fi

# Count unique tools
TOTAL_TOOLS=$(echo "$TOOL_NAMES" | wc -w)
echo "Building $TOTAL_TOOLS tool image(s): $(echo $TOOL_NAMES | tr '\n' ' ')"

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
