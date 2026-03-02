# Stage 1: Build OpenCGMES from source with Maven
FROM docker.io/eclipse-temurin:21-jdk AS builder

WORKDIR /build

# Install Maven and Git
RUN apt-get update && \
    apt-get install -y maven git && \
    rm -rf /var/lib/apt/lists/*

# Clone and build OpenCGMES from source
RUN git clone https://github.com/SOPTIM/OpenCGMES.git && \
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

# Copy uv from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy source files from base build context
WORKDIR /benchmarks
COPY parsers/ /benchmarks/parsers/
COPY benchmarks/ /benchmarks/

# Set Python path
ENV PYTHONPATH="/benchmarks/parsers:${PYTHONPATH}"

# Copy JAR files from builder
COPY --from=builder /build/lib /app/lib

# Install Python dependencies
WORKDIR /app
COPY tool-configs/opencgmes/pyproject.toml .
RUN uv sync

# Install common testing framework dependencies into the same venv
COPY tool-configs/common/requirements.txt ./requirements.txt
RUN uv pip install -r requirements.txt

# Set up Java environment
ENV CLASSPATH="/app/lib/*"
ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /benchmarks

CMD ["pytest", "opencgmes_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/opencgmes_svedala_benchmark.json"]
