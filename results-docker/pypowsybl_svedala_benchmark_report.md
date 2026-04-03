# Benchmark Report

**Generated from**: `results-docker/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 419.7 ms
- **Min time**: 401.7 ms
- **Max time**: 437.0 ms
- **Std dev**: 15.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1047.8
- Buses: 105
- Lines: 97
- Ac Lines: 90
- Dangling Lines: 7
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: pypowsybl
- Library Version: 1.14.0
- Library Dependencies: {'prettytable': '3.17.0', 'pandas': '3.0.2', 'networkx': '3.6.1'}
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Lines

- **Mean time**: 284.8 μs
- **Min time**: 271.5 μs
- **Max time**: 503.0 μs
- **Std dev**: 15.4 μs
- **Rounds**: 1162

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 266.9 μs
- **Min time**: 247.7 μs
- **Max time**: 1.5 ms
- **Std dev**: 50.4 μs
- **Rounds**: 1603

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 189.8 μs
- **Min time**: 178.4 μs
- **Max time**: 558.3 μs
- **Std dev**: 15.7 μs
- **Rounds**: 1773

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 121.9 μs
- **Min time**: 112.2 μs
- **Max time**: 969.5 μs
- **Std dev**: 26.5 μs
- **Rounds**: 3562

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Export Svedala

- **Mean time**: 139.0 ms
- **Min time**: 136.1 ms
- **Max time**: 143.2 ms
- **Std dev**: 2.2 ms
- **Rounds**: 8

**Metrics**:
- Library: pypowsybl
- Dataset: svedala
- Operation: export
- Display Name: PyPowSyBl
- Color: #ff7f0e
