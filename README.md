# cim-bench

Performance benchmarking suite for CIM (Common Information Model) parsers and serializers.

## Benchmark Results

Latest results on AMD Ryzen AI 9 HX 370, 64GB RAM, Python 3.13.12:

### Comparison Summary

**Small Dataset (Svedala - 7.3 MB):**

| Library | Load Time | Memory | Query Speed | Elements |
|---------|-----------|--------|-------------|----------|
| **triplets** | 138 ms | 62.8 MB | 1.9-5.7 ms | 97 lines, 39 gen, 73 loads, 57 subs |
| **pypowsybl** | 477 ms | 944.1 MB | 199-405 μs | 97 lines, 39 gen, 73 loads, 57 subs |
| **VeraGrid** | 1.50 s | 615.4 MB | 46-98 ns | 97 lines, 39 gen, 73 loads, 56 subs |
| **CIM-Graph** | 1.66 s | 277.1 MB | 108-334 ms | 97 lines, 39 gen, 73 loads, 56 subs |
| **RDFlib** | 1.70 s | 263.5 MB | 57-160 μs | 97 lines, 39 gen, 73 loads, 56 subs |

**Large Dataset (RealGrid - 86.5 MB):**

| Library | Load Time | Memory | Query Speed | Elements |
|---------|-----------|--------|-------------|----------|
| **triplets** | 1.56 s | 515.6 MB | 17.6-52.9 ms | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **pypowsybl** | 4.85 s | 4433.3 MB | 3.1-35.3 ms | 7561 lines, 1347 gen, 6687 loads, 4791* subs |
| **VeraGrid** | 17.84 s | 2681.1 MB | 47-125 ns | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **CIM-Graph** | 34.55 s | 3037.3 MB | 2.1-6.3 s | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **RDFlib** | 34.76 s | 2765.0 MB | 371 μs-2.0 ms | 7561 lines, 1347 gen, 6687 loads, 4875 subs |

*pypowsybl converts some substations to voltage levels when connected by transformers, resulting in 84 fewer substations in RealGrid*


### Import Performance Comparison

![Import Performance](results/graphs/import_comparison.svg)
<!-- ![Memory Usgae](results/graphs/memory_comparison.svg) -->

*Cross-dataset comparison showing how all five parsers scale from small (7.3 MB) to large (86.5 MB) datasets*

### Detailed Results: Svedala IGM Dataset (7.3 MB, CGMES 3.0)

#### triplets - RDF/Pandas Parser
- **Load Time**: 138 ms
- **Memory**: 62.8 MB
- **Data Structure**: ~95,000 triplets, ~14,500 unique objects
- **Network Elements**: 97 lines, 39 generators, 73 loads, 57 substations
- **Query Performance**: 1.9-5.7 ms (DataFrame queries for CIM types)
- **Strengths**: Fastest loading, minimal memory, simple API, pandas integration
- **Use Case**: Data extraction, batch processing, RDF manipulation, quick analysis

#### pypowsybl - Power System Network Model
- **Load Time**: 477 ms (3.5x slower than triplets)
- **Memory**: 944.1 MB (15x more than triplets)
- **Network Elements**: 97 lines, 39 generators, 73 loads, 57 substations
- **Query Performance**: 199-405 μs (DataFrame access to network model)
- **Strengths**: Rich network model, sub-millisecond queries, analysis-ready
- **Use Case**: Power flow analysis, network operations, TSO applications, CGMES validation

#### VeraGrid - CGMES Circuit Model
- **Load Time**: 1.50 s (10.9x slower than triplets, 3.1x slower than pypowsybl)
- **Memory**: 615.4 MB (9.8x more than triplets, 0.65x pypowsybl)
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 substations
- **Query Performance**: 46-98 ns (O(1) list access to CGMES assets)
- **Strengths**: Fastest queries (sub-microsecond), direct CGMES object access, full circuit model
- **Use Case**: CGMES analysis, rapid queries on loaded data, GridCal power systems analysis

#### CIM-Graph - Knowledge Graph API
- **Load Time**: 1.66 s (12x slower than triplets)
- **Memory**: 277.1 MB (4.4x more than triplets)
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 substations
- **Query Performance**: 108-334 ms (Python object graph traversal)
- **Strengths**: Modern typed API, RDFlib backend, CIM object model
- **Use Case**: Research, development, CIM data exploration, semantic analysis

#### RDFlib - Generic RDF Parser
- **Load Time**: 1.70 s (12.3x slower than triplets)
- **Memory**: 263.5 MB (4.2x more than triplets)
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 substations
- **Query Performance**: 57-160 μs (SPARQL queries on triple store)
- **Strengths**: Standard RDF library, flexible SPARQL queries, semantic web ready
- **Use Case**: RDF/SPARQL queries, semantic web applications, baseline comparison

### Detailed Results: RealGrid Dataset (86.5 MB, CGMES 2.4.15)

#### triplets - RDF/Pandas Parser
- **Load Time**: 1.56 s
- **Memory**: 515.6 MB
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads (EnergyConsumer), 4875 substations
- **Query Performance**: 17.6-52.9 ms (DataFrame queries scale with data size)
- **Strengths**: Fastest loading, linear scaling, handles large datasets efficiently
- **Use Case**: Large-scale data processing, European grid analysis

#### pypowsybl - Power System Network Model
- **Load Time**: 4.85 s (3.1x slower than triplets)
- **Memory**: 4433.3 MB (8.6x more than triplets)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4791 substations ⚠️
- **Query Performance**: 3.1-35.3 ms (DataFrame access to network model)
- **Strengths**: Fast queries even on large datasets, comprehensive network model
- **Use Case**: Pan-European grid analysis, large TSO networks, production systems
- **Note**: ⚠️ Converts some substations to voltage levels (84 fewer than other parsers)

#### VeraGrid - CGMES Circuit Model
- **Load Time**: 17.84 s (11.4x slower than triplets, 3.7x slower than pypowsybl)
- **Memory**: 2681.1 MB (5.2x more than triplets, 0.60x pypowsybl)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 47-125 ns (O(1) list access to CGMES assets)
- **Strengths**: Sub-nanosecond queries, direct CGMES object access, scales well for queries
- **Use Case**: Large-scale CGMES analysis, query-intensive workflows, GridCal integration

#### CIM-Graph - Knowledge Graph API
- **Load Time**: 34.55 s (22.1x slower than triplets, 7.1x slower than pypowsybl)
- **Memory**: 3037.3 MB (5.9x more than triplets)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 2.1-6.3 s (Python object graph traversal)
- **Strengths**: Modern typed API, RDFlib backend, CIM object model
- **Use Case**: Research, development, CIM data exploration, semantic analysis

#### RDFlib - Generic RDF Parser
- **Load Time**: 34.76 s (22.3x slower than triplets, 7.2x slower than pypowsybl)
- **Memory**: 2765.0 MB (5.4x more than triplets)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 371 μs-2.0 ms (SPARQL queries on triple store)
- **Strengths**: Standard RDF library, flexible SPARQL queries, semantic web ready
- **Use Case**: RDF/SPARQL queries, semantic web applications, baseline comparison


See `tools/*/README.md` for detailed per-tool documentation and analysis.

## Planned Test Additions

## Parsers/Serializers

| Status | Tool / Library | Language | Main Purpose / Strength | Triplet / Graph Access? | CGMES / CIM Support | GitHub / Source | Notes |
|--------|----------------|----------|-------------------------|------------------------|---------------------|-----------------|-------|
| ✅ | **triplets** | Python | Pandas-based RDF parser | Yes (DataFrame triplets) | Version-agnostic CIM/CGMES | [triplets](https://github.com/Haigutus/triplets) | Fast loading, low memory, simple API |
| ✅ | **pypowsybl** | Python | PowSyBl wrapper (network import/export) | Indirect (via network objects) | CGMES 2.4.15/3.0 CGMES import/export | [powsybl/pypowsybl](https://github.com/powsybl/pypowsybl) | Grid-analysis oriented; rich network model |
| ✅ | **GridCal/VeraGrid** | Python | Power systems analysis with UI | Indirect (CGMES circuit model) | CGMES 2.4.15/3.0 import | [SanPen/GridCal](https://github.com/SanPen/GridCal) | Sub-microsecond queries, full circuit model |
| ✅ | **RDFlib** | Python | Generic RDF parser/triple store | Excellent (native triples) | None (generic) | [RDFLib/rdflib](https://github.com/RDFLib/rdflib) | Baseline for speed/memory comparison with Oxigraph |
| ✅ | **CIMantic Graphs** | Python | In-memory labeled property graph | Yes (strong, knowledge graph API) | CIM15–18, custom profiles | [PNNL-CIM-Tools/CIM-Graph](https://github.com/PNNL-CIM-Tools/CIM-Graph) | Modern API, uses RDFlib with typed CIM objects |
| ⚠️ | **cimpy** | Python | Import/export/modify CGMES XML/RDF | Yes (via object topology dict) | CGMES 2.4.15 (partial) | [sogno-platform/cimpy](https://github.com/sogno-platform/cimpy) | Compatibility issues: v1.1.0 only has cgmes_v2_4_15 classes (no CGMES 3.0), parsing bugs with test datasets |
| ❌ | **pycgmes** | Python | Dataclasses + RDF schema + SHACL | Yes (dataclass mapping) | CGMES 3.0+ | [alliander-opensource/pycgmes](https://github.com/alliander-opensource/pycgmes) | No file import capability - dataclass definitions only |
| 📋 | **libcimpp** | C++ | Fast serialize/deserialize CIM XML/RDF | Partial (object model) | CGMES / IEC61970/61968/62325 | [sogno-platform/libcimpp](https://github.com/sogno-platform/libcimpp) | Likely fastest/lowest memory |
| 📋 | **OpenCGMES** | Java | Suite for CGMES / CIM RDF parser | Yes (CIMXML parser) | CGMES / IEC61970-552 | [SOPTIM/OpenCGMES](https://github.com/SOPTIM/OpenCGMES) | Recent CIMXML-specific fixes |
| 📋 | **Apache Jena** | Java | RDF framework + CIMXML parser | Excellent | Potential via custom parser | [apache/jena](https://github.com/apache/jena) | Generic + 2025 CIMXML branch |
| 📋 | **CIMverter** | Java/C++ | Convert CIM RDF to Modelica | Partial | CGMES compatible | [cim-iec/cimverter](https://github.com/cim-iec/cimverter) | Round-trip fidelity testing |
| 📋 | **CIMDraw** | Web/JS | View/edit CGMES node-breaker models | Indirect | ENTSO-E CGMES profile | [danielePala/CIMDraw](https://github.com/danielePala/CIMDraw) | Visual completeness check |
| 📋 | **GraphDB** | Java | Graph database with RDF support | Excellent | Generic RDF | [Ontotext GraphDB](https://www.ontotext.com/products/graphdb/) | Enterprise SPARQL database |
| 📋 | **CIMbion** | TBD | CIM/CGMES data management | TBD | CGMES | [Veracity Store](https://store.veracity.com/cimbion) | Closed source, commercial |
| 📋 | **CIMdesk** | Various | CIM data management | TBD | CGMES | TBD | To be investigated |

**Legend:**
- ✅ Benchmarked
- ⚠️ Compatibility issues found
- ❌ Not suitable for import benchmarking
- 📋 Planned

### 📊 Additional Benchmarks

| Test Category | Description | Metrics | Why Important |
|---------------|-------------|---------|---------------|
| **Export/Serialization** | Write loaded CIM data back to RDF/XML | Time, file size, memory | Round-trip capability, data export use cases |
| **Round-trip Fidelity** | Load → Export → Load → Diff check | Time, diff count, data loss % | Data integrity, lossless conversion verification |
| **SHACL Validation** | Validate CIM models against SHACL shapes | Time, violations found, memory | Data quality, CGMES compliance checking |
| **SPARQL Queries** | Complex graph queries on loaded data | Query time, result count | Advanced data extraction, relationship queries |


### 📁 Planned Datasets

| Dataset | Size | CGMES Version | Network Type | Elements | Status | Purpose |
|---------|------|---------------|--------------|----------|--------|---------|
| **Svedala IGM** | 7.3 MB | CGMES 3.0 | Small (Sweden) | 97 lines, 39 gen, 73 loads, 56 subs | ✅ Active | Fast iteration, baseline tests |
| **RealGrid** | 86.5 MB (3.7 MB compressed) | CGMES 2.4.15 | Large (Pan-European) | 10,000+ elements | ✅ Active | Scalability, real-world TSO scenarios |
| **NC Profiles** | ~50-100 MB | CGMES 3.0 | Medium (ENTSO-E) | TBD | 📋 Planned | Network Code validation, cross-border |

**Comparison Targets**:
- **Small (Svedala)**: Fast parsing, edge case testing, CI/CD friendly
- **Large (RealGrid)**: Memory stress, scalability limits, production-scale performance

### 📈 Performance Visualizations

Performance graphs are automatically generated when running `./run_benchmarks.sh` (requires matplotlib).

**Visualization Types:**

#### Per-Dataset Comparisons
Graphs grouped by **dataset** showing tool comparisons side-by-side:

**Svedala Dataset (7.3 MB)**
- **Comparison**: Load time, memory, and average query performance for all three parsers
  - `results/graphs/svedala_comparison.svg`
- **Detailed**: Load time, memory, lines parsed, generators parsed
  - `results/graphs/svedala_detailed.svg`

**RealGrid Dataset (86.5 MB)**
- **Comparison**: Load time, memory, and average query performance for all three parsers
  - `results/graphs/realgrid_comparison.svg`
- **Detailed**: Load time, memory, lines parsed, generators parsed
  - `results/graphs/realgrid_detailed.svg`

#### Cross-Dataset Comparisons
Graphs showing all three parsers across both datasets for each metric:

- **Import Comparison**: Load/import time for all parsers on both datasets
  - `results/graphs/import_comparison.svg`
- **Memory Comparison**: Memory usage for all parsers on both datasets
  - `results/graphs/memory_comparison.svg`
- **Query Comparison**: Average query performance for all parsers on both datasets
  - `results/graphs/query_comparison.svg`

**Graph Layout**:
- Separate horizontal subplots per dataset (Svedala top, RealGrid bottom)
- Within each dataset, parsers sorted from fastest/smallest to slowest/largest
- Consistent x-axis scales across subplots for easy absolute comparison (log scale for query performance)
- Color palette: triplets (blue), pypowsybl (orange), VeraGrid (green), RDFlib (yellow), CIM-Graph (purple)

**Metrics visualized**:
- Import/load time (ms)
- Memory usage (MB)
- Query performance (ms, log scale)
- Network elements parsed (lines, generators, loads, substations)

*All graphs are generated in SVG format for scalability and web compatibility. Query performance graphs use logarithmic scale to show differences between fast parsers while keeping slower ones visible.*

### 🐳 Podman Containerization

**Isolated, reproducible benchmark environment per parser using uv-managed Python environments**

#### Features
- **One container per parser/tool** with all dependencies pre-installed
- **uv-managed Python versions**: Each tool specifies its exact Python version (==3.14.* or ==3.13.*) and dependencies
- **Multi-language support**: Base image supports Python (via uv), Java, C++, and Rust
- **Standardized test interface**: Same input datasets, same output format
- **No dependency conflicts**: Each parser runs in complete isolation
- **Reproducible**: Exact version pinning for consistent results across machines
- **Rootless execution**: Podman runs without root privileges, no daemon required

#### Architecture
```
docker/
├── base.dockerfile              # Multi-lang base with uv + source files
├── tools/
│   ├── triplets.dockerfile      # Install deps (Python 3.14 from pyproject.toml)
│   ├── pypowsybl.dockerfile     # Install deps + Java (Python 3.13)
│   ├── veragrid.dockerfile      # Install deps (Python 3.14)
│   ├── cimgraph.dockerfile      # Install deps (Python 3.14)
│   └── rdflib.dockerfile        # Install deps (Python 3.14)
├── docker-compose.yml           # Single source of truth for benchmarks
├── setup.sh                     # Build all images (reads docker-compose.yml)
└── run_benchmark.sh             # Run benchmarks + generate reports/graphs

tool-configs/
├── triplets/pyproject.toml      # Python ==3.14.* + dependencies
├── pypowsybl/pyproject.toml     # Python ==3.13.* + dependencies
├── veragrid/pyproject.toml      # Python ==3.14.* + dependencies
├── cimgraph/pyproject.toml      # Python ==3.14.* + dependencies
└── rdflib/pyproject.toml        # Python ==3.14.* + dependencies
```

**Key Design:**
- `docker-compose.yml` is the single source of truth for benchmarks
- `tool-configs/*/pyproject.toml` is the single source of truth for Python versions and dependencies
- `setup.sh` dynamically discovers tools from docker-compose.yml
- Source files in base image, tool images only install dependencies
- Results saved to `results-docker/` for easy comparison with native execution

#### Quick Start
```bash
# Build all Podman images
./docker/setup.sh

# Run all benchmarks in containers (includes report/graph generation)
./docker/run_benchmark.sh

# Parallel execution
./docker/run_benchmark.sh --parallel

# Using podman-compose directly
podman-compose -f docker/docker-compose.yml up
```

#### Container Image Sizes
- **Base**: ~100MB (Debian + uv + system tools)
- **triplets**: ~250MB (Base + Python 3.14 + deps)
- **pypowsybl**: ~450MB (Base + Python 3.13 + JDK 17 + deps)
- **veragrid**: ~300MB (Base + Python 3.14 + deps)
- **cimgraph**: ~350MB (Base + Python 3.14 + rdflib/Oxigraph)
- **rdflib**: ~300MB (Base + Python 3.14 + rdflib/Oxigraph)

**Total disk space**: ~1.75GB (base shared, actual ~1.5GB incremental)

#### Performance Validation
Containerized benchmarks validated against native execution on Podman 5.7.1 / Fedora 43:

**Load Test Overhead** (Primary Metric):
- **triplets**: +7.66% (acceptable)
- **rdflib**: -48% 🚀 (FASTER in container due to Python 3.14 improvements!)
- **pypowsybl**: +5.95% (acceptable)

All overhead within acceptable range for benchmarking. Python 3.14 provides significant performance benefits for some workloads.

See `CONTAINERIZATION_VALIDATION.md` for detailed validation results.

## Getting Started

### Prerequisites

#### Required for Native Execution

This repository uses **Git LFS** (Large File Storage) for large dataset files. Install it before cloning:

```bash
# Ubuntu/Debian
sudo apt-get install git-lfs

# macOS
brew install git-lfs

# After installation
git lfs install
```

For other systems, see: https://git-lfs.github.com/

#### Optional for Containerized Execution

If you want to run benchmarks in Podman containers:

```bash
# Fedora
sudo dnf install podman podman-compose

# Ubuntu/Debian
sudo apt-get install podman podman-compose

# macOS
brew install podman podman-compose
```

**Note**: Podman runs rootless by default (no daemon, no root privileges required). No additional user configuration needed.

### Quick Setup

**Automated setup (recommended):**
```bash
# Clone the repository
git clone https://github.com/yourusername/cim-bench.git
cd cim-bench

# Run setup script (installs uv, Git LFS, pulls submodules and LFS files, installs dependencies)
./setup.sh
```

**Manual setup:**
```bash
# Install Git LFS
git lfs install

# Clone with submodules
git clone --recurse-submodules https://github.com/yourusername/cim-bench.git
cd cim-bench

# Pull LFS files (parent repo and all submodules)
git lfs pull
git submodule foreach --recursive git lfs pull

# Install dependencies
uv sync

# Optional: Install visualization dependencies
uv sync --extra visualization
```

### Running Benchmarks

**Quick Start - Run all benchmarks and generate reports:**
```bash
./run_benchmarks.sh
```

**Fast iteration mode (fewer rounds):**
```bash
./run_benchmarks.sh --quick
```

**Skip benchmarks with existing results:**
```bash
./run_benchmarks.sh --skip-existing
```

**Combine flags:**
```bash
./run_benchmarks.sh --quick --skip-existing
```

This will:
1. Run all configured benchmarks (or skip those with existing JSON results if `--skip-existing` is used)
2. Save JSON results to `results/`
3. Generate individual markdown reports
4. Create a comparison summary report
5. Generate performance visualization graphs (if matplotlib is installed)

**Manual benchmark execution:**

Run all benchmarks:
```bash
uv run pytest benchmarks/ --benchmark-only
```

Run specific benchmark:
```bash
uv run pytest benchmarks/triplets_svedala_benchmark.py --benchmark-only
```

Save results to JSON:
```bash
uv run pytest benchmarks/ --benchmark-only --benchmark-json=results/output.json
```

Generate markdown report from results:
```bash
uv run python tools/generate_report.py results/output.json results/output_report.md
```

Generate comparison report:
```bash
uv run python tools/generate_comparison.py results/file1.json results/file2.json results/comparison.md
```

Generate performance visualization graphs:
```bash
uv run python tools/generate_graphs.py
```

This creates SVG graphs in `results/graphs/`:

**Per-dataset comparisons** (tools compared within each dataset):
- `svedala_comparison.svg` - Svedala: load time, memory, and query performance
- `svedala_detailed.svg` - Svedala: detailed metrics with network elements
- `realgrid_comparison.svg` - RealGrid: load time, memory, and query performance
- `realgrid_detailed.svg` - RealGrid: detailed metrics with network elements

**Cross-dataset comparisons** (all three parsers across both datasets):
- `import_comparison.svg` - Import/load time comparison
- `memory_comparison.svg` - Memory usage comparison
- `query_comparison.svg` - Query performance comparison

**Adding new benchmarks:**

The benchmark runner automatically discovers all `*_benchmark.py` files in the `benchmarks/` directory. Simply create a new benchmark file following the adapter pattern (see `CLAUDE.md` for details) and it will be included in the next run.

### Running Benchmarks with Podman

**Quick Start - Build and run all benchmarks in containers:**
```bash
# Build all Podman images
./docker/setup.sh

# Run all benchmarks (includes report/graph generation)
./docker/run_benchmark.sh
```

**Parallel execution (all tools at once):**
```bash
./docker/run_benchmark.sh --parallel
```

**Using podman-compose:**
```bash
# Run all benchmarks in parallel
podman-compose -f docker/docker-compose.yml up

# Run specific tool
podman-compose -f docker/docker-compose.yml run --rm triplets-svedala
```

**Manual Podman execution:**
```bash
# Run specific tool benchmark
podman run --rm \
  -v $(pwd)/data:/benchmarks/data:ro,z \
  -v $(pwd)/results-docker:/output:z \
  cim-bench/triplets:latest

# Run with custom pytest options
podman run --rm \
  -v $(pwd)/data:/benchmarks/data:ro,z \
  -v $(pwd)/results-docker:/output:z \
  cim-bench/triplets:latest \
  pytest triplets_svedala_benchmark.py --benchmark-only --benchmark-min-rounds=3
```

**Note**: The `:z` flag in volume mounts enables SELinux relabeling (required on Fedora/RHEL).

This will:
1. Run all configured benchmarks in isolated containers
2. Save JSON results to `results-docker/`
3. Generate individual markdown reports
4. Generate comparison summary
5. Generate performance visualization graphs

**Podman vs Native:**
- Podman adds 5-8% overhead (acceptable for benchmarking)
- Python 3.14 in containers provides performance benefits (48% faster for rdflib!)
- Use Podman for reproducibility, isolation, and consistent Python versions
- Use native for fastest iteration during development
- Both produce identical JSON output format

## Contributing

Add new benchmark cases in the `benchmarks/` directory following the existing patterns.
