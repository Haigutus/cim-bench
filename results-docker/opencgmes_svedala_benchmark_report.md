# Benchmark Report

**Generated from**: `results-docker/opencgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Opencgmes Load Svedala

- **Mean time**: 100.3 ms
- **Min time**: 56.7 ms
- **Max time**: 204.5 ms
- **Std dev**: 59.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 247.4
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

- **Mean time**: 290.5 μs
- **Min time**: 143.8 μs
- **Max time**: 1.7 ms
- **Std dev**: 161.0 μs
- **Rounds**: 642

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 96.9 μs
- **Min time**: 64.4 μs
- **Max time**: 17.5 ms
- **Std dev**: 308.4 μs
- **Rounds**: 3226

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 217.8 μs
- **Min time**: 155.0 μs
- **Max time**: 21.5 ms
- **Std dev**: 510.5 μs
- **Rounds**: 1763

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 84.9 μs
- **Min time**: 42.1 μs
- **Max time**: 72.3 ms
- **Std dev**: 1.0 ms
- **Rounds**: 5962

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Svedala

- **Mean time**: 341.0 ms
- **Min time**: 325.3 ms
- **Max time**: 385.9 ms
- **Std dev**: 25.4 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: svedala
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
