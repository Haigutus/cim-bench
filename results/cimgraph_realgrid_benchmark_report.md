# Benchmark Report

**Generated from**: `results/cimgraph_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Cimgraph Load Realgrid

- **Mean time**: 12.46 s
- **Min time**: 11.50 s
- **Max time**: 13.29 s
- **Std dev**: 904.2 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 1478.5
- Triples: 1075523
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
- **Max time**: 4.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 162549

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Generators

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.6 μs
- **Std dev**: 0.0 μs
- **Rounds**: 88402

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
- **Max time**: 27.0 μs
- **Std dev**: 0.1 μs
- **Rounds**: 152370

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Substations

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.5 μs
- **Std dev**: 0.0 μs
- **Rounds**: 95329

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd
