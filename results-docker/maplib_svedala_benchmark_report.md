# Benchmark Report

**Generated from**: `results-docker/maplib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Maplib Load Svedala

- **Mean time**: 251.2 ms
- **Min time**: 243.4 ms
- **Max time**: 260.0 ms
- **Std dev**: 6.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 175.9
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Total Size Mb: 7.3
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Lines

- **Mean time**: 331.6 μs
- **Min time**: 235.8 μs
- **Max time**: 3.1 ms
- **Std dev**: 89.2 μs
- **Rounds**: 1467

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Generators

- **Mean time**: 324.0 μs
- **Min time**: 238.0 μs
- **Max time**: 836.7 μs
- **Std dev**: 51.0 μs
- **Rounds**: 2264

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Loads

- **Mean time**: 910.3 μs
- **Min time**: 718.5 μs
- **Max time**: 2.1 ms
- **Std dev**: 134.0 μs
- **Rounds**: 960

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513

### Maplib Get Substations

- **Mean time**: 342.4 μs
- **Min time**: 256.0 μs
- **Max time**: 2.5 ms
- **Std dev**: 68.1 μs
- **Rounds**: 1913

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: maplib
- Dataset: svedala
- Display Name: maplib
- Color: #8b4513
