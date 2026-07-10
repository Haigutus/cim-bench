# Benchmark Report

**Generated from**: `results-docker/jena_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Jena Load Realgrid

- **Mean time**: 1.60 s
- **Min time**: 1.53 s
- **Max time**: 1.63 s
- **Std dev**: 38.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2208.8
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

- **Mean time**: 3.5 ms
- **Min time**: 1.3 ms
- **Max time**: 73.6 ms
- **Std dev**: 7.7 ms
- **Rounds**: 91

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 506.0 μs
- **Min time**: 353.2 μs
- **Max time**: 1.4 ms
- **Std dev**: 159.7 μs
- **Rounds**: 336

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 1.9 ms
- **Min time**: 1.3 ms
- **Max time**: 7.5 ms
- **Std dev**: 937.9 μs
- **Rounds**: 98

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 866.7 μs
- **Min time**: 765.4 μs
- **Max time**: 2.0 ms
- **Std dev**: 158.9 μs
- **Rounds**: 341

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Realgrid

- **Mean time**: 4.35 s
- **Min time**: 4.27 s
- **Max time**: 4.47 s
- **Std dev**: 89.0 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: realgrid
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
