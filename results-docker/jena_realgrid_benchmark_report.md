# Benchmark Report

**Generated from**: `results-docker/jena_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Jena Load Realgrid

- **Mean time**: 1.58 s
- **Min time**: 1.55 s
- **Max time**: 1.61 s
- **Std dev**: 25.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2586.6
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

- **Mean time**: 203.5 ms
- **Min time**: 164.9 ms
- **Max time**: 316.0 ms
- **Std dev**: 63.9 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 519.2 μs
- **Min time**: 426.5 μs
- **Max time**: 2.6 ms
- **Std dev**: 196.3 μs
- **Rounds**: 236

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 4.9 ms
- **Min time**: 1.4 ms
- **Max time**: 126.8 ms
- **Std dev**: 14.2 ms
- **Rounds**: 77

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 864.4 μs
- **Min time**: 710.0 μs
- **Max time**: 3.0 ms
- **Std dev**: 261.4 μs
- **Rounds**: 353

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Realgrid

- **Mean time**: 4.29 s
- **Min time**: 4.26 s
- **Max time**: 4.35 s
- **Std dev**: 31.5 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: realgrid
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
