# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.55 s
- **Min time**: 1.40 s
- **Max time**: 1.68 s
- **Std dev**: 103.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 594.4
- Triplets Count: 1146215
- Unique Objects: 149174
- Instances: 4
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Lines

- **Mean time**: 67.3 ms
- **Min time**: 64.9 ms
- **Max time**: 69.7 ms
- **Std dev**: 1.6 ms
- **Rounds**: 8

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 64.8 ms
- **Min time**: 63.5 ms
- **Max time**: 66.0 ms
- **Std dev**: 748.4 μs
- **Rounds**: 16

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 196.8 ms
- **Min time**: 196.1 ms
- **Max time**: 198.3 ms
- **Std dev**: 808.0 μs
- **Rounds**: 6

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 66.5 ms
- **Min time**: 65.2 ms
- **Max time**: 67.9 ms
- **Std dev**: 807.7 μs
- **Rounds**: 15

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4
