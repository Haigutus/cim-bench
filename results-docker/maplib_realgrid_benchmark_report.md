# Benchmark Report

**Generated from**: `results-docker/maplib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Maplib Load Realgrid

- **Mean time**: 2.01 s
- **Min time**: 1.98 s
- **Max time**: 2.03 s
- **Std dev**: 21.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 454.8
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: maplib
- Library Version: 0.20.19
- Library Dependencies: {'polars': '1.42.1', 'pyarrow': '23.0.1', 'fastapi': '0.139.0'}
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'python', 'rust']

### Maplib Get Lines

- **Mean time**: 44.6 ms
- **Min time**: 42.8 ms
- **Max time**: 47.7 ms
- **Std dev**: 1.1 ms
- **Rounds**: 23

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 459.0 μs
- **Min time**: 320.0 μs
- **Max time**: 900.4 μs
- **Std dev**: 83.5 μs
- **Rounds**: 1076

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 1.1 ms
- **Min time**: 889.8 μs
- **Max time**: 2.1 ms
- **Std dev**: 146.0 μs
- **Rounds**: 803

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 485.3 μs
- **Min time**: 348.6 μs
- **Max time**: 3.2 ms
- **Std dev**: 91.4 μs
- **Rounds**: 1751

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Export Realgrid

- **Mean time**: 15.26 s
- **Min time**: 15.19 s
- **Max time**: 15.35 s
- **Std dev**: 75.9 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: realgrid
- Operation: export
- Display Name: maplib
- Color: #8b4513
