# Build stage: restore the GridLab GMSS CIM NuGet packages (public on
# nuget.org) and publish to collect all managed DLLs
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS dotnet-build
WORKDIR /build
COPY tool-configs/gmss/gmss.csproj .
RUN --mount=type=cache,target=/root/.nuget/packages dotnet publish -c Release -o /build/publish

FROM localhost/cim-bench/base:latest

# .NET runtime for pythonnet (coreclr)
RUN apt-get update && apt-get install -y wget libicu72 libssl3 \
    && wget -q https://dot.net/v1/dotnet-install.sh -O /tmp/dotnet-install.sh \
    && bash /tmp/dotnet-install.sh --channel 10.0 --runtime dotnet --install-dir /usr/share/dotnet \
    && ln -s /usr/share/dotnet/dotnet /usr/local/bin/dotnet \
    && rm -rf /var/lib/apt/lists/* /tmp/dotnet-install.sh

COPY --from=dotnet-build /build/publish /opt/gmss

WORKDIR /app

# Install tool-specific dependencies first (establishes Python version)
COPY tool-configs/gmss/pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/uv uv sync

ENV PATH="/app/.venv/bin:${PATH}"
ENV PYTHONNET_RUNTIME=coreclr
ENV DOTNET_ROOT=/usr/share/dotnet
ENV GMSS_DLL_DIR=/opt/gmss
WORKDIR /benchmarks

CMD ["pytest", "docker_gmss_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/gmss_svedala_benchmark.json"]
