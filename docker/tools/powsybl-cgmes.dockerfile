# Stage 1: Download PowSyBL dependencies with Maven
FROM docker.io/eclipse-temurin:21-jdk AS builder

WORKDIR /build

# Install Maven
RUN apt-get update && \
    apt-get install -y maven && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml and download dependencies
COPY tool-configs/powsybl-cgmes/pom.xml .
RUN mvn dependency:copy-dependencies -DoutputDirectory=/build/lib

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
COPY tool-configs/powsybl-cgmes/pyproject.toml .
RUN uv sync

# Install common testing framework dependencies into the same venv
COPY tool-configs/common/requirements.txt ./requirements.txt
RUN uv pip install -r requirements.txt

# Set up Java environment
ENV CLASSPATH="/app/lib/*"
ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /benchmarks

CMD ["pytest", "powsybl_cgmes_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/powsybl_cgmes_svedala_benchmark.json"]
