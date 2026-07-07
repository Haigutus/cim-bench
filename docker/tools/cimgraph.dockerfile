FROM localhost/cim-bench/base:latest

WORKDIR /app

# Install dependencies (wheel cache persists across builds via cache mount)
COPY tool-configs/cimgraph/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv uv sync --prerelease=allow

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "cimgraph_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/cimgraph_svedala_benchmark.json"]
