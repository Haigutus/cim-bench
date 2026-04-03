# Benchmark Report

**Generated from**: `results-docker/maplib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Maplib Load Svedala

- **Mean time**: 254.0 ms
- **Min time**: 243.3 ms
- **Max time**: 270.9 ms
- **Std dev**: 10.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 179.5
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: maplib
- Library Version: 0.20.0
- Library Dependencies: {'polars': '1.39.3', 'pyarrow': '23.0.1', 'fastapi': '0.135.3'}
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Lines

- **Mean time**: 366.4 μs
- **Min time**: 251.3 μs
- **Max time**: 2.0 ms
- **Std dev**: 88.5 μs
- **Rounds**: 1438

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 341.4 μs
- **Min time**: 246.0 μs
- **Max time**: 3.1 ms
- **Std dev**: 100.3 μs
- **Rounds**: 1767

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 948.0 μs
- **Min time**: 742.2 μs
- **Max time**: 3.8 ms
- **Std dev**: 153.4 μs
- **Rounds**: 799

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 380.7 μs
- **Min time**: 255.7 μs
- **Max time**: 1.5 ms
- **Std dev**: 77.6 μs
- **Rounds**: 2565

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Export Svedala

- **Mean time**: 1.41 s
- **Min time**: 1.38 s
- **Max time**: 1.42 s
- **Std dev**: 16.1 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: svedala
- Operation: export
- Display Name: maplib
- Color: #8b4513
