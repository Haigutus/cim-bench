# Benchmark Report

**Generated from**: `results-docker/cimoxide_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Cimoxide Load Svedala

- **Mean time**: 103.8 ms
- **Min time**: 81.1 ms
- **Max time**: 120.0 ms
- **Std dev**: 12.4 ms
- **Rounds**: 15

**Metrics**:
- Memory Mb: 60.6
- Objects: 14530
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: cimoxide
- Library Version: 0.0.4
- Library Dependencies: {}
- Dataset: svedala
- Display Name: cimoxide
- Color: #ce422b
- Tags: ['parser', 'validator', 'typed-model', 'python', 'rust']

### Cimoxide Get Lines

- **Mean time**: 259.0 μs
- **Min time**: 245.8 μs
- **Max time**: 377.7 μs
- **Std dev**: 15.6 μs
- **Rounds**: 102

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: cimoxide
- Dataset: svedala
- Display Name: cimoxide
- Color: #ce422b

### Cimoxide Get Generators

- **Mean time**: 292.4 μs
- **Min time**: 236.7 μs
- **Max time**: 1.6 ms
- **Std dev**: 51.4 μs
- **Rounds**: 3486

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: cimoxide
- Dataset: svedala
- Display Name: cimoxide
- Color: #ce422b

### Cimoxide Get Loads

- **Mean time**: 878.1 μs
- **Min time**: 755.6 μs
- **Max time**: 2.7 ms
- **Std dev**: 137.6 μs
- **Rounds**: 1070

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: cimoxide
- Dataset: svedala
- Display Name: cimoxide
- Color: #ce422b

### Cimoxide Get Substations

- **Mean time**: 286.6 μs
- **Min time**: 244.7 μs
- **Max time**: 1.3 ms
- **Std dev**: 35.1 μs
- **Rounds**: 3289

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: cimoxide
- Dataset: svedala
- Display Name: cimoxide
- Color: #ce422b
