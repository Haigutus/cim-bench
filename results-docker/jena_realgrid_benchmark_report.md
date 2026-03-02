# Benchmark Report

**Generated from**: `results-docker/jena_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Jena Load Realgrid

- **Mean time**: 1.57 s
- **Min time**: 1.51 s
- **Max time**: 1.63 s
- **Std dev**: 47.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3928.2
- Triples: 892139
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Lines

- **Mean time**: 1.9 ms
- **Min time**: 903.4 μs
- **Max time**: 60.7 ms
- **Std dev**: 4.4 ms
- **Rounds**: 182

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 382.1 μs
- **Min time**: 222.7 μs
- **Max time**: 39.2 ms
- **Std dev**: 1.2 ms
- **Rounds**: 1036

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 1.2 ms
- **Min time**: 969.4 μs
- **Max time**: 3.6 ms
- **Std dev**: 385.8 μs
- **Rounds**: 337

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 635.2 μs
- **Min time**: 563.0 μs
- **Max time**: 2.3 ms
- **Std dev**: 145.9 μs
- **Rounds**: 692

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728
