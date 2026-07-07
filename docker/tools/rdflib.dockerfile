FROM localhost/cim-bench/base:latest

WORKDIR /app

# Install dependencies (wheel cache persists across builds via cache mount)
COPY tool-configs/rdflib/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv uv sync

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "rdflib_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/rdflib_svedala_benchmark.json"]
