# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 124.1 ms
- **Min time**: 107.2 ms
- **Max time**: 162.6 ms
- **Std dev**: 22.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 427.9
- Triples: 47710
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: jena
- Library Version: 6.0.0
- Library Dependencies: {'jpype1': '1.6.0', 'java': '21.0.10'}
- Java Version: 21.0.10
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Lines

- **Mean time**: 380.6 μs
- **Min time**: 139.2 μs
- **Max time**: 20.9 ms
- **Std dev**: 865.5 μs
- **Rounds**: 595

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 104.2 μs
- **Min time**: 65.6 μs
- **Max time**: 1.8 ms
- **Std dev**: 58.3 μs
- **Rounds**: 2673

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 205.3 μs
- **Min time**: 169.8 μs
- **Max time**: 13.7 ms
- **Std dev**: 359.6 μs
- **Rounds**: 1420

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 109.8 μs
- **Min time**: 48.2 μs
- **Max time**: 73.9 ms
- **Std dev**: 1.2 ms
- **Rounds**: 3993

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Svedala

- **Mean time**: 434.9 ms
- **Min time**: 410.2 ms
- **Max time**: 522.2 ms
- **Std dev**: 48.9 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: svedala
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
