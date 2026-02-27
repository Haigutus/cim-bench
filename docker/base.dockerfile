FROM debian:bookworm-slim

# Copy uv from official image (recommended approach)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && apt-get install -y \
    ca-certificates \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN uv --version

# Copy all source files to base image
WORKDIR /benchmarks
COPY parsers/ /benchmarks/parsers/
COPY benchmarks/ /benchmarks/

# Add parsers to Python path so benchmark files can import adapters
ENV PYTHONPATH="/benchmarks/parsers:${PYTHONPATH}"

CMD ["bash"]
