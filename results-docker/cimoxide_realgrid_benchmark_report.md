# Benchmark Report

**Generated from**: `results-docker/cimoxide_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Cimoxide Load Realgrid

- **Mean time**: 1.26 s
- **Min time**: 1.19 s
- **Max time**: 1.39 s
- **Std dev**: 78.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 537.4
- Objects: 149166
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: cimoxide
- Library Version: 0.0.4
- Library Dependencies: {}
- Dataset: realgrid
- Display Name: cimoxide
- Color: #ce422b
- Tags: ['parser', 'validator', 'typed-model', 'python', 'rust']

### Cimoxide Get Lines

- **Mean time**: 12.9 ms
- **Min time**: 6.3 ms
- **Max time**: 45.0 ms
- **Std dev**: 9.9 ms
- **Rounds**: 23

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: cimoxide
- Dataset: realgrid
- Display Name: cimoxide
- Color: #ce422b

### Cimoxide Get Generators

- **Mean time**: 9.3 ms
- **Min time**: 6.0 ms
- **Max time**: 13.1 ms
- **Std dev**: 1.7 ms
- **Rounds**: 153

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: cimoxide
- Dataset: realgrid
- Display Name: cimoxide
- Color: #ce422b

### Cimoxide Get Loads

- **Mean time**: 26.3 ms
- **Min time**: 19.4 ms
- **Max time**: 33.5 ms
- **Std dev**: 3.8 ms
- **Rounds**: 42

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: cimoxide
- Dataset: realgrid
- Display Name: cimoxide
- Color: #ce422b

### Cimoxide Get Substations

- **Mean time**: 7.4 ms
- **Min time**: 5.7 ms
- **Max time**: 10.8 ms
- **Std dev**: 1.1 ms
- **Rounds**: 109

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: cimoxide
- Dataset: realgrid
- Display Name: cimoxide
- Color: #ce422b
