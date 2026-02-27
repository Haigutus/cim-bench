# Benchmark Report

**Generated from**: `results/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 498.3 ms
- **Min time**: 472.2 ms
- **Max time**: 520.3 ms
- **Std dev**: 22.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 895.1
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

- **Mean time**: 409.9 μs
- **Min time**: 383.2 μs
- **Max time**: 746.7 μs
- **Std dev**: 30.0 μs
- **Rounds**: 769

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 408.9 μs
- **Min time**: 361.5 μs
- **Max time**: 3.0 ms
- **Std dev**: 112.7 μs
- **Rounds**: 1201

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 294.5 μs
- **Min time**: 263.9 μs
- **Max time**: 1.7 ms
- **Std dev**: 52.4 μs
- **Rounds**: 1560

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 215.8 μs
- **Min time**: 185.6 μs
- **Max time**: 912.4 μs
- **Std dev**: 44.7 μs
- **Rounds**: 2637

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
