# Benchmark Report

**Generated from**: `results-docker/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.24 s
- **Min time**: 4.18 s
- **Max time**: 4.29 s
- **Std dev**: 43.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2089.0
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
- Library Version: 1.15.0
- Library Dependencies: {'prettytable': '3.18.0', 'pandas': '3.0.3', 'networkx': '3.6.1'}
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
- Tags: ['parser', 'serializer', 'query', 'powerflow-tool', 'python', 'java']

### Pypowsybl Get Lines

- **Mean time**: 33.2 ms
- **Min time**: 29.6 ms
- **Max time**: 52.3 ms
- **Std dev**: 3.8 ms
- **Rounds**: 30

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 2.2 ms
- **Min time**: 2.1 ms
- **Max time**: 3.5 ms
- **Std dev**: 137.6 μs
- **Rounds**: 232

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 16.1 ms
- **Min time**: 15.0 ms
- **Max time**: 16.9 ms
- **Std dev**: 330.5 μs
- **Rounds**: 53

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 3.5 ms
- **Min time**: 3.2 ms
- **Max time**: 24.2 ms
- **Std dev**: 1.7 ms
- **Rounds**: 156

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Export Realgrid

- **Mean time**: 1.55 s
- **Min time**: 1.53 s
- **Max time**: 1.56 s
- **Std dev**: 10.5 ms
- **Rounds**: 5

**Metrics**:
- Library: pypowsybl
- Dataset: realgrid
- Operation: export
- Display Name: PyPowSyBl
- Color: #ff7f0e
