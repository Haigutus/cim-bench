FROM localhost/cim-bench/base:latest

# Note: Java NOT needed - pypowsybl v1.14.0 uses GraalVM native libraries
# Built with GraalVM JDK 21, but runtime is pure native code
WORKDIR /app

# Install dependencies (wheel cache persists across builds via cache mount)
COPY tool-configs/pypowsybl/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv uv sync

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "pypowsybl_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/pypowsybl_svedala_benchmark.json"]
