# Benchmark Report

**Generated from**: `results-docker/graphdb_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Graphdb Load Realgrid

- **Mean time**: 5.60 s
- **Min time**: 5.50 s
- **Max time**: 5.96 s
- **Std dev**: 199.4 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2457.4
- Triples: 1080282
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: graphdb
- Library Version: 10.8.14
- Library Dependencies: {'jpype1': '1.7.1', 'java': '21.0.11'}
- Java Version: 21.0.11
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'java']

### Graphdb Get Lines

- **Mean time**: 252.1 ms
- **Min time**: 243.8 ms
- **Max time**: 263.7 ms
- **Std dev**: 8.0 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: graphdb
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Generators

- **Mean time**: 409.6 μs
- **Min time**: 231.4 μs
- **Max time**: 10.5 ms
- **Std dev**: 453.8 μs
- **Rounds**: 616

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: graphdb
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Loads

- **Mean time**: 1.2 ms
- **Min time**: 918.6 μs
- **Max time**: 50.4 ms
- **Std dev**: 2.1 ms
- **Rounds**: 623

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: graphdb
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Substations

- **Mean time**: 718.6 μs
- **Min time**: 604.8 μs
- **Max time**: 11.3 ms
- **Std dev**: 567.2 μs
- **Rounds**: 1231

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: graphdb
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Export Realgrid

- **Mean time**: 1.95 s
- **Min time**: 1.93 s
- **Max time**: 1.96 s
- **Std dev**: 10.7 ms
- **Rounds**: 5

**Metrics**:
- Library: graphdb
- Dataset: realgrid
- Operation: export
- Display Name: GraphDB
- Color: #2c3e50
