# Benchmark Report

**Generated from**: `results-docker/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 475.8 ms
- **Min time**: 439.5 ms
- **Max time**: 503.4 ms
- **Std dev**: 28.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1160.2
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

- **Mean time**: 299.3 μs
- **Min time**: 277.7 μs
- **Max time**: 640.9 μs
- **Std dev**: 24.5 μs
- **Rounds**: 1020

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 285.9 μs
- **Min time**: 262.3 μs
- **Max time**: 736.7 μs
- **Std dev**: 32.3 μs
- **Rounds**: 1778

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 215.8 μs
- **Min time**: 184.9 μs
- **Max time**: 24.6 ms
- **Std dev**: 507.9 μs
- **Rounds**: 2315

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 132.0 μs
- **Min time**: 118.0 μs
- **Max time**: 780.5 μs
- **Std dev**: 27.8 μs
- **Rounds**: 3192

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
