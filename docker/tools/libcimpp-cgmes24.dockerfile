# Stage 1: Build pybind11 wrapper
FROM ubuntu:24.04 AS builder

# Copy uv for Python version management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

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
RUN uv python install 3.14 && \
    uv venv --python 3.14 && \
    uv pip install 'pybind11[global]>=2.13.0'

# Add Python 3.14 venv to PATH
ENV PATH="/tmp/build_env/.venv/bin:${PATH}"

# Download and install libcimpp CGMES 2.4.15 Jan 2020 .deb package
WORKDIR /tmp
RUN wget https://github.com/sogno-platform/libcimpp/releases/download/release/v2.2.0/libcimpp_CGMES_2.4.15_27JAN2020-2.2.0-Linux.deb && \
    dpkg -i libcimpp_CGMES_2.4.15_27JAN2020-2.2.0-Linux.deb || apt-get install -f -y && \
    rm libcimpp_CGMES_2.4.15_27JAN2020-2.2.0-Linux.deb

# Build pybind11 wrapper
COPY parsers/libcimpp_wrapper /build/wrapper
WORKDIR /build/wrapper
RUN mkdir build && cd build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release && \
    make -j$(nproc)

# Stage 2: Runtime with Python
FROM ubuntu:24.04

# Copy uv for Python management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    wget \
    libxml2 \
    libstdc++6 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install libcimpp CGMES 2.4.15 from .deb package
WORKDIR /tmp
RUN wget https://github.com/sogno-platform/libcimpp/releases/download/release/v2.2.0/libcimpp_CGMES_2.4.15_27JAN2020-2.2.0-Linux.deb && \
    dpkg -i libcimpp_CGMES_2.4.15_27JAN2020-2.2.0-Linux.deb && \
    rm libcimpp_CGMES_2.4.15_27JAN2020-2.2.0-Linux.deb

# Copy built wrapper from builder
COPY --from=builder /build/wrapper/build/_libcimpp_benchmark*.so /app/lib/

# Install Python dependencies
WORKDIR /app
COPY tool-configs/libcimpp/pyproject.toml .
RUN uv sync

COPY tool-configs/common/requirements.txt ./requirements.txt
RUN uv pip install -r requirements.txt

# Copy source files
WORKDIR /benchmarks
COPY parsers/ /benchmarks/parsers/
COPY benchmarks/ /benchmarks/

# Set library paths
ENV LD_LIBRARY_PATH="/usr/local/lib:/app/lib:${LD_LIBRARY_PATH}"
ENV PYTHONPATH="/app/lib:/benchmarks/parsers:${PYTHONPATH}"
ENV PATH="/app/.venv/bin:${PATH}"

CMD ["pytest", "libcimpp_realgrid_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/libcimpp_realgrid_benchmark.json"]
