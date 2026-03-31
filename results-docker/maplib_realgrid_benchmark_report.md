# Benchmark Report

**Generated from**: `results-docker/maplib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Maplib Load Realgrid

- **Mean time**: 2.14 s
- **Min time**: 2.09 s
- **Max time**: 2.17 s
- **Std dev**: 35.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 551.5
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Lines

- **Mean time**: 548.2 μs
- **Min time**: 400.5 μs
- **Max time**: 1.2 ms
- **Std dev**: 58.5 μs
- **Rounds**: 1522

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 411.2 μs
- **Min time**: 308.2 μs
- **Max time**: 3.0 ms
- **Std dev**: 86.9 μs
- **Rounds**: 1891

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 1.1 ms
- **Min time**: 826.3 μs
- **Max time**: 2.3 ms
- **Std dev**: 122.5 μs
- **Rounds**: 878

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 481.1 μs
- **Min time**: 351.3 μs
- **Max time**: 1.3 ms
- **Std dev**: 59.0 μs
- **Rounds**: 1797

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: maplib
- Dataset: realgrid
- Display Name: maplib
- Color: #8b4513
