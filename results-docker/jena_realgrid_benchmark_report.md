# Benchmark Report

**Generated from**: `results-docker/jena_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.8-200.fc43.x86_64

## Results

### Jena Load Realgrid

- **Mean time**: 1.77 s
- **Min time**: 1.57 s
- **Max time**: 1.88 s
- **Std dev**: 119.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3938.4
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

- **Mean time**: 1.7 ms
- **Min time**: 992.8 μs
- **Max time**: 4.7 ms
- **Std dev**: 728.5 μs
- **Rounds**: 228

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 359.4 μs
- **Min time**: 187.6 μs
- **Max time**: 2.4 ms
- **Std dev**: 172.1 μs
- **Rounds**: 638

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 1.3 ms
- **Min time**: 859.9 μs
- **Max time**: 5.2 ms
- **Std dev**: 584.6 μs
- **Rounds**: 225

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 558.4 μs
- **Min time**: 410.5 μs
- **Max time**: 25.3 ms
- **Std dev**: 804.0 μs
- **Rounds**: 976

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: jena
- Dataset: realgrid
- Display Name: Apache Jena
- Color: #d62728
