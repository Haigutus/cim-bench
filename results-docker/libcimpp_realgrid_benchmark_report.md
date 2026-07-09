# Benchmark Report

**Generated from**: `results-docker/libcimpp_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Libcimpp Load Realgrid

- **Mean time**: 19.53 s
- **Min time**: 19.41 s
- **Max time**: 19.64 s
- **Std dev**: 90.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 133.8
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

- **Mean time**: 5.4 ms
- **Min time**: 3.5 ms
- **Max time**: 13.6 ms
- **Std dev**: 2.8 ms
- **Rounds**: 79

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Generators

- **Mean time**: 5.4 ms
- **Min time**: 3.7 ms
- **Max time**: 13.9 ms
- **Std dev**: 2.7 ms
- **Rounds**: 109

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Loads

- **Mean time**: 12.8 ms
- **Min time**: 9.2 ms
- **Max time**: 22.3 ms
- **Std dev**: 4.5 ms
- **Rounds**: 60

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Substations

- **Mean time**: 5.4 ms
- **Min time**: 3.6 ms
- **Max time**: 13.9 ms
- **Std dev**: 2.7 ms
- **Rounds**: 107

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000
