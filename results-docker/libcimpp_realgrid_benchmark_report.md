# Benchmark Report

**Generated from**: `results-docker/libcimpp_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Libcimpp Load Realgrid

- **Mean time**: 20.11 s
- **Min time**: 19.93 s
- **Max time**: 20.23 s
- **Std dev**: 122.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 134.7
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: libcimpp
- Library Version: 2.2.0
- Library Dependencies: {}
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Lines

- **Mean time**: 6.8 ms
- **Min time**: 3.6 ms
- **Max time**: 13.4 ms
- **Std dev**: 3.1 ms
- **Rounds**: 78

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Generators

- **Mean time**: 6.8 ms
- **Min time**: 3.7 ms
- **Max time**: 14.0 ms
- **Std dev**: 3.3 ms
- **Rounds**: 72

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Loads

- **Mean time**: 16.3 ms
- **Min time**: 9.8 ms
- **Max time**: 23.2 ms
- **Std dev**: 3.6 ms
- **Rounds**: 60

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Substations

- **Mean time**: 7.2 ms
- **Min time**: 3.7 ms
- **Max time**: 16.8 ms
- **Std dev**: 3.9 ms
- **Rounds**: 111

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000
