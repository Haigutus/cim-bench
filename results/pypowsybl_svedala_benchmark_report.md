# Benchmark Report

**Generated from**: `results/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 460.0 ms
- **Min time**: 444.0 ms
- **Max time**: 482.3 ms
- **Std dev**: 19.9 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 921.9
- Buses: 105
- Lines: 97
- Ac Lines: 90
- Dangling Lines: 7
- Generators: 39
- Loads: 73
- Substations: 57
- Total Size Mb: 7.3
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Lines

- **Mean time**: 350.8 μs
- **Min time**: 310.8 μs
- **Max time**: 2.2 ms
- **Std dev**: 78.3 μs
- **Rounds**: 1020

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 367.9 μs
- **Min time**: 300.4 μs
- **Max time**: 3.4 ms
- **Std dev**: 125.5 μs
- **Rounds**: 1581

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 238.5 μs
- **Min time**: 211.6 μs
- **Max time**: 1.2 ms
- **Std dev**: 48.1 μs
- **Rounds**: 2102

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 167.6 μs
- **Min time**: 153.4 μs
- **Max time**: 598.8 μs
- **Std dev**: 18.6 μs
- **Rounds**: 2742

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
