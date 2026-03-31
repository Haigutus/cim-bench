# Benchmark Report

**Generated from**: `results-docker/libcimpp_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Libcimpp Load Realgrid

- **Mean time**: 21.35 s
- **Min time**: 21.29 s
- **Max time**: 21.45 s
- **Std dev**: 63.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 134.7
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Lines

- **Mean time**: 5.0 ms
- **Min time**: 4.2 ms
- **Max time**: 12.2 ms
- **Std dev**: 1.1 ms
- **Rounds**: 79

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Generators

- **Mean time**: 5.2 ms
- **Min time**: 4.4 ms
- **Max time**: 10.4 ms
- **Std dev**: 1.0 ms
- **Rounds**: 75

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Loads

- **Mean time**: 11.0 ms
- **Min time**: 9.9 ms
- **Max time**: 16.9 ms
- **Std dev**: 1.5 ms
- **Rounds**: 52

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Substations

- **Mean time**: 4.7 ms
- **Min time**: 3.9 ms
- **Max time**: 9.6 ms
- **Std dev**: 850.2 μs
- **Rounds**: 107

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000
