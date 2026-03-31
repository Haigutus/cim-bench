# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 136.8 ms
- **Min time**: 102.8 ms
- **Max time**: 157.0 ms
- **Std dev**: 20.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 692.0
- Triples: 47710
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Total Size Mb: 7.3
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Lines

- **Mean time**: 350.6 μs
- **Min time**: 123.6 μs
- **Max time**: 17.2 ms
- **Std dev**: 660.9 μs
- **Rounds**: 746

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 89.0 μs
- **Min time**: 65.2 μs
- **Max time**: 1.4 ms
- **Std dev**: 47.5 μs
- **Rounds**: 3806

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 239.6 μs
- **Min time**: 150.9 μs
- **Max time**: 24.4 ms
- **Std dev**: 623.8 μs
- **Rounds**: 2069

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 56.5 μs
- **Min time**: 42.7 μs
- **Max time**: 20.7 ms
- **Std dev**: 274.9 μs
- **Rounds**: 5708

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728
