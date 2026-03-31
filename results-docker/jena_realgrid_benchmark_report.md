# Benchmark Report

**Generated from**: `results-docker/jena_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Jena Load Realgrid

- **Mean time**: 1.58 s
- **Min time**: 1.52 s
- **Max time**: 1.62 s
- **Std dev**: 44.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 5105.4
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

- **Mean time**: 1.6 ms
- **Min time**: 939.1 μs
- **Max time**: 41.7 ms
- **Std dev**: 3.0 ms
- **Rounds**: 186

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 291.1 μs
- **Min time**: 169.9 μs
- **Max time**: 30.5 ms
- **Std dev**: 842.0 μs
- **Rounds**: 1317

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 1.0 ms
- **Min time**: 805.5 μs
- **Max time**: 2.8 ms
- **Std dev**: 232.5 μs
- **Rounds**: 345

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 498.9 μs
- **Min time**: 437.6 μs
- **Max time**: 1.5 ms
- **Std dev**: 97.9 μs
- **Rounds**: 623

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728
