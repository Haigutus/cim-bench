# Benchmark Report

**Generated from**: `results-docker/jena_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Jena Load Realgrid

- **Mean time**: 3.23 s
- **Min time**: 2.90 s
- **Max time**: 3.63 s
- **Std dev**: 336.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3352.6
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

- **Mean time**: 9.9 ms
- **Min time**: 5.8 ms
- **Max time**: 20.3 ms
- **Std dev**: 2.9 ms
- **Rounds**: 50

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 2.4 ms
- **Min time**: 1.1 ms
- **Max time**: 5.7 ms
- **Std dev**: 857.5 μs
- **Rounds**: 160

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 13.2 ms
- **Min time**: 3.8 ms
- **Max time**: 136.8 ms
- **Std dev**: 17.5 ms
- **Rounds**: 54

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 2.8 ms
- **Min time**: 1.8 ms
- **Max time**: 7.8 ms
- **Std dev**: 1.2 ms
- **Rounds**: 172

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Realgrid

- **Mean time**: 6.13 s
- **Min time**: 4.84 s
- **Max time**: 7.55 s
- **Std dev**: 1.21 s
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: realgrid
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
