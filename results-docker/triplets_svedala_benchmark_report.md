# Benchmark Report

**Generated from**: `results-docker/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 116.1 ms
- **Min time**: 101.8 ms
- **Max time**: 121.3 ms
- **Std dev**: 6.1 ms
- **Rounds**: 11

**Metrics**:
- Memory Mb: 43.2
- Triplets Count: 95539
- Unique Objects: 14540
- Instances: 5
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Total Size Mb: 7.3
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Lines

- **Mean time**: 21.1 ms
- **Min time**: 20.2 ms
- **Max time**: 29.2 ms
- **Std dev**: 1.3 ms
- **Rounds**: 46

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 21.1 ms
- **Min time**: 20.4 ms
- **Max time**: 22.1 ms
- **Std dev**: 423.7 μs
- **Rounds**: 45

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 41.3 ms
- **Min time**: 39.8 ms
- **Max time**: 44.1 ms
- **Std dev**: 1.0 ms
- **Rounds**: 22

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 20.7 ms
- **Min time**: 19.8 ms
- **Max time**: 22.0 ms
- **Std dev**: 488.3 μs
- **Rounds**: 44

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4
