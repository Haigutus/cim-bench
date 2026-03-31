# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.35 s
- **Min time**: 1.22 s
- **Max time**: 1.42 s
- **Std dev**: 85.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 594.6
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

- **Mean time**: 325.0 ms
- **Min time**: 304.5 ms
- **Max time**: 357.4 ms
- **Std dev**: 20.6 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 274.7 ms
- **Min time**: 261.8 ms
- **Max time**: 291.5 ms
- **Std dev**: 12.6 ms
- **Rounds**: 5

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 645.5 ms
- **Min time**: 614.6 ms
- **Max time**: 715.3 ms
- **Std dev**: 42.8 ms
- **Rounds**: 5

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 246.3 ms
- **Min time**: 240.7 ms
- **Max time**: 255.6 ms
- **Std dev**: 5.6 ms
- **Rounds**: 5

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4
