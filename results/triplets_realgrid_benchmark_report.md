# Benchmark Report

**Generated from**: `results/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.60 s
- **Min time**: 1.58 s
- **Max time**: 1.62 s
- **Std dev**: 15.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 515.6
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

- **Mean time**: 19.9 ms
- **Min time**: 16.3 ms
- **Max time**: 24.4 ms
- **Std dev**: 1.8 ms
- **Rounds**: 54

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 19.4 ms
- **Min time**: 16.0 ms
- **Max time**: 26.2 ms
- **Std dev**: 2.0 ms
- **Rounds**: 47

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 55.2 ms
- **Min time**: 52.9 ms
- **Max time**: 56.5 ms
- **Std dev**: 1.0 ms
- **Rounds**: 21

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 19.0 ms
- **Min time**: 15.0 ms
- **Max time**: 28.8 ms
- **Std dev**: 2.5 ms
- **Rounds**: 54

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4
