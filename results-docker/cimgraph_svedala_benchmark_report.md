# Benchmark Report

**Generated from**: `results-docker/cimgraph_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Cimgraph Load Svedala

- **Mean time**: 909.0 ms
- **Min time**: 830.0 ms
- **Max time**: 1.03 s
- **Std dev**: 82.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 204.8
- Triples: 66724
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Total Size Mb: 7.3
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Lines

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 0.2 μs
- **Std dev**: 0.0 μs
- **Rounds**: 74544

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
- **Max time**: 0.5 μs
- **Std dev**: 0.0 μs
- **Rounds**: 73769

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
- **Max time**: 26.4 μs
- **Std dev**: 0.1 μs
- **Rounds**: 137476

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
- **Max time**: 2.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 67944

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd
