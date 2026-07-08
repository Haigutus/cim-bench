# Benchmark Report

**Generated from**: `results-docker/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 1.12 s
- **Min time**: 1.07 s
- **Max time**: 1.20 s
- **Std dev**: 48.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 989.3
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

- **Mean time**: 714.6 μs
- **Min time**: 599.3 μs
- **Max time**: 2.0 ms
- **Std dev**: 153.7 μs
- **Rounds**: 493

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 704.9 μs
- **Min time**: 582.0 μs
- **Max time**: 1.6 ms
- **Std dev**: 135.2 μs
- **Rounds**: 708

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 509.4 μs
- **Min time**: 400.3 μs
- **Max time**: 1.3 ms
- **Std dev**: 108.3 μs
- **Rounds**: 1161

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 353.5 μs
- **Min time**: 254.7 μs
- **Max time**: 1.8 ms
- **Std dev**: 113.7 μs
- **Rounds**: 1577

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Export Svedala

- **Mean time**: 456.5 ms
- **Min time**: 371.0 ms
- **Max time**: 565.0 ms
- **Std dev**: 75.5 ms
- **Rounds**: 5

**Metrics**:
- Library: pypowsybl
- Dataset: svedala
- Operation: export
- Display Name: PyPowSyBl
- Color: #ff7f0e
