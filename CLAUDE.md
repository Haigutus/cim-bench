# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**cim-bench** is a performance benchmarking suite for CIM (Common Information Model) parsers and serializers. It measures load time, memory usage, and query performance of different libraries parsing CGMES (Common Grid Model Exchange Standard) XML/RDF files.

## Architecture

### Adapter Pattern (Core Design)

The codebase uses an adapter pattern to standardize benchmarking across different parsers:

1. **`parsers/parser_adapter.py`**: Abstract interface all parsers must implement
   - `load()`, `get_load_metrics()`, `get_lines_count()`, etc.
   - `get_display_name()`, `get_color()`: Return display name and color for graphs

2. **Parser adapters** (e.g., `pypowsybl_adapter.py`, `triplets_adapter.py`):
   - Implement ParserAdapter interface
   - Define display name and color as class methods
   - Handle parser-specific data structures

3. **`benchmarks/benchmark_template.py`**: Dynamic test generator
   - `create_benchmarks()` injects tests into caller's module namespace
   - Embeds display_name and color from adapter into JSON extra_info
   - Creates 1 load test + 4 query tests automatically

4. **Individual benchmark files** (~15 lines each):
   ```python
   from triplets_adapter import TripletsAdapter
   from benchmark_template import create_benchmarks

   create_benchmarks(
       adapter=TripletsAdapter(),
       dataset_key="svedala_igm_cgmes_3",
       parser_name="triplets",
       dataset_name="svedala"
   )
   ```

### Data Flow

```
Adapter (display_name, color, tags)
    ↓
Benchmark template (embeds in extra_info)
    ↓
pytest-benchmark JSON results
    ↓
benchmark_data.py (shared loader, reads JSON only)
    ↓                          ↓
generate_graphs.py      generate_site.py
(SVG visualizations)    (docs/index.html - GitHub Pages,
                         sortable/filterable, tag chips)
```

**Key insight**: Display names, colors and tags are embedded in JSON reports, so the graph/site generators never import adapters—they just read JSON files (`tools/benchmark_data.py` is the shared loader).

**Tool tags**: each adapter declares `get_tags()` (capability + language, e.g. `["parser", "serializer", "query", "python"]`; CLI template always adds `"cli"`). Vocabulary: `parser`, `serializer`, `validator`, `query`, `powerflow-tool`, `triplestore`, `typed-model`, `cli` + language tags (`python`, `java`, `c++`, `rust`, `go`, `c#`). Tags drive the filter chips on the results site.

### Dataset Configuration

**`parsers/datasets.py`**: Central registry with two datasets:
- **svedala_igm_cgmes_3**: Small (7.3 MB, CGMES 3.0)
- **realgrid_cgmes_2_4**: Large (86.5 MB, CGMES 2.4.15)

Each dataset includes file paths, CGMES version, size, and expected element counts.

## Common Commands

### Running Benchmarks

```bash
# Run all benchmarks with full pipeline
./run_benchmarks.sh

# Quick mode (fewer rounds, faster)
./run_benchmarks.sh --quick

# Run specific benchmark
uv run pytest benchmarks/triplets_svedala_benchmark.py --benchmark-only

# Run with JSON output
uv run pytest benchmarks/ --benchmark-only --benchmark-json=results/output.json
```

### Report Generation

```bash
# Generate markdown report from JSON
uv run python tools/generate_report.py results/benchmark.json results/report.md

# Generate comparison from multiple JSONs
uv run python tools/generate_comparison.py results/file1.json results/file2.json results/comparison.md

# Generate all graphs (reads all JSONs in results/)
uv run python tools/generate_graphs.py

# Generate the results site for GitHub Pages (reads all JSONs, writes docs/)
uv run python tools/generate_site.py results-docker docs
```

### Environment Setup

```bash
# Initial setup
./setup.sh

# Sync dependencies
uv sync

# Install with visualization (matplotlib)
uv sync --extra visualization
```

## Podman Containerization

The project supports Podman-based benchmarking using uv-managed Python environments. Each tool runs in its own container with isolated dependencies.

### Containerization Architecture

- **Base image** (`debian:bookworm-slim`): Multi-language support (Python via uv, Java, C++, Rust) + all source files
- **Per-tool images**: Each parser has its own container with exact Python version (==3.14.* or ==3.13.*) and dependencies
- **uv-managed environments**: Python versions and packages managed by uv (no Python in base image)
- **Tool configurations**: Each tool defines exact dependencies in `tool-configs/{tool}/pyproject.toml`
- **Optimized structure**: Source files in base image, tool images only install dependencies
- **Best practices**: Follows official uv Docker guide - copies binary from official image, uses `uv sync`
- **Rootless execution**: Podman runs without root privileges, no daemon required

### Directory Structure

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
├── setup.sh                     # Build images (all, or named tools as args)
├── run_benchmark.sh             # Run benchmarks (--tools, --skip-existing) + outputs
├── run_single.sh                # Run one tool+dataset, then regenerate outputs
└── generate_outputs.sh          # Reports + comparison + graphs from existing JSONs

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
- `run_benchmark.sh` orchestrates podman-compose execution and generates reports/graphs
- Source files in base image are overridden at runtime: `benchmarks/` and `parsers/` are volume-mounted read-only into containers, so code changes never require image rebuilds
- `uv sync` reads Python version from `requires-python` in pyproject.toml (no --python flag needed)
- Results saved to `results-docker/` for easy comparison with native execution

### Containerization Commands

Benchmarks always run **sequentially** - parallel execution is not supported because concurrent tools would skew each other's measurements.

```bash
# Build all Podman images, or just the named ones
./docker/setup.sh
./docker/setup.sh gmss cimgo    # base built only if missing (--rebuild to force)

# Run all benchmarks in containers (sequential, includes report/graph generation)
./docker/run_benchmark.sh

# Granular runs: subset of tools and/or skip already-benchmarked ones
./docker/run_benchmark.sh --tools triplets,rdflib --skip-existing

# Run single tool-dataset combination (for adding/debugging a tool);
# also regenerates reports/comparison/graphs with ALL existing results included
./docker/run_single.sh triplets svedala
./docker/run_single.sh jena realgrid

# Regenerate reports/comparison/graphs from existing JSONs without running anything
./docker/generate_outputs.sh    # default: results-docker

# Using podman-compose directly
podman-compose -f docker/docker-compose.yml run --rm triplets-svedala  # Single

# Run specific tool via Podman (source mounts REQUIRED - images bake no source)
podman run --rm \
  -v $(pwd)/benchmarks:/benchmarks:ro,z \
  -v $(pwd)/parsers:/benchmarks/parsers:ro,z \
  -v $(pwd)/data:/benchmarks/data:ro,z \
  -v $(pwd)/results-docker:/output:z \
  cim-bench/triplets:latest

# Build specific image
podman build -f docker/tools/triplets.dockerfile -t cim-bench/triplets:latest .
```

**Note**: The `:z` flag in volume mounts enables SELinux relabeling (required on Fedora/RHEL).

**To add a new benchmark:**
1. Create a git branch named after the tool (convention: one branch per tool integration, e.g. `cimgo`, `gmss`); merge to master when validated
2. Create the tool adapter and benchmark files (see "Adding a New Parser")
3. Create `tool-configs/{tool}/pyproject.toml` with dependencies
4. Create `docker/tools/{tool}.dockerfile`
5. Add services to `docker/docker-compose.yml`
6. Build and iterate with a single tool: `./docker/setup.sh {tool}` + `./docker/run_single.sh {tool} svedala` - each run refreshes reports/comparison/graphs with all previously saved results, so there is NO need to rerun the other tools
7. A full `./docker/run_benchmark.sh` rerun is only needed when the *environment* changes (new hardware, OS upgrade), not when adding a tool

**For debugging:** Use `./docker/run_single.sh {tool} {dataset}` to quickly test a specific tool-dataset combination without running the entire benchmark suite. Source is volume-mounted, so code edits take effect without rebuilding images.

**Language bridges** - how non-Python tools are integrated in-process (preferred, enables the full load+query benchmark suite):
- **Java**: JPype/JVM in the tool image (jena, opencgmes, powsybl-cgmes)
- **C++**: pybind11 wrapper compiled in the dockerfile (libcimpp)
- **C#/.NET**: pythonnet hosting CoreCLR + published NuGet DLLs (gmss)
- **Rust**: PyO3/maturin wrapper crate compiled in the dockerfile (the way pyoxigraph wraps Oxigraph; planned for cimoxide)

**CLI-only tools** (no library API, e.g. cimgo, cimd, pocket-rdf) use `benchmarks/cli_benchmark_template.py` instead of the adapter interface: each CLI operation becomes one timed subprocess test with peak-RSS measurement (`parsers/subprocess_memory.py`). Their results are tagged `extra_info["tool_type"] = "cli"` and form a **separate benchmark family**: separate `cli_*.svg` graphs and a separate comparison section, never mixed with in-process library numbers (a subprocess includes full process lifecycle and cannot be compared fairly).

### Container Image Sizes

| Image | Size | Notes |
|-------|------|-------|
| `cim-bench/base` | ~100MB | Debian + uv + system tools |
| `cim-bench/triplets` | ~250MB | Base + Python 3.14 + deps |
| `cim-bench/pypowsybl` | ~450MB | Base + Python 3.13 + JDK 17 + deps |
| `cim-bench/veragrid` | ~300MB | Base + Python 3.14 + deps |
| `cim-bench/cimgraph` | ~350MB | Base + Python 3.14 + rdflib/Oxigraph |
| `cim-bench/rdflib` | ~300MB | Base + Python 3.14 + rdflib/Oxigraph |

**Total disk space**: ~1.75GB (base shared, actual ~1.5GB incremental)

### Validated Performance

Containerized benchmarks validated on Podman 5.7.1 / Fedora 43:

**Load Test Overhead** (Primary Metric):
- **triplets**: +7.66% (acceptable)
- **rdflib**: -48% 🚀 (FASTER in container due to Python 3.14 improvements!)
- **pypowsybl**: +5.95% (acceptable)

All overhead within acceptable range. Python 3.14 provides significant performance benefits.

See `CONTAINERIZATION_VALIDATION.md` for detailed validation results.

## Adding a New Parser

Follow this 3-step pattern:

### 1. Create adapter in `parsers/`

```python
# parsers/cimpy_adapter.py
from parser_adapter import ParserAdapter
from datasets import DATASETS

class CimpyAdapter(ParserAdapter):
    @classmethod
    def get_display_name(cls):
        return "CIMpy"

    @classmethod
    def get_color(cls):
        return "#9b59b6"  # Purple

    @classmethod
    def get_tags(cls):
        return ["parser", "typed-model", "python"]

    def load(self, dataset_key):
        # Load using cimpy
        pass

    def get_load_metrics(self, loaded_obj, memory_mb):
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "lines": self.get_lines_count(loaded_obj),
            # ... other metrics
        }

    def get_lines_count(self, loaded_obj):
        # Query implementation
        pass

    # Implement other required methods...
```

#### Adapter Implementation Guidelines

**CRITICAL: Always load ALL dataset files**
- Load every file in the dataset, not just selected profiles
- Benchmarks measure real-world loading performance, which includes all CGMES profiles
- Never swallow per-file load errors: if the tool cannot load every profile (merged or as separate models), raise `IncompleteLoadError` (from `parser_adapter`) listing the failures — the benchmark template turns it into a pytest skip so partial loads never produce misleading numbers
- If the tool doesn't support merging multiple files into a single graph:
  - Load each file into separate graphs/models
  - Store all loaded graphs (e.g., in a dict: `self.models = {}`)
  - Select the largest profile (usually EQ - Equipment) for queries

**Clean file loading pattern:**
```python
from pathlib import Path
import zipfile
import tempfile

def load(self, dataset_key: str):
    """Load CIM dataset."""
    dataset = DATASETS[dataset_key]

    # Determine files to load
    files = (v for k, v in dataset.items() if "_metadata" not in k.lower())

    # Extract ZIP if needed (only for setting up files variable)
    if "ZIP" in dataset:
        temp_dir = tempfile.TemporaryDirectory()
        tmp = temp_dir.name
        zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
        files = Path(tmp).rglob("*.xml")

    # Load all files (same logic for ZIP and non-ZIP)
    for f in files:
        self.graph.parse(f, format="xml")

    # Cleanup if ZIP was used
    if "ZIP" in dataset:
        temp_dir.cleanup()

    return self
```

**For tools that can't merge files into single graph:**
```python
def load(self, dataset_key: str):
    """Load CIM dataset - separate graph per file."""
    dataset = DATASETS[dataset_key]
    self.models = {}

    # Determine files to load (keep profile names)
    files = [(k, Path(v)) for k, v in dataset.items() if "_metadata" not in k.lower()]

    # Extract ZIP if needed
    if "ZIP" in dataset:
        temp_dir = tempfile.TemporaryDirectory()
        tmp = temp_dir.name
        zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
        files = [(f.stem, f) for f in Path(tmp).rglob("*.xml")]

    # Load all files into separate models
    for profile, path in files:
        self.models[profile] = self.parse_file(path)

    # Select EQ profile for queries (largest, most complete)
    eq_key = next((k for k in self.models.keys() if "EQ" in k), None)
    self.model = self.models[eq_key] if eq_key else list(self.models.values())[0]

    # Cleanup if ZIP was used
    if "ZIP" in dataset:
        temp_dir.cleanup()

    return self
```

**Key patterns:**
- Use `pathlib.Path` for all file operations
- Use generator expressions `(x for x in ...)` for memory efficiency
- Use `.rglob("*.xml")` to recursively find XML files
- Use `if "ZIP" in dataset:` ONLY for: (1) extracting files, (2) cleanup
- Keep loading logic outside if/else - same code path for both cases
- Manual cleanup with `temp_dir.cleanup()` (not context manager `with`)

### 2. Create benchmark files in `benchmarks/`

```python
# benchmarks/cimpy_svedala_benchmark.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimpy_adapter import CimpyAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=CimpyAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="cimpy",
    dataset_name="svedala"
)
```

### 3. Create Podman configuration (optional)

If using Podman, create `tool-configs/cimpy/pyproject.toml`:
```toml
[project]
name = "cim-bench-cimpy"
version = "0.1.0"
requires-python = "==3.14.*"  # Use exact version for reproducibility
dependencies = [
    "cimpy>=1.0.0",
    "pytest>=7.0.0",
    "pytest-benchmark>=4.0.0",
    "psutil>=5.9.0"
]
```

Create `docker/tools/cimpy.dockerfile`:
```dockerfile
FROM cim-bench/base:latest

# Install Python and dependencies via uv sync (reads Python version from pyproject.toml)
WORKDIR /app
COPY tool-configs/cimpy/pyproject.toml .
RUN uv sync

# Source files already in base image
ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /benchmarks

CMD ["pytest", "cimpy_svedala_benchmark.py", "--benchmark-only", \
     "--benchmark-json=/output/cimpy_svedala_benchmark.json"]
```

Add service to `docker/docker-compose.yml`:
```yaml
  cimpy-svedala:
    <<: *common
    image: cim-bench/cimpy:latest
    command: pytest cimpy_svedala_benchmark.py --benchmark-only --benchmark-json=/output/cimpy_svedala_benchmark.json

  cimpy-realgrid:
    <<: *common
    image: cim-bench/cimpy:latest
    command: pytest cimpy_realgrid_benchmark.py --benchmark-only --benchmark-json=/output/cimpy_realgrid_benchmark.json
```

### 4. Run benchmarks

```bash
# Native execution
./run_benchmarks.sh

# Podman execution (if configured)
./docker/setup.sh      # Automatically discovers cimpy from docker-compose.yml
./docker/run_benchmark.sh
```

**That's it!** The script auto-discovers all `benchmarks/*_benchmark.py` files and runs them. Graphs will automatically include the new parser using its display name and color from the JSON reports.

**No configuration needed** - just create the benchmark files and run the script!

## Key Implementation Details

### Benchmark Test Generation

Tests are generated at import time and injected into the module namespace. This allows:
- Custom test names: `test_{parser}_load_{dataset}`
- Fixture sharing: All query tests share the `loaded_object` fixture
- Automatic cleanup: Adapters with `cleanup()` method are called automatically

### Memory Measurement

- Baseline captured before loading: `memory_baseline` fixture
- Delta calculated: `current_memory - baseline_memory`
- Uses `psutil.Process().memory_info().rss`

### Graph Generation (227 lines)

`tools/generate_graphs.py` is fully automatic:
- **`load_benchmarks()`**: Discovers all `*_benchmark.json`, organizes by dataset → tool
- **`plot_dataset()`**: Generates comparison + detailed charts per dataset
- **`plot_cross_dataset()`**: Generates 3 cross-dataset charts (import, memory, query)
- **No configuration needed**: Reads display names and colors from JSON

### Results Structure

**Native execution** (`./run_benchmarks.sh`):
```
results/
├── {parser}_{dataset}_benchmark.json    # Raw pytest-benchmark output
├── {parser}_{dataset}_report.md         # Individual report
├── comparison_summary.md                # Cross-parser comparison
└── graphs/
    ├── import_comparison.svg
    ├── memory_comparison.svg
    ├── query_comparison.svg
    ├── svedala_comparison.svg
    ├── svedala_detailed.svg
    ├── realgrid_comparison.svg
    └── realgrid_detailed.svg
```

**Containerized execution** (`./docker/run_benchmark.sh`):
```
results-docker/
├── {parser}_{dataset}_benchmark.json    # Raw pytest-benchmark output
├── {parser}_{dataset}_report.md         # Individual report
├── comparison_summary.md                # Cross-parser comparison
└── graphs/
    ├── import_comparison.svg
    ├── memory_comparison.svg
    ├── query_comparison.svg
    ├── svedala_comparison.svg
    ├── svedala_detailed.svg
    ├── realgrid_comparison.svg
    └── realgrid_detailed.svg
```

## Git LFS Requirement

Large dataset files are stored using Git LFS:

```bash
git lfs install
git lfs pull
git submodule foreach --recursive git lfs pull
```

## Design Principles

1. **Zero-configuration extensibility**: Adding a parser requires no changes to graph generation or report tooling
2. **Data-driven**: Display metadata (names, colors) flows through JSON reports to all consumers
3. **Single source of truth**: Adapter defines metadata once; benchmark embeds it; tools read it
4. **Dynamic discovery**: Graph generator finds all JSONs automatically—no manual file mapping
5. **Parser isolation**: Each adapter is independent; no shared logic except abstract interface

## Code Style

### Guiding Principles

- **Short and concise, not cryptic** - Prioritize readability over cleverness
- **Logic should fit one screen** (~40-60 lines) - Keep concepts comprehensible at a glance
- **Limited lines > comprehensive features** - This is a benchmarking tool, not production-critical software
- **Let things fail with clear errors** - No defensive exception handling unless truly needed
- **Avoid over-engineering** - Introduce complexity only when needed

### General Patterns

**Prefer flat structures over nested:**
```python
# Good - flat list of dictionaries
tools = [
    {"name": "triplets", "color": "#3498db"},
    {"name": "pypowsybl", "color": "#e74c3c"},
]

# Avoid - nested structure
tools = {
    "triplets": {"color": "#3498db"},
    "pypowsybl": {"color": "#e74c3c"},
}
```

**Use comprehensions for simple operations:**
```python
json_files = [f for f in files if f.endswith(".json")]
colors = [tool_data.get("color", "#999") for tool_data in tools]
```

**Walrus operator for assignment + condition:**
```python
if (display_name := extra.get("display_name")):
    use_display_name(display_name)
```

**Type hints only when helpful:**
```python
# Add if it clarifies without clutter
def load(self, dataset_key: str) -> Any:
    pass

# Skip for obvious cases
def get_color(cls):  # Return type obvious from name
    return "#3498db"
```

### Function Design

**Single responsibility** - Functions do one thing well:
```python
def plot_dataset(dataset_name, tools_data, output_dir):
    """Generate comparison charts for a dataset."""
    # Just plotting logic here
    # Data loading is separate
    # File discovery is separate
```

**Make functions intuitive** - Accept both single items and lists where it makes sense:
```python
def extract_data(benchmark_json):
    # User might pass string or Path
    if isinstance(benchmark_json, str):
        benchmark_json = Path(benchmark_json)
```

**Docstrings with clear return structure:**
```python
def load_benchmarks(results_dir):
    """
    Load all benchmark JSONs and organize by dataset.

    Returns:
        dict: Nested dict organized as data[dataset][tool][metric]
    """
```

**Accumulate results, then concatenate:**
```python
# Good - accumulate then combine
data_list = []
for file in files:
    df = load_data(file)
    data_list.append(df)
return pd.concat(data_list, ignore_index=True)

# Avoid - growing DataFrame in loop
result = pd.DataFrame()
for file in files:
    result = pd.concat([result, load_data(file)])
```

### What to Avoid

**No hardcoded tool names** - Use data from adapters/JSON:
```python
# Bad
if tool == "triplets":
    color = "#3498db"

# Good
color = tool_data.get("color", "#999999")
```

**No complex exception handling** - Let failures be obvious:
```python
# Bad - hiding errors
try:
    value = data["key"]
except KeyError:
    value = None

# Good - let it fail or use .get()
value = data.get("key")  # Only for optional values
value = data["key"]      # For required values - let KeyError happen
```

**No unnecessary classes** - Use functions unless you need state/inheritance:
```python
# Good - simple function
def generate_graph(data, output_path):
    pass

# Avoid - unnecessary class wrapper
class GraphGenerator:
    def generate(self, data, output_path):
        pass
```

**No duplicate logic** - Extract to shared utilities:
```python
# If you find yourself writing similar code twice,
# extract it to a common function/module
```

## Important Files

- `benchmarks/benchmark_template.py` (155 lines): Test generator, embeds display_name/color
- `tools/generate_graphs.py` (227 lines): Fully automatic graph generation from JSON
- `parsers/parser_adapter.py` (62 lines): Abstract interface with display name/color methods
- `run_benchmarks.sh`: Orchestrates benchmark → report → graph pipeline
