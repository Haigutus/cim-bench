FROM debian:bookworm-slim

# Copy uv from official image (pinned - bump deliberately)
COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /uvx /bin/

RUN apt-get update && apt-get install -y \
    ca-certificates \
    git \
    && rm -rf /var/lib/apt/lists/*

# No source baked in: benchmarks/ and parsers/ are volume-mounted at runtime,
# so code changes never invalidate image layers
WORKDIR /benchmarks

# Add parsers to Python path so benchmark files can import adapters
ENV PYTHONPATH="/benchmarks/parsers:${PYTHONPATH}"
# Required for uv cache mounts (cache and venv are on different filesystems)
ENV UV_LINK_MODE=copy

CMD ["bash"]
