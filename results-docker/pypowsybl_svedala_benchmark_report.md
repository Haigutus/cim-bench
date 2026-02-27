# Benchmark Report

**Generated from**: `results-docker/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 489.4 ms
- **Min time**: 468.2 ms
- **Max time**: 516.0 ms
- **Std dev**: 22.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 898.9
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

- **Mean time**: 345.0 μs
- **Min time**: 319.8 μs
- **Max time**: 1.3 ms
- **Std dev**: 45.5 μs
- **Rounds**: 1106

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 328.9 μs
- **Min time**: 291.2 μs
- **Max time**: 23.4 ms
- **Std dev**: 637.9 μs
- **Rounds**: 1313

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 225.4 μs
- **Min time**: 206.0 μs
- **Max time**: 1.2 ms
- **Std dev**: 48.6 μs
- **Rounds**: 1737

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 146.2 μs
- **Min time**: 129.7 μs
- **Max time**: 1.0 ms
- **Std dev**: 40.8 μs
- **Rounds**: 2668

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
