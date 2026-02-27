FROM cim-bench/base:latest

# Note: Java NOT needed - pypowsybl v1.14.0 uses GraalVM native libraries
# Built with GraalVM JDK 21, but runtime is pure native code

WORKDIR /app

# Install tool-specific dependencies first (establishes Python version)
COPY tool-configs/pypowsybl/pyproject.toml .
RUN uv sync

# Install common testing framework dependencies into the same venv
COPY tool-configs/common/requirements.txt ./requirements.txt
RUN uv pip install -r requirements.txt

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "pypowsybl_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/pypowsybl_svedala_benchmark.json"]
