FROM localhost/cim-bench/base:latest

WORKDIR /app

COPY tool-configs/powerio/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv uv sync

# An explicit prerelease or immutable source spec may be supplied for a separate
# comparison image. The result records the installed version, not this argument.
ARG POWERIO_SPEC=""
RUN --mount=type=cache,target=/root/.cache/uv \
    if [ -n "$POWERIO_SPEC" ]; then uv pip install --python .venv/bin/python "$POWERIO_SPEC"; fi

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "powerio_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/powerio_svedala_benchmark.json"]
