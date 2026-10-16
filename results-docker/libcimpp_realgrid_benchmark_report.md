# Benchmark Report

**Generated from**: `results-docker/libcimpp_realgrid_benchmark.json`

## Environment

- **CPU**: 11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz
- **Cores**: 4
- **Python**: 3.14.6
- **System**: Linux 6.8.0-147-generic

## Results

### Libcimpp Load Realgrid

- **Mean time**: 4.90 s
- **Min time**: 4.85 s
- **Max time**: 4.96 s
- **Std dev**: 49.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 132.2
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: libcimpp
- Library Version: 2.3.1
- Library Dependencies: {}
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000
- Tags: ['parser', 'serializer', 'query', 'typed-model', 'c++']

### Libcimpp Get Lines

- **Mean time**: 13.5 ms
- **Min time**: 12.2 ms
- **Max time**: 16.5 ms
- **Std dev**: 878.5 μs
- **Rounds**: 75

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Generators

- **Mean time**: 14.5 ms
- **Min time**: 13.3 ms
- **Max time**: 18.1 ms
- **Std dev**: 611.1 μs
- **Rounds**: 76

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Loads

- **Mean time**: 25.1 ms
- **Min time**: 24.0 ms
- **Max time**: 27.4 ms
- **Std dev**: 850.0 μs
- **Rounds**: 41

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Substations

- **Mean time**: 12.4 ms
- **Min time**: 11.7 ms
- **Max time**: 13.6 ms
- **Std dev**: 472.5 μs
- **Rounds**: 70

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: libcimpp
- Dataset: realgrid
- Display Name: libcimpp
- Color: #000000

### Libcimpp Export Realgrid

- **Mean time**: 6.39 s
- **Min time**: 6.36 s
- **Max time**: 6.45 s
- **Std dev**: 34.4 ms
- **Rounds**: 5

**Metrics**:
- Library: libcimpp
- Dataset: realgrid
- Operation: export
- Display Name: libcimpp
- Color: #000000
