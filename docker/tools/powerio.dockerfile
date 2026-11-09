FROM localhost/cim-bench/base:latest

WORKDIR /app

COPY tool-configs/powerio/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv uv sync

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "powerio_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/powerio_svedala_benchmark.json"]
