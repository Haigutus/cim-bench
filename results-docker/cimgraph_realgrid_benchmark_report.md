# Benchmark Report

**Generated from**: `results-docker/cimgraph_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Cimgraph Load Realgrid

- **Mean time**: 34.65 s
- **Min time**: 17.65 s
- **Max time**: 55.87 s
- **Std dev**: 16.70 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2608.4
- Triples: 1233106
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: cimgraph
- Library Version: 0.4.3a12
- Library Dependencies: {'defusedxml': '0.8.0rc2', 'gridappsd-python': '2026.2.1', 'mermaid-python': '0.1', 'mysql-connector-python': '9.7.0', 'neo4j': '6.2.0', 'nest-asyncio': '1.6.0', 'oxrdflib': '0.5.0', 'pint': '0.25.3', 'rdflib': '7.6.0', 'sparqlwrapper': '2.0.0'}
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd
- Tags: ['parser', 'query', 'typed-model', 'triplestore', 'python']

### Cimgraph Get Lines

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 19.7 μs
- **Std dev**: 0.1 μs
- **Rounds**: 171205

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Generators

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 1.0 μs
- **Std dev**: 0.0 μs
- **Rounds**: 77610

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Loads

- **Mean time**: 0.2 μs
- **Min time**: 0.2 μs
- **Max time**: 27.7 μs
- **Std dev**: 0.1 μs
- **Rounds**: 120701

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Substations

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 9.0 μs
- **Std dev**: 0.0 μs
- **Rounds**: 61767

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd
