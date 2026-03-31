# Benchmark Report

**Generated from**: `results-docker/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 413.2 ms
- **Min time**: 382.2 ms
- **Max time**: 445.8 ms
- **Std dev**: 26.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 951.9
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

- **Mean time**: 302.4 μs
- **Min time**: 277.9 μs
- **Max time**: 1.5 ms
- **Std dev**: 66.5 μs
- **Rounds**: 1126

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 284.5 μs
- **Min time**: 262.8 μs
- **Max time**: 1.2 ms
- **Std dev**: 41.4 μs
- **Rounds**: 1713

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 211.5 μs
- **Min time**: 187.4 μs
- **Max time**: 25.4 ms
- **Std dev**: 515.1 μs
- **Rounds**: 2397

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 119.8 μs
- **Min time**: 111.6 μs
- **Max time**: 714.9 μs
- **Std dev**: 16.2 μs
- **Rounds**: 3318

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
