FROM localhost/cim-bench/base:latest

# Install curl to fetch the release tarball
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Fetch the prebuilt cimd binary from the Codeberg release.
# TARGETARCH is set automatically by BuildKit / podman buildx (amd64 or arm64).
ARG TARGETARCH=amd64
ARG CIMD_VERSION=v0.2.3
RUN case "${TARGETARCH}" in \
        amd64) CIMD_ARCH=x86_64 ;; \
        arm64) CIMD_ARCH=aarch64 ;; \
        *) echo "Unsupported TARGETARCH: ${TARGETARCH}" >&2; exit 1 ;; \
    esac && \
    curl -fsSL \
        "https://codeberg.org/caspereijkens/cimd/releases/download/${CIMD_VERSION}/cimd-${CIMD_VERSION}-${CIMD_ARCH}-linux.tar.gz" \
        | tar -xz -C /usr/local/bin && \
    chmod +x /usr/local/bin/cimd && \
    cimd version

# Install Python test dependencies in a venv
WORKDIR /app
COPY tool-configs/cimd/pyproject.toml .
RUN uv sync

COPY tool-configs/common/requirements.txt ./requirements.txt
RUN uv pip install -r requirements.txt

ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "cimd_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/cimd_svedala_benchmark.json"]
