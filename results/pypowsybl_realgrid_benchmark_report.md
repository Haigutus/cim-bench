# Benchmark Report

**Generated from**: `results/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.62 s
- **Min time**: 4.56 s
- **Max time**: 4.72 s
- **Std dev**: 87.6 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 3340.1
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

- **Mean time**: 45.1 ms
- **Min time**: 37.1 ms
- **Max time**: 58.0 ms
- **Std dev**: 5.7 ms
- **Rounds**: 24

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 4.2 ms
- **Min time**: 2.7 ms
- **Max time**: 8.1 ms
- **Std dev**: 1.3 ms
- **Rounds**: 143

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 24.4 ms
- **Min time**: 18.2 ms
- **Max time**: 83.2 ms
- **Std dev**: 10.3 ms
- **Rounds**: 37

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 5.9 ms
- **Min time**: 3.9 ms
- **Max time**: 12.2 ms
- **Std dev**: 1.3 ms
- **Rounds**: 123

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
