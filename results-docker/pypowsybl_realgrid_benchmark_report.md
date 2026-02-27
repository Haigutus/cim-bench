# Benchmark Report

**Generated from**: `results-docker/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.29 s
- **Min time**: 4.21 s
- **Max time**: 4.42 s
- **Std dev**: 91.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4012.8
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

- **Mean time**: 33.2 ms
- **Min time**: 32.1 ms
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

- **Mean time**: 2.6 ms
- **Min time**: 2.3 ms
- **Max time**: 16.8 ms
- **Std dev**: 1.0 ms
- **Rounds**: 216

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 18.8 ms
- **Min time**: 17.5 ms
- **Max time**: 21.2 ms
- **Std dev**: 823.3 μs
- **Rounds**: 48

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 4.1 ms
- **Min time**: 3.5 ms
- **Max time**: 11.0 ms
- **Std dev**: 812.0 μs
- **Rounds**: 148

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
