# cim-bench

Performance benchmarking suite for CIM (Common Information Model) parsers and serializers.

### Performance Comparison Graphs

![Import Performance](results-docker/graphs/import_comparison.svg)
![Export Performance](results-docker/graphs/export_comparison.svg)
![Memory Usage](results-docker/graphs/memory_comparison.svg)

## Benchmark Results

Latest containerized results on AMD Ryzen AI 9 HX 370 (24 cores), 64GB RAM, Podman 5.7.1 / Fedora 43:
- Python 3.14.3 for: triplets, rdflib, cimgraph, veragrid, maplib
- Python 3.13.12 for Java tools (JPype): jena, opencgmes, powsybl-cgmes, pypowsybl

### Comparison Summary

**Small Dataset (Svedala - 7.3 MB, CGMES 3.0):**

| Library | Version | Load Time | Memory | Query Speed | Elements |
|---------|---------|-----------|--------|-------------|----------|
| **OpenCGMES** | 1.0.0-SNAPSHOT | 99.6 ms | 427 MB | 129-537 μs | 97 lines, 39 gen, 73 loads, 56 subs |
| **triplets** | 0.0.17 | 132 ms | 43 MB | 25-55 ms | 97 lines, 39 gen, 73 loads, 57 subs |
| **Apache Jena** | 6.0.0 | 147.6 ms | 768 MB | 94-307 μs | 97 lines, 39 gen, 73 loads, 56 subs |
| **PowSyBL CGMES** | 2025.3.1 | 270 ms | 679 MB | 62-159 μs | 97 lines, 39 gen, 73 loads, 57 subs |
| **maplib** | 0.20.0 | 324.9 ms | 176 MB | 362 μs-1.1 ms | 97 lines, 39 gen, 73 loads, 57 subs |
| **pypowsybl** | 1.14.0 | 476 ms | 1,160 MB | 133-300 μs | 97 lines, 39 gen, 73 loads, 57 subs |
| **VeraGrid** | 5.6.38 | 480.7 ms | 450 MB | 0.05-0.1 μs | 97 lines, 39 gen, 73 loads, 56 subs |
| **CIM-Graph** | 0.4.3a12 | 912 ms | 191 MB | 0.07-0.2 μs | 97 lines, 39 gen, 73 loads, 56 subs |
| **RDFlib** | 7.6.0 | 1.59 s | 285 MB | 48-138 μs | 97 lines, 78 gen, 146 loads, 57 subs |

**Large Dataset (RealGrid - 86.5 MB, CGMES 2.4.15):**

| Library | Version | Load Time | Memory | Query Speed | Elements |
|---------|---------|-----------|--------|-------------|----------|
| **OpenCGMES** | 1.0.0-SNAPSHOT | 1.24 s | 5,527 MB | 249 μs-2.5 ms | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **triplets** | 0.0.17 | 1.45 s | 594 MB | 263-655 ms | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **Apache Jena** | 6.0.0 | 1.77 s | 3,938 MB | 359 μs-1.7 ms | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **PowSyBL CGMES** | 2025.3.1 | 1.85 s | 4,224 MB | 221 μs-1.2 ms | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **maplib** | 0.20.0 | 2.43 s | 517 MB | 493 μs-1.3 ms | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **pypowsybl** | 1.14.0 | 4.61 s | 4,497 MB | 2.8-33 ms | 7561 lines, 1347 gen, 6687 loads, 4791* subs |
| **VeraGrid** | 5.6.38 | 6.85 s | 1,315 MB | 0.05-0.2 μs | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **CIM-Graph** | 0.4.3a12 | 12.98 s | 3,254 MB | 0.08-0.2 μs | 7561 lines, 1347 gen, 6687 loads, 4875 subs |
| **RDFlib** | 7.6.0 | 19.13 s | 1,520 MB | 420 μs-2.1 ms | 7561 lines, 2694 gen, 13374 loads, 4875 subs |
| **libcimpp** | 2.2.0 | 23.41 s | 135 MB | 9.4-21.3 ms | 7561 lines, 1347 gen, 6687 loads, 4875 subs |

*pypowsybl converts some substations to voltage levels when connected by transformers, resulting in 84 fewer substations in RealGrid*

**Note:** libcimpp currently only benchmarked on RealGrid (CGMES 2.4.15) due to compatibility issues with CGMES 3.0 European extensions in the Svedala dataset.

> **⚠️ Query Performance Note**: Query times are not directly comparable across parsers. Some parsers (triplets) use `type_tableview()` which retrieves **all element data with parameters**, while others (RDFlib, Jena, OpenCGMES, PowSyBL CGMES) use SPARQL `COUNT()` queries that only return **element counts**. Retrieving full data is 10-100x slower but provides complete element information. Future work will standardize all parsers to retrieve full element data for fair comparison.

### Export Performance

Export benchmarks measure serialization of loaded CIM data back to RDF/XML. Not all tools support export — CIM-Graph and libcimpp lack serialization APIs.

**Small Dataset (Svedala - 7.3 MB, CGMES 3.0):**

| Library | Export Time | Output Format | Notes |
|---------|-----------|---------------|-------|
| **PyPowSyBl** | 139 ms | CGMES ZIP | Fastest exporter, native network dump |
| **PowSyBL CGMES** | 188 ms | RDF/XML (per-profile) | Writes via DirectoryDataSource |
| **OpenCGMES** | 366 ms | RDF/XML (per-profile) | Jena Model.write per profile |
| **Apache Jena** | 435 ms | RDF/XML (per-profile) | Model.write per loaded profile |
| **triplets** | 607 ms | ZIP per profile | CIM XML export with schema mapping |
| **VeraGrid** | 1.08 s | CGMES ZIP | CimExporter with 4 profiles |
| **maplib** | 1.41 s | RDF/XML (single file) | 58 ms with N-Quads (24x faster), RDF/XML serialization is the bottleneck |
| **RDFlib** | 1.60 s | RDF/XML (single file) | Oxigraph graph.serialize() |

**Large Dataset (RealGrid - 86.5 MB, CGMES 2.4.15):**

| Library | Export Time | Output Format | Notes |
|---------|-----------|---------------|-------|
| **PyPowSyBl** | 1.59 s | CGMES ZIP | Fastest, good scaling |
| **PowSyBL CGMES** | 2.11 s | RDF/XML (per-profile) | Scales well |
| **OpenCGMES** | 3.91 s | RDF/XML (per-profile) | Jena-based, consistent performance |
| **Apache Jena** | 4.38 s | RDF/XML (per-profile) | Model.write per loaded profile |
| **triplets** | 5.78 s | ZIP per profile | Parallel export with 4 workers |
| **VeraGrid** | 12.55 s | CGMES ZIP | Slower scaling on large datasets |
| **maplib** | 16.79 s | RDF/XML (single file) | 309 ms with N-Quads (54x faster), RDF/XML serialization is the bottleneck |
| **RDFlib** | 18.69 s | RDF/XML (single file) | Slowest for RDF/XML serialization |

**maplib RDF/XML vs N-Quads**: maplib's default N-Quads export is extremely fast (309 ms for RealGrid) but RDF/XML takes 16.79 s — a 54x slowdown. The benchmark uses RDF/XML for consistency with other tools.

**Import vs Export Speed (RealGrid - 86.5 MB):**

| Library | Import | Export | Ratio |
|---------|--------|--------|-------|
| **PyPowSyBl** | 4.32 s | 1.59 s | 0.37x |
| **RDFlib** | 19.42 s | 18.69 s | 0.96x |
| **PowSyBL CGMES** | 1.75 s | 2.11 s | 1.20x |
| **VeraGrid** | 6.90 s | 12.55 s | 1.82x |
| **Apache Jena** | 1.59 s | 4.38 s | 2.75x |
| **OpenCGMES** | 1.04 s | 3.91 s | 3.77x |
| **triplets** | 1.36 s | 5.78 s | 4.26x |
| **maplib** | 2.18 s | 16.79 s | 7.70x |



*Cross-dataset comparison showing how all ten tools scale from small (7.3 MB) to large (86.5 MB) datasets*

### Detailed Results: Svedala IGM Dataset (7.3 MB, CGMES 3.0)

#### OpenCGMES - Java CGMES Parser
- **Load Time**: 99.6 ms
- **Memory**: 427 MB
- **Backend**: Apache Jena with CGMES optimizations (jpype1 1.6.0)
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 substations
- **Query Performance**: 129-537 μs (SPARQL on Jena)
- **Strengths**: Fast loading, CGMES-specific optimizations, UUID normalization
- **Use Case**: Large file parsing, CGMES validation, production systems

#### Apache Jena - Pure RDF Framework
- **Load Time**: 147.6 ms
- **Memory**: 768 MB
- **Backend**: In-memory RDF triples (jpype1 1.6.0)
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 subs
- **Query Performance**: 94-307 μs (SPARQL queries)
- **Strengths**: Generic RDF, flexible SPARQL, lenient UUID handling
- **Use Case**: RDF processing, semantic web applications, generic CIM/RDF

#### triplets - RDF/Pandas Parser
- **Load Time**: 132 ms
- **Memory**: 43 MB (smallest!)
- **Backend**: pandas DataFrames + lxml
- **Network Elements**: 97 lines, 39 generators, 73 loads, 57 substations
- **Query Performance**: 25-55 ms (DataFrame queries)
- **Strengths**: Minimal memory, simple API, pandas integration
- **Use Case**: Data extraction, batch processing, quick analysis

#### PowSyBL CGMES - Java Triplestore
- **Load Time**: 270 ms
- **Memory**: 679 MB
- **Backend**: RDF4J triplestore
- **Network Elements**: 97 lines, 39 generators, 73 loads, 57 substations
- **Query Performance**: 62-159 μs (SPARQL on RDF4J)
- **Strengths**: Fast queries, robust triplestore, CGMES model
- **Use Case**: CGMES analysis, SPARQL queries, integration with PowSyBl

#### pypowsybl - Power System Network Model
- **Load Time**: 476 ms
- **Memory**: 1,160 MB
- **Backend**: Java native network model
- **Network Elements**: 97 lines, 39 generators, 73 loads, 57 substations
- **Query Performance**: 133-300 μs (DataFrame access)
- **Strengths**: Rich network model, analysis-ready
- **Use Case**: Power flow analysis, TSO applications

#### CIM-Graph - Typed Knowledge Graph
- **Load Time**: 912 ms
- **Memory**: 191 MB
- **Backend**: Oxigraph + typed CIM objects
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 substations
- **Query Performance**: 0.07-0.2 μs 
- **Strengths**: Sub-microsecond queries, modern typed API, CIM object model
- **Use Case**: Research, development, CIM data exploration

#### maplib - Rust-backed RDF Library
- **Load Time**: 324.9 ms
- **Memory**: 176 MB
- **Backend**: Oxigraph (Rust) + Polars DataFrames (v0.20.0)
- **Network Elements**: 97 lines, 39 generators, 73 loads, 57 substations
- **Query Performance**: 362 μs-1.1 ms (SPARQL with Polars output)
- **Strengths**: Rust performance, sub-millisecond queries, returns DataFrames
- **Use Case**: High-performance RDF processing, data analysis pipelines

#### VeraGrid - GridCal CGMES Parser
- **Load Time**: 480.7 ms
- **Memory**: 450 MB
- **Backend**: Custom CGMES parser (v5.6.38)
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 substations
- **Query Performance**: 0.05-0.1 μs (O(1) list access) (fastest queries!)
- **Strengths**: Fastest queries, direct CGMES object access
- **Use Case**: GridCal power systems analysis, query-intensive workflows

#### RDFlib - Generic RDF Parser
- **Load Time**: 1.59 s
- **Memory**: 285 MB
- **Backend**: Oxigraph via oxrdflib
- **Network Elements**: 97 lines, 78 generators, 146 loads, 57 substations
- **Query Performance**: 48-138 μs (SPARQL on Oxigraph)
- **Strengths**: Standard RDF library, flexible SPARQL, Python 3.14 optimized
- **Use Case**: RDF/SPARQL queries, semantic web applications

### Detailed Results: RealGrid Dataset (86.5 MB, CGMES 2.4.15)

#### OpenCGMES - Java CGMES Parser
- **Load Time**: 1.24 s
- **Memory**: 5,527 MB
- **Backend**: Apache Jena with CGMES optimizations (jpype1 1.6.0)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 249 μs-2.5 ms (SPARQL on Jena)
- **Strengths**: Fast large file loading, CGMES-specific, UUID normalization
- **Use Case**: Production systems, large TSO networks, CGMES validation

#### triplets - RDF/Pandas Parser
- **Load Time**: 1.45 s (fastest!)
- **Memory**: 594 MB (smallest!)
- **Backend**: pandas DataFrames + lxml
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 263-655 ms (DataFrame queries)
- **Strengths**: Low memory, good scaling, simple API
- **Use Case**: Large-scale data processing, European grid analysis

#### Apache Jena - Pure RDF Framework
- **Load Time**: 1.77 s
- **Memory**: 3,938 MB
- **Backend**: In-memory RDF triples (jpype1 1.6.0)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 359 μs-1.7 ms (SPARQL queries)
- **Strengths**: Generic RDF, flexible, lenient UUID handling
- **Use Case**: RDF processing, generic CIM/RDF applications

#### PowSyBL CGMES - Java Triplestore
- **Load Time**: 1.85 s
- **Memory**: 4,224 MB
- **Backend**: RDF4J triplestore
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 221 μs-1.2 ms (SPARQL on RDF4J)
- **Strengths**: Fast queries, robust triplestore
- **Use Case**: CGMES analysis with SPARQL, PowSyBl integration

#### pypowsybl - Power System Network Model
- **Load Time**: 4.61 s
- **Memory**: 4,497 MB
- **Backend**: Java native network model
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4791* substations
- **Query Performance**: 2.8-33 ms (DataFrame access)
- **Strengths**: Comprehensive network model, analysis-ready
- **Use Case**: Power flow analysis, large TSO networks
- **Note**: *Converts some substations to voltage levels (84 fewer)

#### maplib - Rust-backed RDF Library
- **Load Time**: 2.43 s
- **Memory**: 517 MB
- **Backend**: Oxigraph (Rust) + Polars DataFrames (v0.20.0)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 493 μs-1.3 ms (SPARQL with Polars output)
- **Strengths**: Excellent Rust-backed performance, DataFrames output
- **Use Case**: Large-scale RDF processing, high-performance data pipelines

#### VeraGrid - GridCal CGMES Parser
- **Load Time**: 6.85 s
- **Memory**: 1,315 MB
- **Backend**: Custom CGMES parser (v5.6.38)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 0.05-0.2 μs (O(1) list access) (fastest queries!)
- **Strengths**: Fastest queries, direct CGMES object access, improved load performance
- **Use Case**: GridCal integration, query-intensive workflows

#### CIM-Graph - Typed Knowledge Graph
- **Load Time**: 12.98 s
- **Memory**: 3,254 MB
- **Backend**: Oxigraph + typed CIM objects
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 0.08-0.2 μs
- **Strengths**: Sub-microsecond queries, modern typed API
- **Use Case**: Research, rapid queries on loaded data

#### RDFlib - Generic RDF Parser
- **Load Time**: 19.13 s
- **Memory**: 1,520 MB
- **Backend**: Oxigraph via oxrdflib
- **Network Elements**: 7561 lines, 2694 generators, 13374 loads, 4875 substations
- **Query Performance**: 420 μs-2.1 ms (SPARQL on Oxigraph)
- **Strengths**: Standard RDF, flexible SPARQL, Python 3.14 optimized
- **Use Case**: RDF/SPARQL queries, semantic web applications

#### libcimpp - C++ Object Model
- **Load Time**: 23.41 s
- **Memory**: 135 MB (lowest!)
- **Backend**: Native C++ object model
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4875 substations
- **Query Performance**: 9.4-21.3 ms (C++ object iteration)
- **Strengths**: Lowest memory footprint, native C++ performance for queries
- **Use Case**: Memory-constrained environments, C++ integration
- **Limitation**: CGMES 3.0 support incomplete (fails on Svedala with European extensions)


See `tools/*/README.md` for detailed per-tool documentation and analysis.

## Planned Test Additions

## Parsers/Serializers

| Status | Tool / Library | Version | Language | Main Purpose / Strength | Triplet / Graph Access? | CGMES / CIM Support | GitHub / Source | Notes |
|--------|----------------|---------|----------|-------------------------|------------------------|---------------------|-----------------|-------|
| ✅ | **triplets** | 0.0.17 | Python | Pandas-based RDF parser | pandas DataFrames + lxml | Version-agnostic CIM/CGMES | [triplets](https://github.com/Haigutus/triplets) | Fast loading, low memory, simple API |
| ✅ | **pypowsybl** | 1.14.0 | Python | PowSyBl wrapper (network import/export) | Native network model (Java) | CGMES 2.4.15/3.0 CGMES import/export | [powsybl/pypowsybl](https://github.com/powsybl/pypowsybl) | Grid-analysis oriented; rich network model |
| ✅ | **GridCal/VeraGrid** | 5.6.38 | Python | Power systems analysis with UI | Custom CGMES parser | CGMES 2.4.15/3.0 import | [SanPen/GridCal](https://github.com/SanPen/GridCal) | Sub-microsecond queries, full circuit model, improved load performance |
| ✅ | **RDFlib** | 7.6.0 | Python | Generic RDF parser/triple store | Oxigraph (via oxrdflib 0.5.0) | None (generic) | [RDFLib/rdflib](https://github.com/RDFLib/rdflib) | Baseline for speed/memory comparison with Oxigraph |
| ✅ | **CIMantic Graphs** | 0.4.3a12 | Python | In-memory labeled property graph | Oxigraph + typed objects | CIM15–18, custom profiles | [PNNL-CIM-Tools/CIM-Graph](https://github.com/PNNL-CIM-Tools/CIM-Graph) | Modern API, uses RDFlib with typed CIM objects |
| ✅ | **Apache Jena** | 6.0.0 (jpype1 1.6.0) | Java (JPype) | RDF framework + CIMXML parser | In-memory RDF triples | Generic RDF | [apache/jena](https://github.com/apache/jena) | Pure Jena with lenient UUID handling |
| ✅ | **OpenCGMES** | latest (jpype1 1.6.0) | Java (JPype) | Suite for CGMES / CIM RDF parser | Apache Jena (optimized) | CGMES / IEC61970-552 | [SOPTIM/OpenCGMES](https://github.com/SOPTIM/OpenCGMES) | CGMES-specific optimizations, UUID normalization |
| ✅ | **PowSyBL CGMES** | 2025.3.1 | Java (JPype) | CGMES model with triplestore | RDF4J triplestore | CGMES 2.4.15/3.0 | [powsybl/powsybl-core](https://github.com/powsybl/powsybl-core) | CGMES model with SPARQL queries |
| ✅ | **maplib** | 0.20.0 | Python/Rust | High-performance RDF with SPARQL | Polars DataFrames + Oxigraph | Generic RDF (CGMES compatible) | [DataTreehouse/maplib](https://github.com/DataTreehouse/maplib) | Rust-backed performance, sub-millisecond queries |
| ⚠️ | **libcimpp** | 2.2.0 | C++ (Python wrapper) | Fast C++ object model | Native C++ objects | CGMES 2.4.15 (3.0 partial) | [sogno-platform/libcimpp](https://github.com/sogno-platform/libcimpp) | Lowest memory usage (135 MB), CGMES 3.0 fails on Svedala (European extensions) |
| ⚠️ | **cimpy** | 1.1.0 | Python | Import/export/modify CGMES XML/RDF | Object topology dict | CGMES 2.4.15 (partial) | [sogno-platform/cimpy](https://github.com/sogno-platform/cimpy) | Compatibility issues: v1.1.0 only has cgmes_v2_4_15 classes (no CGMES 3.0), parsing bugs with test datasets |
| ❌ | **pycgmes** | latest | Python | Dataclasses + RDF schema + SHACL | Dataclass mapping | CGMES 3.0+ | [alliander-opensource/pycgmes](https://github.com/alliander-opensource/pycgmes) | No file import capability - dataclass definitions only |
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
- Within each dataset, tools sorted from fastest/smallest to slowest/largest
- Independent x-axis scales per dataset for better readability (log scale for query performance)
- Color palette: triplets (blue), rdflib (yellow), pypowsybl (green), cimgraph (red), veragrid (pink), jena (purple), opencgmes (brown), powsybl-cgmes (cyan), maplib (saddle brown), libcimpp (gray)

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
│   ├── rdflib.dockerfile        # Install deps (Python 3.14)
│   ├── maplib.dockerfile        # Install deps (Python 3.14)
│   ├── jena.dockerfile          # Install deps + Java (Python 3.13)
│   ├── opencgmes.dockerfile     # Install deps + Java (Python 3.13)
│   ├── powsybl-cgmes.dockerfile # Install deps + Java (Python 3.13)
│   ├── libcimpp-cgmes24.dockerfile  # C++ build for CGMES 2.4.15
│   └── libcimpp-cgmes3.dockerfile   # C++ build for CGMES 3.0
├── docker-compose.yml           # Single source of truth for benchmarks
├── setup.sh                     # Build all images (reads docker-compose.yml)
└── run_benchmark.sh             # Run benchmarks + generate reports/graphs

tool-configs/
├── triplets/pyproject.toml      # Python ==3.14.* + dependencies
├── pypowsybl/pyproject.toml     # Python ==3.13.* + dependencies
├── veragrid/pyproject.toml      # Python ==3.14.* + dependencies
├── cimgraph/pyproject.toml      # Python ==3.14.* + dependencies
├── rdflib/pyproject.toml        # Python ==3.14.* + dependencies
├── maplib/pyproject.toml        # Python ==3.14.* + dependencies
├── jena/pyproject.toml          # Python ==3.13.* + dependencies
├── opencgmes/pyproject.toml     # Python ==3.13.* + dependencies
├── powsybl-cgmes/pyproject.toml # Python ==3.13.* + dependencies
└── libcimpp/pyproject.toml      # Python ==3.14.* + CMake/C++ build
```

**Key Design:**
- `docker-compose.yml` is the single source of truth for benchmarks
- `tool-configs/*/pyproject.toml` is the single source of truth for Python versions and dependencies
- `setup.sh` dynamically discovers tools from docker-compose.yml
- Source files in base image, tool images only install dependencies
- Results saved to `results-docker/` for easy comparison with native execution

#### Quick Start
```bash
# Build all Podman images (or just some: ./docker/setup.sh gmss cimgo)
./docker/setup.sh

# Run all benchmarks in containers (sequential, includes report/graph generation)
./docker/run_benchmark.sh

# Run a subset of tools, skip already-benchmarked ones
./docker/run_benchmark.sh --tools triplets,rdflib --skip-existing

# Run a single tool+dataset (also refreshes reports/graphs with all prior results)
./docker/run_single.sh triplets svedala

# Regenerate reports/comparison/graphs without running anything
./docker/generate_outputs.sh
```

Benchmarks always run **sequentially** - parallel execution would let tools
skew each other's measurements. Source directories are volume-mounted into
the containers, so code changes don't require image rebuilds.

#### Container Image Sizes
- **Base**: ~100MB (Debian + uv + system tools)
- **triplets**: ~250MB (Base + Python 3.14 + deps)
- **pypowsybl**: ~450MB (Base + Python 3.13 + JDK 17 + deps)
- **veragrid**: ~300MB (Base + Python 3.14 + deps)
- **cimgraph**: ~350MB (Base + Python 3.14 + rdflib/Oxigraph)
- **rdflib**: ~300MB (Base + Python 3.14 + rdflib/Oxigraph)
- **maplib**: ~350MB (Base + Python 3.14 + Rust libs + Polars)
- **jena**: ~500MB (Base + Python 3.13 + JDK + Jena)
- **opencgmes**: ~550MB (Base + Python 3.13 + JDK + OpenCGMES)
- **powsybl-cgmes**: ~500MB (Base + Python 3.13 + JDK + PowSyBL)
- **libcimpp**: ~400MB (Base + Python 3.14 + CMake + C++ toolchain + libcimpp)

**Total disk space**: ~4GB (base shared across all images)

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
