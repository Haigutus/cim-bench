# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 131.7 ms
- **Min time**: 115.9 ms
- **Max time**: 155.4 ms
- **Std dev**: 17.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 387.1
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

- **Mean time**: 280.0 μs
- **Min time**: 150.7 μs
- **Max time**: 1.6 ms
- **Std dev**: 138.1 μs
- **Rounds**: 557

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 100.3 μs
- **Min time**: 59.1 μs
- **Max time**: 22.9 ms
- **Std dev**: 491.7 μs
- **Rounds**: 3319

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 268.9 μs
- **Min time**: 132.3 μs
- **Max time**: 66.9 ms
- **Std dev**: 1.4 ms
- **Rounds**: 2538

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 57.6 μs
- **Min time**: 42.3 μs
- **Max time**: 11.9 ms
- **Std dev**: 263.9 μs
- **Rounds**: 6625

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Svedala

- **Mean time**: 311.2 ms
- **Min time**: 298.3 ms
- **Max time**: 325.5 ms
- **Std dev**: 13.0 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: svedala
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
