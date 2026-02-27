# Benchmark Report

**Generated from**: `results-docker/cimgraph_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Cimgraph Load Svedala

- **Mean time**: 342.6 ms
- **Min time**: 286.8 ms
- **Max time**: 400.9 ms
- **Std dev**: 42.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 126.9
- Triples: 51893
- Lines: 97
- Generators: 39
- Loads: 0
- Substations: 56
- Total Size Mb: 7.3
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Lines

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.4 μs
- **Std dev**: 0.0 μs
- **Rounds**: 98242

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Generators

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 94707

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Loads

- **Mean time**: 0.2 μs
- **Min time**: 0.1 μs
- **Max time**: 5.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 135429

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Substations

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.5 μs
- **Std dev**: 0.0 μs
- **Rounds**: 90736

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd
