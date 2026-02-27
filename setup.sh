#!/bin/bash
set -e

# Check for Git LFS
if ! command -v git-lfs &> /dev/null; then
    echo "⚠️  Git LFS not found. Large dataset files won't be available."
    echo "   Install: https://git-lfs.github.com/"
    echo "   Then run: git lfs install && git lfs pull"
else
    git lfs install 2>/dev/null || true
fi

# Install uv if not present
command -v uv &> /dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize git submodules and pull LFS files
if [ -d ".git" ]; then
    git submodule update --init --recursive
    if command -v git-lfs &> /dev/null; then
        git lfs pull
        git submodule foreach --recursive git lfs pull
    fi
fi

# Install dependencies
uv sync --extra visualization --prerelease=allow

echo "✓ Setup complete! Run: ./run_benchmarks.sh"
