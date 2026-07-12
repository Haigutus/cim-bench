FROM localhost/cim-bench/base:latest

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Fetch pre-built cimd binary from the Codeberg release
ARG CIMD_VERSION=v0.4.0
RUN curl -fsSL \
    "https://codeberg.org/caspereijkens/cimd/releases/download/${CIMD_VERSION}/cimd-${CIMD_VERSION}-x86_64-linux.tar.gz" \
    | tar -xz -C /usr/local/bin \
    && chmod +x /usr/local/bin/cimd \
    && cimd version

# Install test dependencies (wheel cache persists across builds via cache mount)
WORKDIR /app
COPY tool-configs/cimd/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv uv sync

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "cimd_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/cimd_svedala_benchmark.json"]
