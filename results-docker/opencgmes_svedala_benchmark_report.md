# Benchmark Report

**Generated from**: `results-docker/opencgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Opencgmes Load Svedala

- **Mean time**: 88.4 ms
- **Min time**: 64.0 ms
- **Max time**: 137.0 ms
- **Std dev**: 31.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 293.5
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

- **Mean time**: 4.7 ms
- **Min time**: 2.1 ms
- **Max time**: 14.7 ms
- **Std dev**: 2.1 ms
- **Rounds**: 97

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 160.7 μs
- **Min time**: 67.7 μs
- **Max time**: 1.3 ms
- **Std dev**: 133.4 μs
- **Rounds**: 1112

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 251.6 μs
- **Min time**: 149.2 μs
- **Max time**: 52.9 ms
- **Std dev**: 1.1 ms
- **Rounds**: 2717

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 81.7 μs
- **Min time**: 43.6 μs
- **Max time**: 48.3 ms
- **Std dev**: 819.7 μs
- **Rounds**: 3833

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Svedala

- **Mean time**: 357.3 ms
- **Min time**: 324.7 ms
- **Max time**: 453.2 ms
- **Std dev**: 54.0 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: svedala
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
