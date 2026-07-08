# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 343.5 ms
- **Min time**: 313.3 ms
- **Max time**: 432.1 ms
- **Std dev**: 50.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 492.5
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
- **Min time**: 497.0 μs
- **Max time**: 3.9 ms
- **Std dev**: 599.1 μs
- **Rounds**: 265

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 467.3 μs
- **Min time**: 186.7 μs
- **Max time**: 5.1 ms
- **Std dev**: 367.5 μs
- **Rounds**: 1208

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 897.0 μs
- **Min time**: 385.9 μs
- **Max time**: 44.4 ms
- **Std dev**: 1.5 ms
- **Rounds**: 905

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 238.7 μs
- **Min time**: 135.6 μs
- **Max time**: 1.0 ms
- **Std dev**: 93.8 μs
- **Rounds**: 3000

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Svedala

- **Mean time**: 1.40 s
- **Min time**: 1.17 s
- **Max time**: 1.65 s
- **Std dev**: 216.3 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: svedala
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
