# Benchmark Report

**Generated from**: `results-docker/maplib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Maplib Load Realgrid

- **Mean time**: 4.86 s
- **Min time**: 4.60 s
- **Max time**: 5.47 s
- **Std dev**: 348.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 360.1
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

- **Mean time**: 2.0 ms
- **Min time**: 1.3 ms
- **Max time**: 4.1 ms
- **Std dev**: 387.7 μs
- **Rounds**: 352

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 1.4 ms
- **Min time**: 946.6 μs
- **Max time**: 4.2 ms
- **Std dev**: 344.7 μs
- **Rounds**: 616

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 3.8 ms
- **Min time**: 2.3 ms
- **Max time**: 14.6 ms
- **Std dev**: 1.3 ms
- **Rounds**: 188

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 1.9 ms
- **Min time**: 1.1 ms
- **Max time**: 5.6 ms
- **Std dev**: 627.2 μs
- **Rounds**: 300

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Export Realgrid

- **Mean time**: 67.61 s
- **Min time**: 55.60 s
- **Max time**: 74.44 s
- **Std dev**: 7.97 s
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: realgrid
- Operation: export
- Display Name: maplib
- Color: #8b4513
