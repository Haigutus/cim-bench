# Benchmark Report

**Generated from**: `results-docker/opencgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Opencgmes Load Svedala

- **Mean time**: 79.2 ms
- **Min time**: 66.5 ms
- **Max time**: 96.7 ms
- **Std dev**: 10.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 351.4
- Triples: 47700
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: opencgmes
- Library Version: 1.0.0-SNAPSHOT
- Library Dependencies: {'jpype1': '1.6.0', 'java': '21.0.10', 'jena': '5.5.0'}
- Java Version: 21.0.10
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Lines

- **Mean time**: 438.4 μs
- **Min time**: 155.5 μs
- **Max time**: 65.6 ms
- **Std dev**: 2.5 ms
- **Rounds**: 666

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 172.2 μs
- **Min time**: 70.5 μs
- **Max time**: 80.8 ms
- **Std dev**: 2.1 ms
- **Rounds**: 1554

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 295.7 μs
- **Min time**: 151.8 μs
- **Max time**: 54.2 ms
- **Std dev**: 1.3 ms
- **Rounds**: 1899

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 70.5 μs
- **Min time**: 41.9 μs
- **Max time**: 23.7 ms
- **Std dev**: 439.8 μs
- **Rounds**: 6089

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Svedala

- **Mean time**: 365.6 ms
- **Min time**: 329.1 ms
- **Max time**: 419.1 ms
- **Std dev**: 45.9 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: svedala
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
