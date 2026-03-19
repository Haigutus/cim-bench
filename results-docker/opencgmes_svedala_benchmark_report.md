# Benchmark Report

**Generated from**: `results-docker/opencgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.8-200.fc43.x86_64

## Results

### Opencgmes Load Svedala

- **Mean time**: 99.6 ms
- **Min time**: 79.1 ms
- **Max time**: 128.3 ms
- **Std dev**: 19.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 426.7
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

- **Mean time**: 536.8 μs
- **Min time**: 149.3 μs
- **Max time**: 3.6 ms
- **Std dev**: 402.1 μs
- **Rounds**: 573

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 200.6 μs
- **Min time**: 65.2 μs
- **Max time**: 103.6 ms
- **Std dev**: 2.4 ms
- **Rounds**: 2770

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 306.8 μs
- **Min time**: 171.7 μs
- **Max time**: 16.8 ms
- **Std dev**: 784.2 μs
- **Rounds**: 983

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 129.1 μs
- **Min time**: 50.3 μs
- **Max time**: 153.4 ms
- **Std dev**: 2.2 ms
- **Rounds**: 5052

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63
