# Benchmark Report

**Generated from**: `results-docker/maplib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Maplib Load Realgrid

- **Mean time**: 4.53 s
- **Min time**: 4.42 s
- **Max time**: 4.70 s
- **Std dev**: 120.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 356.3
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

- **Mean time**: 1.8 ms
- **Min time**: 1.1 ms
- **Max time**: 3.7 ms
- **Std dev**: 280.6 μs
- **Rounds**: 525

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 1.3 ms
- **Min time**: 916.3 μs
- **Max time**: 3.6 ms
- **Std dev**: 271.5 μs
- **Rounds**: 718

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 3.2 ms
- **Min time**: 2.1 ms
- **Max time**: 6.7 ms
- **Std dev**: 572.3 μs
- **Rounds**: 309

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 1.5 ms
- **Min time**: 990.3 μs
- **Max time**: 5.4 ms
- **Std dev**: 309.0 μs
- **Rounds**: 651

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Export Realgrid

- **Mean time**: 54.74 s
- **Min time**: 54.20 s
- **Max time**: 55.50 s
- **Std dev**: 526.9 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: realgrid
- Operation: export
- Display Name: maplib
- Color: #8b4513
