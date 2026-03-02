# Benchmark Report

**Generated from**: `results-docker/opencgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Opencgmes Load Svedala

- **Mean time**: 90.2 ms
- **Min time**: 68.0 ms
- **Max time**: 126.2 ms
- **Std dev**: 22.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 413.0
- Triples: 47700
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Total Size Mb: 7.3
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Lines

- **Mean time**: 455.7 μs
- **Min time**: 162.8 μs
- **Max time**: 4.1 ms
- **Std dev**: 350.6 μs
- **Rounds**: 624

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 136.7 μs
- **Min time**: 72.7 μs
- **Max time**: 15.5 ms
- **Std dev**: 382.1 μs
- **Rounds**: 1687

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 273.0 μs
- **Min time**: 196.1 μs
- **Max time**: 1.7 ms
- **Std dev**: 104.1 μs
- **Rounds**: 860

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 141.0 μs
- **Min time**: 52.1 μs
- **Max time**: 105.7 ms
- **Std dev**: 2.2 ms
- **Rounds**: 6046

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63
