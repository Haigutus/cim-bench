# Benchmark Report

**Generated from**: `results/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 447.2 ms
- **Min time**: 426.0 ms
- **Max time**: 466.2 ms
- **Std dev**: 18.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1157.2
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

- **Mean time**: 343.3 μs
- **Min time**: 318.7 μs
- **Max time**: 3.1 ms
- **Std dev**: 86.7 μs
- **Rounds**: 1065

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 329.8 μs
- **Min time**: 302.5 μs
- **Max time**: 628.9 μs
- **Std dev**: 28.4 μs
- **Rounds**: 1603

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 233.0 μs
- **Min time**: 214.7 μs
- **Max time**: 464.3 μs
- **Std dev**: 27.0 μs
- **Rounds**: 2101

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 185.2 μs
- **Min time**: 144.5 μs
- **Max time**: 23.9 ms
- **Std dev**: 452.0 μs
- **Rounds**: 2786

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
