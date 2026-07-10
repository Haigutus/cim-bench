# Benchmark Report

**Generated from**: `results-docker/cimgraph_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Cimgraph Load Svedala

- **Mean time**: 1.51 s
- **Min time**: 1.31 s
- **Max time**: 1.86 s
- **Std dev**: 228.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 179.1
- Triples: 66724
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: cimgraph
- Library Version: 0.4.3a12
- Library Dependencies: {'defusedxml': '0.8.0rc2', 'gridappsd-python': '2026.2.1', 'mermaid-python': '0.1', 'mysql-connector-python': '9.7.0', 'neo4j': '6.2.0', 'nest-asyncio': '1.6.0', 'oxrdflib': '0.5.0', 'pint': '0.25.3', 'rdflib': '7.6.0', 'sparqlwrapper': '2.0.0'}
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd
- Tags: ['parser', 'query', 'typed-model', 'triplestore', 'python']

### Cimgraph Get Lines

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 3.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 193837

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Generators

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 0.4 μs
- **Std dev**: 0.0 μs
- **Rounds**: 75959

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Loads

- **Mean time**: 0.2 μs
- **Min time**: 0.2 μs
- **Max time**: 11.0 μs
- **Std dev**: 0.1 μs
- **Rounds**: 98146

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Substations

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 0.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 73497

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Export Svedala

- **Mean time**: 645.6 ms
- **Min time**: 637.1 ms
- **Max time**: 652.1 ms
- **Std dev**: 6.2 ms
- **Rounds**: 5

**Metrics**:
- Library: cimgraph
- Dataset: svedala
- Operation: export
- Display Name: CIM-Graph
- Color: #9467bd
