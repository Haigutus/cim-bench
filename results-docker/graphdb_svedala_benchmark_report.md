# Benchmark Report

**Generated from**: `results-docker/graphdb_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Graphdb Load Svedala

- **Mean time**: 818.4 ms
- **Min time**: 734.8 ms
- **Max time**: 972.4 ms
- **Std dev**: 92.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1764.0
- Triples: 84976
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: graphdb
- Library Version: 10.8.14
- Library Dependencies: {'jpype1': '1.7.1', 'java': '21.0.11'}
- Java Version: 21.0.11
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'java']

### Graphdb Get Lines

- **Mean time**: 355.3 μs
- **Min time**: 169.1 μs
- **Max time**: 1.8 ms
- **Std dev**: 213.7 μs
- **Rounds**: 442

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: graphdb
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Generators

- **Mean time**: 116.7 μs
- **Min time**: 62.7 μs
- **Max time**: 24.6 ms
- **Std dev**: 489.1 μs
- **Rounds**: 2559

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: graphdb
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Loads

- **Mean time**: 205.7 μs
- **Min time**: 138.8 μs
- **Max time**: 1.0 ms
- **Std dev**: 53.4 μs
- **Rounds**: 1425

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: graphdb
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Substations

- **Mean time**: 80.5 μs
- **Min time**: 43.8 μs
- **Max time**: 49.1 ms
- **Std dev**: 803.6 μs
- **Rounds**: 4975

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: graphdb
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Export Svedala

- **Mean time**: 187.8 ms
- **Min time**: 180.3 ms
- **Max time**: 193.8 ms
- **Std dev**: 5.2 ms
- **Rounds**: 5

**Metrics**:
- Library: graphdb
- Dataset: svedala
- Operation: export
- Display Name: GraphDB
- Color: #2c3e50
