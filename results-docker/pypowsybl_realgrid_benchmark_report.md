# Benchmark Report

**Generated from**: `results-docker/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 9.86 s
- **Min time**: 8.82 s
- **Max time**: 10.83 s
- **Std dev**: 840.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 6201.0
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

- **Mean time**: 51.9 ms
- **Min time**: 43.5 ms
- **Max time**: 63.4 ms
- **Std dev**: 5.9 ms
- **Rounds**: 16

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 6.8 ms
- **Min time**: 4.4 ms
- **Max time**: 11.3 ms
- **Std dev**: 1.7 ms
- **Rounds**: 129

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 31.6 ms
- **Min time**: 24.7 ms
- **Max time**: 46.3 ms
- **Std dev**: 5.7 ms
- **Rounds**: 30

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 10.4 ms
- **Min time**: 8.1 ms
- **Max time**: 15.2 ms
- **Std dev**: 1.6 ms
- **Rounds**: 103

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Export Realgrid

- **Mean time**: 3.88 s
- **Min time**: 3.52 s
- **Max time**: 4.20 s
- **Std dev**: 286.3 ms
- **Rounds**: 5

**Metrics**:
- Library: pypowsybl
- Dataset: realgrid
- Operation: export
- Display Name: PyPowSyBl
- Color: #ff7f0e
