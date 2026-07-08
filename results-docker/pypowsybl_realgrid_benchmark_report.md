# Benchmark Report

**Generated from**: `results-docker/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 11.69 s
- **Min time**: 10.92 s
- **Max time**: 12.24 s
- **Std dev**: 562.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 7619.7
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

- **Mean time**: 72.8 ms
- **Min time**: 47.0 ms
- **Max time**: 90.3 ms
- **Std dev**: 14.2 ms
- **Rounds**: 17

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 9.0 ms
- **Min time**: 5.4 ms
- **Max time**: 16.9 ms
- **Std dev**: 2.3 ms
- **Rounds**: 97

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 40.5 ms
- **Min time**: 30.2 ms
- **Max time**: 52.6 ms
- **Std dev**: 6.5 ms
- **Rounds**: 20

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 13.1 ms
- **Min time**: 8.4 ms
- **Max time**: 20.6 ms
- **Std dev**: 3.0 ms
- **Rounds**: 60

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Export Realgrid

- **Mean time**: 2.65 s
- **Min time**: 1.94 s
- **Max time**: 4.43 s
- **Std dev**: 1.07 s
- **Rounds**: 5

**Metrics**:
- Library: pypowsybl
- Dataset: realgrid
- Operation: export
- Display Name: PyPowSyBl
- Color: #ff7f0e
