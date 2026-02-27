# Benchmark Report

**Generated from**: `results-docker/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 433.8 ms
- **Min time**: 405.4 ms
- **Max time**: 478.0 ms
- **Std dev**: 30.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1044.7
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

- **Mean time**: 296.7 μs
- **Min time**: 266.0 μs
- **Max time**: 19.0 ms
- **Std dev**: 557.4 μs
- **Rounds**: 1130

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 264.6 μs
- **Min time**: 250.7 μs
- **Max time**: 409.7 μs
- **Std dev**: 14.0 μs
- **Rounds**: 1843

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 189.1 μs
- **Min time**: 178.5 μs
- **Max time**: 355.7 μs
- **Std dev**: 13.4 μs
- **Rounds**: 2383

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 119.0 μs
- **Min time**: 110.9 μs
- **Max time**: 301.9 μs
- **Std dev**: 12.6 μs
- **Rounds**: 3586

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
