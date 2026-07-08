# Benchmark Report

**Generated from**: `results-docker/maplib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Maplib Load Svedala

- **Mean time**: 526.9 ms
- **Min time**: 464.1 ms
- **Max time**: 546.0 ms
- **Std dev**: 35.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 128.4
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: maplib
- Library Version: 0.20.19
- Library Dependencies: {'polars': '1.42.1', 'pyarrow': '23.0.1', 'fastapi': '0.139.0'}
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'python', 'rust']

### Maplib Get Lines

- **Mean time**: 919.2 μs
- **Min time**: 639.1 μs
- **Max time**: 3.5 ms
- **Std dev**: 212.0 μs
- **Rounds**: 749

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 1.0 ms
- **Min time**: 639.8 μs
- **Max time**: 2.5 ms
- **Std dev**: 260.1 μs
- **Rounds**: 1009

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 2.4 ms
- **Min time**: 1.6 ms
- **Max time**: 4.1 ms
- **Std dev**: 464.5 μs
- **Rounds**: 397

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 975.5 μs
- **Min time**: 663.0 μs
- **Max time**: 2.5 ms
- **Std dev**: 205.3 μs
- **Rounds**: 940

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Export Svedala

- **Mean time**: 4.42 s
- **Min time**: 4.22 s
- **Max time**: 4.62 s
- **Std dev**: 144.5 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: svedala
- Operation: export
- Display Name: maplib
- Color: #8b4513
