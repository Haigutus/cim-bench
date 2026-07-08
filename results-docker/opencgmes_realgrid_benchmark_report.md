# Benchmark Report

**Generated from**: `results-docker/opencgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Opencgmes Load Realgrid

- **Mean time**: 2.18 s
- **Min time**: 1.93 s
- **Max time**: 2.43 s
- **Std dev**: 228.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4391.8
- Triples: 892131
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: opencgmes
- Library Version: 1.1.0-SNAPSHOT
- Library Dependencies: {'jpype1': '1.7.1', 'java': '21.0.11', 'jena': '6.1.0'}
- Java Version: 21.0.11
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'java']

### Opencgmes Get Lines

- **Mean time**: 13.2 ms
- **Min time**: 5.1 ms
- **Max time**: 32.3 ms
- **Std dev**: 6.9 ms
- **Rounds**: 39

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 2.8 ms
- **Min time**: 1.1 ms
- **Max time**: 9.5 ms
- **Std dev**: 2.0 ms
- **Rounds**: 85

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 7.5 ms
- **Min time**: 4.0 ms
- **Max time**: 15.0 ms
- **Std dev**: 2.3 ms
- **Rounds**: 61

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 4.6 ms
- **Min time**: 1.9 ms
- **Max time**: 14.3 ms
- **Std dev**: 2.5 ms
- **Rounds**: 67

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Realgrid

- **Mean time**: 7.56 s
- **Min time**: 6.87 s
- **Max time**: 8.50 s
- **Std dev**: 586.1 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: realgrid
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
