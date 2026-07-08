# Benchmark Report

**Generated from**: `results-docker/opencgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Opencgmes Load Svedala

- **Mean time**: 251.0 ms
- **Min time**: 143.3 ms
- **Max time**: 472.5 ms
- **Std dev**: 137.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 275.1
- Triples: 47700
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: opencgmes
- Library Version: 1.1.0-SNAPSHOT
- Library Dependencies: {'jpype1': '1.7.1', 'java': '21.0.11', 'jena': '6.1.0'}
- Java Version: 21.0.11
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'java']

### Opencgmes Get Lines

- **Mean time**: 1.2 ms
- **Min time**: 538.3 μs
- **Max time**: 4.5 ms
- **Std dev**: 515.5 μs
- **Rounds**: 213

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 394.7 μs
- **Min time**: 150.4 μs
- **Max time**: 4.6 ms
- **Std dev**: 305.1 μs
- **Rounds**: 1444

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 854.4 μs
- **Min time**: 512.8 μs
- **Max time**: 3.6 ms
- **Std dev**: 266.7 μs
- **Rounds**: 643

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 449.7 μs
- **Min time**: 163.1 μs
- **Max time**: 164.8 ms
- **Std dev**: 4.0 ms
- **Rounds**: 1768

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Svedala

- **Mean time**: 842.3 ms
- **Min time**: 690.2 ms
- **Max time**: 1.01 s
- **Std dev**: 121.4 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: svedala
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
