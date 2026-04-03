# Benchmark Report

**Generated from**: `results-docker/cimgraph_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Cimgraph Load Realgrid

- **Mean time**: 13.42 s
- **Min time**: 12.18 s
- **Max time**: 14.78 s
- **Std dev**: 1.10 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3259.2
- Triples: 1233106
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: cimgraph
- Library Version: 0.4.3a12
- Library Dependencies: {'defusedxml': '0.8.0rc2', 'gridappsd-python': '2026.2.1', 'mermaid-python': '0.1', 'mysql-connector-python': '9.6.0', 'neo4j': '6.1.0', 'nest-asyncio': '1.6.0', 'oxrdflib': '0.5.0', 'pint': '0.25.3', 'rdflib': '7.6.0', 'sparqlwrapper': '2.0.0'}
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Lines

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 30.6 μs
- **Std dev**: 0.1 μs
- **Rounds**: 158932

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
- **Max time**: 0.4 μs
- **Std dev**: 0.0 μs
- **Rounds**: 70842

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
- **Max time**: 5.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 101431

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
- **Max time**: 0.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 68134

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd
