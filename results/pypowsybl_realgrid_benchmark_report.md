# Benchmark Report

**Generated from**: `results/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.88 s
- **Min time**: 4.81 s
- **Max time**: 4.98 s
- **Std dev**: 75.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1266.1
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

- **Mean time**: 39.3 ms
- **Min time**: 35.8 ms
- **Max time**: 56.6 ms
- **Std dev**: 4.3 ms
- **Rounds**: 27

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 3.3 ms
- **Min time**: 2.8 ms
- **Max time**: 9.1 ms
- **Std dev**: 851.4 μs
- **Rounds**: 199

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 20.7 ms
- **Min time**: 18.7 ms
- **Max time**: 33.3 ms
- **Std dev**: 2.6 ms
- **Rounds**: 47

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 5.7 ms
- **Min time**: 4.5 ms
- **Max time**: 15.8 ms
- **Std dev**: 1.9 ms
- **Rounds**: 137

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
