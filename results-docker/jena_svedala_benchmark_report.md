# Benchmark Report

**Generated from**: `results-docker/jena_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.8-200.fc43.x86_64

## Results

### Jena Load Svedala

- **Mean time**: 147.6 ms
- **Min time**: 136.6 ms
- **Max time**: 162.7 ms
- **Std dev**: 12.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 768.4
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

- **Mean time**: 306.6 μs
- **Min time**: 144.3 μs
- **Max time**: 3.4 ms
- **Std dev**: 195.8 μs
- **Rounds**: 740

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Generators

- **Mean time**: 94.7 μs
- **Min time**: 64.2 μs
- **Max time**: 18.6 ms
- **Std dev**: 294.7 μs
- **Rounds**: 4063

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Loads

- **Mean time**: 264.0 μs
- **Min time**: 151.3 μs
- **Max time**: 73.8 ms
- **Std dev**: 1.6 ms
- **Rounds**: 2099

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728

### Jena Get Substations

- **Mean time**: 93.6 μs
- **Min time**: 53.5 μs
- **Max time**: 23.3 ms
- **Std dev**: 363.9 μs
- **Rounds**: 4558

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: jena
- Dataset: svedala
- Display Name: Apache Jena
- Color: #d62728
