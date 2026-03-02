# Benchmark Report

**Generated from**: `results-docker/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.61 s
- **Min time**: 4.46 s
- **Max time**: 4.71 s
- **Std dev**: 90.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4496.6
- Buses: 6051
- Lines: 7561
- Ac Lines: 7561
- Dangling Lines: 0
- Generators: 1347
- Loads: 6687
- Substations: 4791
- Dataset Size Mb: 86.5
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Lines

- **Mean time**: 33.1 ms
- **Min time**: 32.0 ms
- **Max time**: 36.7 ms
- **Std dev**: 1.1 ms
- **Rounds**: 29

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 2.8 ms
- **Min time**: 2.3 ms
- **Max time**: 22.3 ms
- **Std dev**: 1.4 ms
- **Rounds**: 213

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 20.2 ms
- **Min time**: 18.4 ms
- **Max time**: 30.8 ms
- **Std dev**: 3.0 ms
- **Rounds**: 44

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 3.9 ms
- **Min time**: 3.3 ms
- **Max time**: 15.0 ms
- **Std dev**: 1.0 ms
- **Rounds**: 148

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
