# Benchmark Report

**Generated from**: `results-docker/opencgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Opencgmes Load Realgrid

- **Mean time**: 1.10 s
- **Min time**: 1.05 s
- **Max time**: 1.15 s
- **Std dev**: 48.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3055.9
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

- **Mean time**: 144.9 ms
- **Min time**: 139.6 ms
- **Max time**: 156.0 ms
- **Std dev**: 6.7 ms
- **Rounds**: 6

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 521.7 μs
- **Min time**: 385.3 μs
- **Max time**: 2.2 ms
- **Std dev**: 225.5 μs
- **Rounds**: 222

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 2.5 ms
- **Min time**: 1.2 ms
- **Max time**: 10.2 ms
- **Std dev**: 1.4 ms
- **Rounds**: 95

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 744.9 μs
- **Min time**: 639.4 μs
- **Max time**: 2.0 ms
- **Std dev**: 136.6 μs
- **Rounds**: 418

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Realgrid

- **Mean time**: 4.00 s
- **Min time**: 3.94 s
- **Max time**: 4.13 s
- **Std dev**: 79.4 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: realgrid
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
