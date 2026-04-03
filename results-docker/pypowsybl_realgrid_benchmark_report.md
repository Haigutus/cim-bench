# Benchmark Report

**Generated from**: `results-docker/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.32 s
- **Min time**: 4.22 s
- **Max time**: 4.44 s
- **Std dev**: 80.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1640.2
- Buses: 6051
- Lines: 7561
- Ac Lines: 7561
- Dangling Lines: 0
- Generators: 1347
- Loads: 6687
- Substations: 4791
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: pypowsybl
- Library Version: 1.14.0
- Library Dependencies: {'prettytable': '3.17.0', 'pandas': '3.0.2', 'networkx': '3.6.1'}
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Lines

- **Mean time**: 36.4 ms
- **Min time**: 33.0 ms
- **Max time**: 44.5 ms
- **Std dev**: 3.5 ms
- **Rounds**: 31

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 2.7 ms
- **Min time**: 2.2 ms
- **Max time**: 17.2 ms
- **Std dev**: 1.2 ms
- **Rounds**: 223

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 21.3 ms
- **Min time**: 17.7 ms
- **Max time**: 33.8 ms
- **Std dev**: 4.4 ms
- **Rounds**: 53

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 4.5 ms
- **Min time**: 3.3 ms
- **Max time**: 11.6 ms
- **Std dev**: 1.6 ms
- **Rounds**: 122

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Export Realgrid

- **Mean time**: 1.59 s
- **Min time**: 1.57 s
- **Max time**: 1.62 s
- **Std dev**: 19.2 ms
- **Rounds**: 5

**Metrics**:
- Library: pypowsybl
- Dataset: realgrid
- Operation: export
- Display Name: PyPowSyBl
- Color: #ff7f0e
