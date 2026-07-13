# Benchmark Report

**Generated from**: `results-docker/maplib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Maplib Load Svedala

- **Mean time**: 218.0 ms
- **Min time**: 210.4 ms
- **Max time**: 226.5 ms
- **Std dev**: 5.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 140.6
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

- **Mean time**: 14.6 ms
- **Min time**: 11.1 ms
- **Max time**: 16.7 ms
- **Std dev**: 974.8 μs
- **Rounds**: 71

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 331.3 μs
- **Min time**: 243.2 μs
- **Max time**: 800.1 μs
- **Std dev**: 42.6 μs
- **Rounds**: 1474

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 869.9 μs
- **Min time**: 677.1 μs
- **Max time**: 1.8 ms
- **Std dev**: 138.4 μs
- **Rounds**: 1042

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 355.0 μs
- **Min time**: 258.1 μs
- **Max time**: 1.2 ms
- **Std dev**: 58.0 μs
- **Rounds**: 2462

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Export Svedala

- **Mean time**: 1.28 s
- **Min time**: 1.27 s
- **Max time**: 1.31 s
- **Std dev**: 17.1 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: svedala
- Operation: export
- Display Name: maplib
- Color: #8b4513
