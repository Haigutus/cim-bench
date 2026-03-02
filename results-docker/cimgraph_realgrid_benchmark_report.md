# Benchmark Report

**Generated from**: `results-docker/cimgraph_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Cimgraph Load Realgrid

- **Mean time**: 12.98 s
- **Min time**: 11.89 s
- **Max time**: 14.32 s
- **Std dev**: 1.04 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3254.1
- Triples: 1233106
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Lines

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 57.3 μs
- **Std dev**: 0.2 μs
- **Rounds**: 142389

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
- **Max time**: 53.4 μs
- **Std dev**: 0.3 μs
- **Rounds**: 157679

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Loads

- **Mean time**: 0.2 μs
- **Min time**: 0.1 μs
- **Max time**: 9.2 μs
- **Std dev**: 0.0 μs
- **Rounds**: 191571

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
- **Max time**: 100.2 μs
- **Std dev**: 0.3 μs
- **Rounds**: 173281

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd
