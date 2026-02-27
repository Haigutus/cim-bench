# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.35 s
- **Min time**: 1.22 s
- **Max time**: 1.43 s
- **Std dev**: 87.4 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 593.9
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

- **Mean time**: 64.5 ms
- **Min time**: 63.7 ms
- **Max time**: 65.3 ms
- **Std dev**: 490.4 μs
- **Rounds**: 9

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 64.6 ms
- **Min time**: 64.0 ms
- **Max time**: 65.3 ms
- **Std dev**: 392.2 μs
- **Rounds**: 16

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 193.8 ms
- **Min time**: 193.0 ms
- **Max time**: 195.6 ms
- **Std dev**: 939.1 μs
- **Rounds**: 6

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 64.4 ms
- **Min time**: 63.2 ms
- **Max time**: 65.7 ms
- **Std dev**: 584.3 μs
- **Rounds**: 16

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4
