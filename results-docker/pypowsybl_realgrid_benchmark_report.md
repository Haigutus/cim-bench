# Benchmark Report

**Generated from**: `results-docker/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.57 s
- **Min time**: 4.41 s
- **Max time**: 4.74 s
- **Std dev**: 152.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4801.7
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

- **Mean time**: 35.8 ms
- **Min time**: 34.6 ms
- **Max time**: 38.2 ms
- **Std dev**: 858.1 μs
- **Rounds**: 29

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 2.7 ms
- **Min time**: 2.4 ms
- **Max time**: 6.4 ms
- **Std dev**: 774.4 μs
- **Rounds**: 171

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 20.5 ms
- **Min time**: 16.8 ms
- **Max time**: 70.3 ms
- **Std dev**: 8.3 ms
- **Rounds**: 42

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 4.0 ms
- **Min time**: 3.4 ms
- **Max time**: 9.9 ms
- **Std dev**: 1.0 ms
- **Rounds**: 153

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
