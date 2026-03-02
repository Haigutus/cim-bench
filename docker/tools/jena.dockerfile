# Stage 1: Download Apache Jena dependencies with Maven
FROM docker.io/eclipse-temurin:17-jdk AS builder

WORKDIR /build

# Install Maven
RUN apt-get update && \
    apt-get install -y maven && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml and download Apache Jena dependencies
COPY tool-configs/jena/pom.xml /build/pom.xml
RUN mvn dependency:copy-dependencies -DoutputDirectory=/build/lib

# Stage 2: Runtime image with JRE and Python
FROM localhost/cim-bench/base:latest

# Install Java JRE 17
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless && \
    rm -rf /var/lib/apt/lists/*

# Copy JAR files from builder
COPY --from=builder /build/lib /app/lib

# Install Python dependencies
WORKDIR /app
COPY tool-configs/jena/pyproject.toml .
RUN uv sync

# Install common testing framework dependencies into the same venv
COPY tool-configs/common/requirements.txt ./requirements.txt
RUN uv pip install -r requirements.txt

# Set up Java environment
ENV CLASSPATH="/app/lib/*"
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /benchmarks

CMD ["pytest", "jena_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/jena_svedala_benchmark.json"]
