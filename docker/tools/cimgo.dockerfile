FROM localhost/cim-bench/base:latest

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Fetch pre-built cimgo binary from GitHub release
ARG CIMGO_VERSION=v0.0.5
RUN curl -fsSL \
    "https://github.com/m-mirz/cimgo/releases/download/${CIMGO_VERSION}/cimcli-linux-amd64" \
    -o /usr/local/bin/cimcli-linux-amd64 \
    && chmod +x /usr/local/bin/cimcli-linux-amd64

# Install test dependencies (wheel cache persists across builds via cache mount)
WORKDIR /app
COPY tool-configs/cimgo/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv uv sync

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks
