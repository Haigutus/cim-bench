# Benchmark Report

**Generated from**: `results-docker/jena_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Jena Load Realgrid

- **Mean time**: 1.59 s
- **Min time**: 1.58 s
- **Max time**: 1.62 s
- **Std dev**: 17.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2525.7
- Triples: 892139
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: jena
- Library Version: 6.0.0
- Library Dependencies: {'jpype1': '1.6.0', 'java': '21.0.10'}
- Java Version: 21.0.10
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Lines

- **Mean time**: 3.0 ms
- **Min time**: 1.7 ms
- **Max time**: 9.0 ms
- **Std dev**: 1.4 ms
- **Rounds**: 86

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 565.1 μs
- **Min time**: 351.6 μs
- **Max time**: 25.8 ms
- **Std dev**: 1.2 ms
- **Rounds**: 462

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 2.4 ms
- **Min time**: 1.3 ms
- **Max time**: 6.4 ms
- **Std dev**: 1.2 ms
- **Rounds**: 134

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 894.9 μs
- **Min time**: 769.1 μs
- **Max time**: 3.8 ms
- **Std dev**: 243.4 μs
- **Rounds**: 268

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Export Realgrid

- **Mean time**: 4.38 s
- **Min time**: 4.29 s
- **Max time**: 4.49 s
- **Std dev**: 77.1 ms
- **Rounds**: 5

**Metrics**:
- Library: jena
- Dataset: realgrid
- Operation: export
- Display Name: Apache Jena
- Color: #d62728
