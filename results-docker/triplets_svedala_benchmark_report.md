# Benchmark Report

**Generated from**: `results-docker/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 118.0 ms
- **Min time**: 102.1 ms
- **Max time**: 124.3 ms
- **Std dev**: 6.7 ms
- **Rounds**: 11

**Metrics**:
- Memory Mb: 43.3
- Triplets Count: 95539
- Unique Objects: 14540
- Instances: 5
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: triplets
- Library Version: 0.0.17
- Library Dependencies: {'pandas': '3.0.2', 'lxml': '6.0.2', 'aniso8601': '10.0.1'}
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Lines

- **Mean time**: 21.2 ms
- **Min time**: 20.3 ms
- **Max time**: 25.7 ms
- **Std dev**: 835.8 μs
- **Rounds**: 47

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 21.4 ms
- **Min time**: 20.8 ms
- **Max time**: 23.2 ms
- **Std dev**: 449.7 μs
- **Rounds**: 41

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 42.7 ms
- **Min time**: 40.7 ms
- **Max time**: 46.8 ms
- **Std dev**: 1.7 ms
- **Rounds**: 22

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 21.0 ms
- **Min time**: 19.8 ms
- **Max time**: 25.5 ms
- **Std dev**: 955.7 μs
- **Rounds**: 46

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Svedala

- **Mean time**: 607.4 ms
- **Min time**: 580.8 ms
- **Max time**: 623.8 ms
- **Std dev**: 16.2 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: svedala
- Operation: export
- Display Name: triplets
- Color: #1f77b4
