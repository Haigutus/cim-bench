# Benchmark Report

**Generated from**: `results/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.51 s
- **Min time**: 4.44 s
- **Max time**: 4.62 s
- **Std dev**: 68.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4754.8
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

- **Mean time**: 38.6 ms
- **Min time**: 33.7 ms
- **Max time**: 54.5 ms
- **Std dev**: 4.1 ms
- **Rounds**: 26

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 3.4 ms
- **Min time**: 2.6 ms
- **Max time**: 9.5 ms
- **Std dev**: 1.2 ms
- **Rounds**: 103

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 19.3 ms
- **Min time**: 17.4 ms
- **Max time**: 22.9 ms
- **Std dev**: 1.4 ms
- **Rounds**: 46

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 4.6 ms
- **Min time**: 3.7 ms
- **Max time**: 20.2 ms
- **Std dev**: 1.5 ms
- **Rounds**: 138

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
