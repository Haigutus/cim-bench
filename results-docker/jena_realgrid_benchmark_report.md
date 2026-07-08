# Benchmark Report

**Generated from**: `results-docker/jena_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Jena Load Realgrid

- **Mean time**: 2.05 s
- **Min time**: 1.77 s
- **Max time**: 2.52 s
- **Std dev**: 310.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3942.1
- Triples: 892139
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: jena
- Library Version: 6.0.0
- Library Dependencies: {'jpype1': '1.7.1', 'java': '21.0.11'}
- Java Version: 21.0.11
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'java']

### Jena Get Lines

- **Mean time**: 7.9 ms
- **Min time**: 3.9 ms
- **Max time**: 31.7 ms
- **Std dev**: 4.3 ms
- **Rounds**: 94

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 1.7 ms
- **Min time**: 917.4 μs
- **Max time**: 3.9 ms
- **Std dev**: 496.5 μs
- **Rounds**: 189

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 12.2 ms
- **Min time**: 5.5 ms
- **Max time**: 23.8 ms
- **Std dev**: 4.8 ms
- **Rounds**: 26

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 2.9 ms
- **Min time**: 2.0 ms
- **Max time**: 9.3 ms
- **Std dev**: 1.1 ms
- **Rounds**: 143

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Realgrid

- **Mean time**: 5.88 s
- **Min time**: 4.77 s
- **Max time**: 7.79 s
- **Std dev**: 1.24 s
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: realgrid
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
