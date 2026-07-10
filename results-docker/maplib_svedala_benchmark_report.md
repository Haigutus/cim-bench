# Benchmark Report

**Generated from**: `results-docker/maplib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Maplib Load Svedala

- **Mean time**: 223.5 ms
- **Min time**: 201.9 ms
- **Max time**: 243.7 ms
- **Std dev**: 14.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 139.6
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

- **Mean time**: 363.6 μs
- **Min time**: 242.5 μs
- **Max time**: 1.5 ms
- **Std dev**: 78.6 μs
- **Rounds**: 1277

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 351.1 μs
- **Min time**: 250.9 μs
- **Max time**: 1.1 ms
- **Std dev**: 65.0 μs
- **Rounds**: 2470

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 897.6 μs
- **Min time**: 693.4 μs
- **Max time**: 3.7 ms
- **Std dev**: 180.9 μs
- **Rounds**: 729

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 385.3 μs
- **Min time**: 268.4 μs
- **Max time**: 1.2 ms
- **Std dev**: 77.7 μs
- **Rounds**: 1619

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Export Svedala

- **Mean time**: 1.29 s
- **Min time**: 1.27 s
- **Max time**: 1.32 s
- **Std dev**: 21.0 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: svedala
- Operation: export
- Display Name: maplib
- Color: #8b4513
