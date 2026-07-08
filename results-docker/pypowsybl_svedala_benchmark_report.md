# Benchmark Report

**Generated from**: `results-docker/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 1.34 s
- **Min time**: 1.18 s
- **Max time**: 1.50 s
- **Std dev**: 132.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 978.6
- Buses: 105
- Lines: 97
- Ac Lines: 90
- Dangling Lines: 7
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: pypowsybl
- Library Version: 1.15.0
- Library Dependencies: {'prettytable': '3.18.0', 'pandas': '3.0.3', 'networkx': '3.6.1'}
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
- Tags: ['parser', 'serializer', 'query', 'powerflow-tool', 'python', 'java']

### Pypowsybl Get Lines

- **Mean time**: 1.5 ms
- **Min time**: 900.6 μs
- **Max time**: 3.2 ms
- **Std dev**: 307.8 μs
- **Rounds**: 440

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 1.4 ms
- **Min time**: 1.1 ms
- **Max time**: 2.4 ms
- **Std dev**: 237.6 μs
- **Rounds**: 420

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 1.0 ms
- **Min time**: 596.0 μs
- **Max time**: 2.5 ms
- **Std dev**: 248.9 μs
- **Rounds**: 555

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 625.6 μs
- **Min time**: 431.3 μs
- **Max time**: 1.3 ms
- **Std dev**: 154.8 μs
- **Rounds**: 979

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Export Svedala

- **Mean time**: 452.5 ms
- **Min time**: 401.1 ms
- **Max time**: 553.4 ms
- **Std dev**: 60.4 ms
- **Rounds**: 5

**Metrics**:
- Library: pypowsybl
- Dataset: svedala
- Operation: export
- Display Name: PyPowSyBl
- Color: #ff7f0e
