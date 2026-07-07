# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 368.1 ms
- **Min time**: 257.0 ms
- **Max time**: 498.1 ms
- **Std dev**: 87.4 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 391.9
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
- Tags: ['parser', 'serializer', 'query', 'triplestore', 'java']

### Jena Get Lines

- **Mean time**: 1.2 ms
- **Min time**: 556.4 μs
- **Max time**: 6.6 ms
- **Std dev**: 727.6 μs
- **Rounds**: 234

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 474.1 μs
- **Min time**: 183.0 μs
- **Max time**: 6.2 ms
- **Std dev**: 388.0 μs
- **Rounds**: 1245

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 927.0 μs
- **Min time**: 445.1 μs
- **Max time**: 2.8 ms
- **Std dev**: 307.5 μs
- **Rounds**: 526

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 261.5 μs
- **Min time**: 143.7 μs
- **Max time**: 3.6 ms
- **Std dev**: 136.2 μs
- **Rounds**: 1387

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Svedala

- **Mean time**: 1.07 s
- **Min time**: 990.8 ms
- **Max time**: 1.18 s
- **Std dev**: 87.1 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: svedala
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
