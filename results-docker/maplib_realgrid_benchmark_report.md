# Benchmark Report

**Generated from**: `results-docker/maplib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Maplib Load Realgrid

- **Mean time**: 2.03 s
- **Min time**: 1.98 s
- **Max time**: 2.06 s
- **Std dev**: 31.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 441.4
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

- **Mean time**: 618.4 μs
- **Min time**: 413.1 μs
- **Max time**: 1.5 ms
- **Std dev**: 114.7 μs
- **Rounds**: 905

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 485.6 μs
- **Min time**: 329.3 μs
- **Max time**: 1.5 ms
- **Std dev**: 105.3 μs
- **Rounds**: 1294

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 1.2 ms
- **Min time**: 837.9 μs
- **Max time**: 3.0 ms
- **Std dev**: 234.1 μs
- **Rounds**: 781

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 524.3 μs
- **Min time**: 359.5 μs
- **Max time**: 2.9 ms
- **Std dev**: 105.4 μs
- **Rounds**: 1433

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Export Realgrid

- **Mean time**: 15.10 s
- **Min time**: 14.81 s
- **Max time**: 15.22 s
- **Std dev**: 165.8 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: realgrid
- Operation: export
- Display Name: maplib
- Color: #8b4513
