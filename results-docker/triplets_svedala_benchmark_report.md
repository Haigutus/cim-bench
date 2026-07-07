# Benchmark Report

**Generated from**: `results-docker/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 329.5 ms
- **Min time**: 309.7 ms
- **Max time**: 359.0 ms
- **Std dev**: 18.4 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 27.6
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
- Library Version: 0.1.0
- Library Dependencies: {'pandas': '3.0.3', 'lxml': '6.1.1'}
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4
- Tags: ['parser', 'serializer', 'query', 'python']

### Triplets Get Lines

- **Mean time**: 30.1 ms
- **Min time**: 26.8 ms
- **Max time**: 38.2 ms
- **Std dev**: 2.5 ms
- **Rounds**: 31

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 29.3 ms
- **Min time**: 24.1 ms
- **Max time**: 39.7 ms
- **Std dev**: 3.5 ms
- **Rounds**: 35

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 44.3 ms
- **Min time**: 38.0 ms
- **Max time**: 54.6 ms
- **Std dev**: 4.4 ms
- **Rounds**: 22

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 28.5 ms
- **Min time**: 24.2 ms
- **Max time**: 34.1 ms
- **Std dev**: 2.5 ms
- **Rounds**: 36

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Svedala

- **Mean time**: 930.9 ms
- **Min time**: 889.2 ms
- **Max time**: 1.01 s
- **Std dev**: 48.8 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: svedala
- Operation: export
- Display Name: triplets
- Color: #1f77b4
