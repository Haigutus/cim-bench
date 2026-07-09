# Benchmark Report

**Generated from**: `results-docker/opencgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Opencgmes Load Realgrid

- **Mean time**: 1.09 s
- **Min time**: 1.01 s
- **Max time**: 1.18 s
- **Std dev**: 69.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3133.8
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

- **Mean time**: 3.7 ms
- **Min time**: 1.9 ms
- **Max time**: 11.4 ms
- **Std dev**: 2.1 ms
- **Rounds**: 83

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 775.6 μs
- **Min time**: 340.2 μs
- **Max time**: 4.9 ms
- **Std dev**: 609.8 μs
- **Rounds**: 247

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 2.2 ms
- **Min time**: 1.2 ms
- **Max time**: 8.0 ms
- **Std dev**: 1.4 ms
- **Rounds**: 153

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 812.7 μs
- **Min time**: 655.2 μs
- **Max time**: 3.6 ms
- **Std dev**: 411.7 μs
- **Rounds**: 218

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Realgrid

- **Mean time**: 4.15 s
- **Min time**: 4.02 s
- **Max time**: 4.38 s
- **Std dev**: 133.9 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: realgrid
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
