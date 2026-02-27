# Benchmark Report

**Generated from**: `results/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.48 s
- **Min time**: 1.48 s
- **Max time**: 1.49 s
- **Std dev**: 7.7 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 513.6
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

- **Mean time**: 15.4 ms
- **Min time**: 14.1 ms
- **Max time**: 19.5 ms
- **Std dev**: 1.1 ms
- **Rounds**: 64

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 14.5 ms
- **Min time**: 13.5 ms
- **Max time**: 16.5 ms
- **Std dev**: 559.1 μs
- **Rounds**: 72

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 44.1 ms
- **Min time**: 42.3 ms
- **Max time**: 47.1 ms
- **Std dev**: 1.5 ms
- **Rounds**: 23

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 14.4 ms
- **Min time**: 13.9 ms
- **Max time**: 17.5 ms
- **Std dev**: 495.5 μs
- **Rounds**: 71

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4
