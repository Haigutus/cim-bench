# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.45 s
- **Min time**: 1.31 s
- **Max time**: 1.53 s
- **Std dev**: 86.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 593.6
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

- **Mean time**: 339.3 ms
- **Min time**: 326.6 ms
- **Max time**: 354.8 ms
- **Std dev**: 13.9 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 278.2 ms
- **Min time**: 276.4 ms
- **Max time**: 280.5 ms
- **Std dev**: 1.6 ms
- **Rounds**: 5

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 655.3 ms
- **Min time**: 647.8 ms
- **Max time**: 668.3 ms
- **Std dev**: 7.7 ms
- **Rounds**: 5

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 263.9 ms
- **Min time**: 258.7 ms
- **Max time**: 271.3 ms
- **Std dev**: 5.1 ms
- **Rounds**: 5

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4
