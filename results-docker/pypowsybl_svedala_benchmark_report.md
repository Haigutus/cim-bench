# Benchmark Report

**Generated from**: `results-docker/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 428.4 ms
- **Min time**: 401.3 ms
- **Max time**: 450.5 ms
- **Std dev**: 24.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1566.6
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

- **Mean time**: 292.9 μs
- **Min time**: 280.3 μs
- **Max time**: 449.3 μs
- **Std dev**: 8.3 μs
- **Rounds**: 1173

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 265.9 μs
- **Min time**: 254.3 μs
- **Max time**: 380.5 μs
- **Std dev**: 9.4 μs
- **Rounds**: 1810

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 194.2 μs
- **Min time**: 176.3 μs
- **Max time**: 10.4 ms
- **Std dev**: 241.3 μs
- **Rounds**: 1791

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 120.9 μs
- **Min time**: 113.0 μs
- **Max time**: 674.6 μs
- **Std dev**: 12.8 μs
- **Rounds**: 3644

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Export Svedala

- **Mean time**: 138.0 ms
- **Min time**: 136.6 ms
- **Max time**: 141.8 ms
- **Std dev**: 1.7 ms
- **Rounds**: 8

**Metrics**:
- Library: pypowsybl
- Dataset: svedala
- Operation: export
- Display Name: PyPowSyBl
- Color: #ff7f0e
