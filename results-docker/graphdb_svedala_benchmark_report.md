# Benchmark Report

**Generated from**: `results-docker/graphdb_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Graphdb Load Svedala

- **Mean time**: 712.3 ms
- **Min time**: 659.1 ms
- **Max time**: 875.7 ms
- **Std dev**: 91.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1344.3
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

- **Mean time**: 5.9 ms
- **Min time**: 3.7 ms
- **Max time**: 53.3 ms
- **Std dev**: 5.2 ms
- **Rounds**: 99

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: graphdb
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Generators

- **Mean time**: 137.9 μs
- **Min time**: 62.7 μs
- **Max time**: 11.3 ms
- **Std dev**: 343.4 μs
- **Rounds**: 1155

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: graphdb
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Loads

- **Mean time**: 288.6 μs
- **Min time**: 140.0 μs
- **Max time**: 65.3 ms
- **Std dev**: 1.9 ms
- **Rounds**: 1145

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: graphdb
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Substations

- **Mean time**: 82.4 μs
- **Min time**: 36.9 μs
- **Max time**: 60.0 ms
- **Std dev**: 1.1 ms
- **Rounds**: 5347

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: graphdb
- Dataset: svedala
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Export Svedala

- **Mean time**: 191.8 ms
- **Min time**: 178.8 ms
- **Max time**: 221.8 ms
- **Std dev**: 17.1 ms
- **Rounds**: 5

**Metrics**:
- Library: graphdb
- Dataset: svedala
- Operation: export
- Display Name: GraphDB
- Color: #2c3e50
