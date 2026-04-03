# Benchmark Report

**Generated from**: `results-docker/maplib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Maplib Load Realgrid

- **Mean time**: 2.18 s
- **Min time**: 2.15 s
- **Max time**: 2.22 s
- **Std dev**: 26.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 576.3
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: maplib
- Library Version: 0.20.0
- Library Dependencies: {'polars': '1.39.3', 'pyarrow': '23.0.1', 'fastapi': '0.135.3'}
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Lines

- **Mean time**: 609.0 μs
- **Min time**: 434.9 μs
- **Max time**: 3.1 ms
- **Std dev**: 125.3 μs
- **Rounds**: 958

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 452.2 μs
- **Min time**: 327.0 μs
- **Max time**: 3.2 ms
- **Std dev**: 138.2 μs
- **Rounds**: 1590

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 1.2 ms
- **Min time**: 864.5 μs
- **Max time**: 4.1 ms
- **Std dev**: 193.4 μs
- **Rounds**: 766

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 517.6 μs
- **Min time**: 383.0 μs
- **Max time**: 2.2 ms
- **Std dev**: 81.8 μs
- **Rounds**: 1964

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Export Realgrid

- **Mean time**: 16.79 s
- **Min time**: 16.71 s
- **Max time**: 16.96 s
- **Std dev**: 101.7 ms
- **Rounds**: 5

**Metrics**:
- Library: maplib
- Dataset: realgrid
- Operation: export
- Display Name: maplib
- Color: #8b4513
