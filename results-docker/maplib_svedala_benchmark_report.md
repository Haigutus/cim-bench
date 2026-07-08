# Benchmark Report

**Generated from**: `results-docker/maplib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Maplib Load Svedala

- **Mean time**: 663.4 ms
- **Min time**: 598.0 ms
- **Max time**: 750.3 ms
- **Std dev**: 55.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 125.5
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

- **Mean time**: 1.1 ms
- **Min time**: 649.7 μs
- **Max time**: 2.9 ms
- **Std dev**: 323.3 μs
- **Rounds**: 587

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 1.1 ms
- **Min time**: 638.3 μs
- **Max time**: 3.8 ms
- **Std dev**: 314.1 μs
- **Rounds**: 801

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 2.6 ms
- **Min time**: 1.6 ms
- **Max time**: 5.2 ms
- **Std dev**: 645.5 μs
- **Rounds**: 241

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 1.3 ms
- **Min time**: 788.1 μs
- **Max time**: 6.4 ms
- **Std dev**: 376.4 μs
- **Rounds**: 973

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Export Svedala

- **Mean time**: 4.75 s
- **Min time**: 4.43 s
- **Max time**: 5.20 s
- **Std dev**: 281.7 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: svedala
- Operation: export
- Display Name: maplib
- Color: #8b4513
