# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 120.1 ms
- **Min time**: 106.5 ms
- **Max time**: 146.1 ms
- **Std dev**: 15.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 402.0
- Triples: 47710
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: jena
- Library Version: 6.0.0
- Library Dependencies: {'jpype1': '1.7.1', 'java': '21.0.11'}
- Java Version: 21.0.11
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'java']

### Jena Get Lines

- **Mean time**: 4.1 ms
- **Min time**: 2.1 ms
- **Max time**: 32.4 ms
- **Std dev**: 3.4 ms
- **Rounds**: 109

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 165.9 μs
- **Min time**: 65.7 μs
- **Max time**: 1.3 ms
- **Std dev**: 113.1 μs
- **Rounds**: 715

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 295.9 μs
- **Min time**: 131.8 μs
- **Max time**: 158.5 ms
- **Std dev**: 3.2 ms
- **Rounds**: 2572

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 64.3 μs
- **Min time**: 44.1 μs
- **Max time**: 9.0 ms
- **Std dev**: 115.1 μs
- **Rounds**: 6407

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Svedala

- **Mean time**: 403.1 ms
- **Min time**: 386.7 ms
- **Max time**: 434.4 ms
- **Std dev**: 18.4 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: svedala
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
