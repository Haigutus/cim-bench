# Stage 1: Download Java dependencies with Maven
FROM docker.io/eclipse-temurin:21-jdk AS builder

WORKDIR /build

# Install Maven
RUN apt-get update && \
    apt-get install -y maven && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml and download dependencies (repo cache persists via cache mount)
COPY tool-configs/powsybl-cgmes/pom.xml /build/pom.xml
RUN --mount=type=cache,target=/root/.m2 \
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
COPY tool-configs/powsybl-cgmes/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv UV_LINK_MODE=copy uv sync

# Source (benchmarks/, parsers/) is volume-mounted at runtime
ENV PYTHONPATH="/benchmarks/parsers:${PYTHONPATH}"
ENV CLASSPATH="/app/lib/*"
ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /benchmarks

CMD ["pytest", "docker_powsybl_cgmes_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/powsybl_cgmes_svedala_benchmark.json"]
