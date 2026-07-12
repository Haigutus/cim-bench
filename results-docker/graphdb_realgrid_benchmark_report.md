# Benchmark Report

**Generated from**: `results-docker/graphdb_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Graphdb Load Realgrid

- **Mean time**: 5.86 s
- **Min time**: 5.81 s
- **Max time**: 5.98 s
- **Std dev**: 67.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1050.8
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

- **Mean time**: 1.8 ms
- **Min time**: 1.1 ms
- **Max time**: 18.1 ms
- **Std dev**: 1.2 ms
- **Rounds**: 270

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: graphdb
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Generators

- **Mean time**: 319.1 μs
- **Min time**: 205.3 μs
- **Max time**: 60.5 ms
- **Std dev**: 1.4 ms
- **Rounds**: 2080

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: graphdb
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Loads

- **Mean time**: 1.1 ms
- **Min time**: 879.6 μs
- **Max time**: 15.4 ms
- **Std dev**: 762.2 μs
- **Rounds**: 723

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: graphdb
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Get Substations

- **Mean time**: 876.5 μs
- **Min time**: 605.7 μs
- **Max time**: 15.4 ms
- **Std dev**: 664.9 μs
- **Rounds**: 1268

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: graphdb
- Dataset: realgrid
- Display Name: GraphDB
- Color: #2c3e50

### Graphdb Export Realgrid

- **Mean time**: 2.06 s
- **Min time**: 1.98 s
- **Max time**: 2.25 s
- **Std dev**: 108.5 ms
- **Rounds**: 5

**Metrics**:
- Library: graphdb
- Dataset: realgrid
- Operation: export
- Display Name: GraphDB
- Color: #2c3e50
