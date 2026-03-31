# Benchmark Report

**Generated from**: `results-docker/opencgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Opencgmes Load Svedala

- **Mean time**: 80.1 ms
- **Min time**: 73.7 ms
- **Max time**: 97.4 ms
- **Std dev**: 9.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 532.9
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

- **Mean time**: 329.5 μs
- **Min time**: 103.5 μs
- **Max time**: 2.5 ms
- **Std dev**: 247.2 μs
- **Rounds**: 665

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 154.7 μs
- **Min time**: 74.1 μs
- **Max time**: 91.4 ms
- **Std dev**: 1.7 ms
- **Rounds**: 3962

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 301.6 μs
- **Min time**: 184.1 μs
- **Max time**: 63.8 ms
- **Std dev**: 1.6 ms
- **Rounds**: 2103

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 62.1 μs
- **Min time**: 42.9 μs
- **Max time**: 12.9 ms
- **Std dev**: 309.7 μs
- **Rounds**: 2444

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63
