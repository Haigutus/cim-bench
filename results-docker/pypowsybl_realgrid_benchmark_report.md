# Benchmark Report

**Generated from**: `results-docker/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.87 s
- **Min time**: 4.82 s
- **Max time**: 4.99 s
- **Std dev**: 70.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1706.3
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

- **Mean time**: 40.5 ms
- **Min time**: 36.0 ms
- **Max time**: 51.0 ms
- **Std dev**: 3.6 ms
- **Rounds**: 27

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 3.9 ms
- **Min time**: 2.9 ms
- **Max time**: 7.4 ms
- **Std dev**: 915.0 μs
- **Rounds**: 145

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 23.1 ms
- **Min time**: 20.4 ms
- **Max time**: 37.0 ms
- **Std dev**: 2.7 ms
- **Rounds**: 44

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 6.5 ms
- **Min time**: 5.3 ms
- **Max time**: 10.2 ms
- **Std dev**: 964.1 μs
- **Rounds**: 103

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
