# Stage 1: Build OpenCGMES from source with Maven
FROM docker.io/eclipse-temurin:21-jdk AS builder

WORKDIR /build

# Install Maven and Git
RUN apt-get update && \
    apt-get install -y maven git && \
    rm -rf /var/lib/apt/lists/*

# Clone OpenCGMES pinned to a commit (reproducible layer)
ARG OPENCGMES_COMMIT=27ff47bc69a05b885ee3642df8155fd67bae4113
RUN git clone https://github.com/SOPTIM/OpenCGMES.git && \
    cd OpenCGMES && \
    git checkout ${OPENCGMES_COMMIT}

# Build (Maven repo cache persists via cache mount)
RUN --mount=type=cache,target=/root/.m2 \
    cd OpenCGMES/cimxml && \
    mvn clean package -DskipTests && \
    mkdir -p /build/lib && \
    cp target/*.jar /build/lib/ && \
    mvn dependency:copy-dependencies -DoutputDirectory=/build/lib

# Stage 2: Runtime image with JRE 21 and Python
FROM docker.io/eclipse-temurin:21-jre

# Install ca-certificates and git (needed for uv)
RUN apt-get update && \
    apt-get install -y ca-certificates git && \
    rm -rf /var/lib/apt/lists/*

# Copy uv from official image (pinned - bump deliberately)
COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /uvx /bin/

# Copy JAR files from builder
COPY --from=builder /build/lib /app/lib

# Install Python dependencies (wheel cache persists via cache mount)
WORKDIR /app
COPY tool-configs/opencgmes/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv UV_LINK_MODE=copy uv sync

# Source (benchmarks/, parsers/) is volume-mounted at runtime
ENV PYTHONPATH="/benchmarks/parsers:${PYTHONPATH}"
ENV CLASSPATH="/app/lib/*"
ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /benchmarks

CMD ["pytest", "docker_opencgmes_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/opencgmes_svedala_benchmark.json"]
