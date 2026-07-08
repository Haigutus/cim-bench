# Benchmark Report

**Generated from**: `results-docker/libcimpp_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Libcimpp Load Realgrid

- **Mean time**: 23.95 s
- **Min time**: 21.18 s
- **Max time**: 28.09 s
- **Std dev**: 2.54 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 132.1
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
- Tags: ['parser', 'query', 'typed-model', 'c++']

### Libcimpp Get Lines

- **Mean time**: 8.2 ms
- **Min time**: 4.4 ms
- **Max time**: 13.4 ms
- **Std dev**: 2.5 ms
- **Rounds**: 71

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Generators

- **Mean time**: 7.3 ms
- **Min time**: 4.5 ms
- **Max time**: 12.8 ms
- **Std dev**: 1.7 ms
- **Rounds**: 88

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Loads

- **Mean time**: 19.2 ms
- **Min time**: 16.2 ms
- **Max time**: 21.8 ms
- **Std dev**: 1.5 ms
- **Rounds**: 60

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Substations

- **Mean time**: 8.3 ms
- **Min time**: 4.8 ms
- **Max time**: 13.5 ms
- **Std dev**: 2.8 ms
- **Rounds**: 91

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000
