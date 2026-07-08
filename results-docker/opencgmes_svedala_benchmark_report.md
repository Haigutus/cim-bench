# Benchmark Report

**Generated from**: `results-docker/opencgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Opencgmes Load Svedala

- **Mean time**: 268.6 ms
- **Min time**: 169.5 ms
- **Max time**: 467.8 ms
- **Std dev**: 120.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 255.8
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

- **Mean time**: 1.4 ms
- **Min time**: 547.2 μs
- **Max time**: 5.4 ms
- **Std dev**: 668.7 μs
- **Rounds**: 191

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 644.0 μs
- **Min time**: 192.4 μs
- **Max time**: 4.4 ms
- **Std dev**: 407.8 μs
- **Rounds**: 706

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 909.9 μs
- **Min time**: 431.5 μs
- **Max time**: 23.4 ms
- **Std dev**: 824.0 μs
- **Rounds**: 861

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 247.7 μs
- **Min time**: 168.3 μs
- **Max time**: 3.0 ms
- **Std dev**: 110.2 μs
- **Rounds**: 1365

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: opencgmes
- Dataset: svedala
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Svedala

- **Mean time**: 801.6 ms
- **Min time**: 717.9 ms
- **Max time**: 920.1 ms
- **Std dev**: 78.8 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: svedala
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
