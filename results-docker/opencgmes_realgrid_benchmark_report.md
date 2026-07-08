# Benchmark Report

**Generated from**: `results-docker/opencgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Opencgmes Load Realgrid

- **Mean time**: 2.50 s
- **Min time**: 2.18 s
- **Max time**: 3.03 s
- **Std dev**: 360.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3891.2
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

- **Mean time**: 13.1 ms
- **Min time**: 7.2 ms
- **Max time**: 32.3 ms
- **Std dev**: 5.2 ms
- **Rounds**: 39

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 2.1 ms
- **Min time**: 982.4 μs
- **Max time**: 6.0 ms
- **Std dev**: 930.3 μs
- **Rounds**: 137

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 9.4 ms
- **Min time**: 3.4 ms
- **Max time**: 124.3 ms
- **Std dev**: 13.2 ms
- **Rounds**: 80

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 2.1 ms
- **Min time**: 1.3 ms
- **Max time**: 18.4 ms
- **Std dev**: 2.2 ms
- **Rounds**: 199

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Realgrid

- **Mean time**: 6.56 s
- **Min time**: 5.60 s
- **Max time**: 7.58 s
- **Std dev**: 733.9 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: realgrid
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
