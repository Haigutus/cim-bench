# Stage 1: Build pybind11 wrapper
FROM ubuntu:24.04 AS builder

# Copy uv for Python version management (pinned - bump deliberately)
COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /uvx /bin/

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    wget \
    libxml2-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python 3.14 and pybind11 using uv
WORKDIR /tmp/build_env
RUN --mount=type=cache,target=/root/.cache/uv \
    UV_LINK_MODE=copy uv python install 3.14 && \
    uv venv --python 3.14 && \
    UV_LINK_MODE=copy uv pip install 'pybind11[global]>=2.13.0'

# Add Python 3.14 venv to PATH
ENV PATH="/tmp/build_env/.venv/bin:${PATH}"

# Download and install libcimpp CGMES 3.0.0 .deb package (kept for runtime stage)
WORKDIR /tmp
RUN wget https://github.com/sogno-platform/libcimpp/releases/download/release/v2.2.0/libcimpp_CGMES_3.0.0-2.2.0-Linux.deb && \
    (dpkg -i libcimpp_CGMES_3.0.0-2.2.0-Linux.deb || apt-get install -f -y)

# Build pybind11 wrapper
COPY parsers/libcimpp_wrapper /build/wrapper
WORKDIR /build/wrapper
RUN mkdir build && cd build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release && \
    make -j$(nproc)

# Stage 2: Runtime with Python
FROM ubuntu:24.04

# Copy uv for Python management (pinned - bump deliberately)
COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /uvx /bin/

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libxml2 \
    libstdc++6 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install libcimpp from the .deb already downloaded in the builder
COPY --from=builder /tmp/libcimpp_CGMES_3.0.0-2.2.0-Linux.deb /tmp/libcimpp_CGMES_3.0.0-2.2.0-Linux.deb
RUN dpkg -i /tmp/libcimpp_CGMES_3.0.0-2.2.0-Linux.deb && rm /tmp/libcimpp_CGMES_3.0.0-2.2.0-Linux.deb

# Copy built wrapper from builder
COPY --from=builder /build/wrapper/build/_libcimpp_benchmark*.so /app/lib/

# Install Python dependencies (wheel cache persists via cache mount)
WORKDIR /app
COPY tool-configs/libcimpp/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv UV_LINK_MODE=copy uv sync

# Source (benchmarks/, parsers/) is volume-mounted at runtime
ENV LD_LIBRARY_PATH="/usr/local/lib:/app/lib:${LD_LIBRARY_PATH}"
ENV PYTHONPATH="/app/lib:/benchmarks/parsers:${PYTHONPATH}"
ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /benchmarks

CMD ["pytest", "libcimpp_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/libcimpp_svedala_benchmark.json"]
