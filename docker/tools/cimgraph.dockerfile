FROM localhost/cim-bench/base:latest

WORKDIR /app

# Install tool-specific dependencies first (establishes Python version)
COPY tool-configs/cimgraph/pyproject.toml .
RUN uv sync --prerelease=allow

# Install common testing framework dependencies into the same venv
COPY tool-configs/common/requirements.txt ./requirements.txt
RUN uv pip install -r requirements.txt

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "cimgraph_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/cimgraph_svedala_benchmark.json"]
