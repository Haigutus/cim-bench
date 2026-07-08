# Benchmark Report

**Generated from**: `results-docker/libcimpp_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Libcimpp Load Realgrid

- **Mean time**: 22.74 s
- **Min time**: 22.57 s
- **Max time**: 22.96 s
- **Std dev**: 147.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 132.9
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

- **Mean time**: 8.1 ms
- **Min time**: 6.5 ms
- **Max time**: 12.0 ms
- **Std dev**: 1.3 ms
- **Rounds**: 78

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Generators

- **Mean time**: 8.4 ms
- **Min time**: 6.6 ms
- **Max time**: 11.3 ms
- **Std dev**: 1.0 ms
- **Rounds**: 79

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Loads

- **Mean time**: 19.5 ms
- **Min time**: 18.0 ms
- **Max time**: 21.4 ms
- **Std dev**: 882.6 μs
- **Rounds**: 54

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Substations

- **Mean time**: 8.3 ms
- **Min time**: 6.1 ms
- **Max time**: 11.6 ms
- **Std dev**: 1.2 ms
- **Rounds**: 87

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000
