# Benchmark Report

**Generated from**: `results-docker/libcimpp_svedala_benchmark.json`

## Environment

- **CPU**: 11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz
- **Cores**: 4
- **Python**: 3.14.6
- **System**: Linux 6.8.0-147-generic

## Results

### Libcimpp Load Svedala

- **Mean time**: 135.1 ms
- **Min time**: 132.2 ms
- **Max time**: 139.5 ms
- **Std dev**: 2.7 ms
- **Rounds**: 7

**Metrics**:
- Memory Mb: 9.4
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: libcimpp
- Library Version: 2.3.1
- Library Dependencies: {}
- Dataset: svedala
- Display Name: libcimpp
- Color: #000000
- Tags: ['parser', 'serializer', 'query', 'typed-model', 'c++']

### Libcimpp Get Lines

- **Mean time**: 428.4 μs
- **Min time**: 342.2 μs
- **Max time**: 844.0 μs
- **Std dev**: 40.5 μs
- **Rounds**: 1712

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: libcimpp
- Dataset: svedala
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Generators

- **Mean time**: 422.0 μs
- **Min time**: 358.2 μs
- **Max time**: 976.2 μs
- **Std dev**: 32.7 μs
- **Rounds**: 2280

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: libcimpp
- Dataset: svedala
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Loads

- **Mean time**: 1.2 ms
- **Min time**: 1.1 ms
- **Max time**: 4.9 ms
- **Std dev**: 167.6 μs
- **Rounds**: 817

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: libcimpp
- Dataset: svedala
- Display Name: libcimpp
- Color: #000000

### Libcimpp Get Substations

- **Mean time**: 417.4 μs
- **Min time**: 351.5 μs
- **Max time**: 1.0 ms
- **Std dev**: 40.6 μs
- **Rounds**: 2169

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: libcimpp
- Dataset: svedala
- Display Name: libcimpp
- Color: #000000

### Libcimpp Export Svedala

- **Mean time**: 411.1 ms
- **Min time**: 404.9 ms
- **Max time**: 417.9 ms
- **Std dev**: 5.4 ms
- **Rounds**: 5

**Metrics**:
- Library: libcimpp
- Dataset: svedala
- Operation: export
- Display Name: libcimpp
- Color: #000000
