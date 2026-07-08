# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 259.7 ms
- **Min time**: 213.2 ms
- **Max time**: 303.0 ms
- **Std dev**: 37.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 495.6
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

- **Mean time**: 1.1 ms
- **Min time**: 445.3 μs
- **Max time**: 3.6 ms
- **Std dev**: 457.3 μs
- **Rounds**: 317

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 452.2 μs
- **Min time**: 159.0 μs
- **Max time**: 3.1 ms
- **Std dev**: 340.9 μs
- **Rounds**: 846

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 792.3 μs
- **Min time**: 376.2 μs
- **Max time**: 24.4 ms
- **Std dev**: 787.6 μs
- **Rounds**: 1024

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 230.9 μs
- **Min time**: 122.8 μs
- **Max time**: 1.7 ms
- **Std dev**: 95.6 μs
- **Rounds**: 2753

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Svedala

- **Mean time**: 832.2 ms
- **Min time**: 749.2 ms
- **Max time**: 940.5 ms
- **Std dev**: 79.0 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: svedala
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
