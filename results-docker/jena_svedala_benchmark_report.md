# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 132.0 ms
- **Min time**: 126.9 ms
- **Max time**: 141.7 ms
- **Std dev**: 5.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 721.1
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

- **Mean time**: 339.6 μs
- **Min time**: 175.6 μs
- **Max time**: 1.5 ms
- **Std dev**: 166.0 μs
- **Rounds**: 553

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 112.6 μs
- **Min time**: 71.5 μs
- **Max time**: 963.4 μs
- **Std dev**: 55.9 μs
- **Rounds**: 2783

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 365.6 μs
- **Min time**: 196.1 μs
- **Max time**: 64.8 ms
- **Std dev**: 2.0 ms
- **Rounds**: 1643

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 138.5 μs
- **Min time**: 49.8 μs
- **Max time**: 155.1 ms
- **Std dev**: 2.8 ms
- **Rounds**: 3553

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728
