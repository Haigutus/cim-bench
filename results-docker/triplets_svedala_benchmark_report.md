# Benchmark Report

**Generated from**: `results-docker/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 21.8 ms
- **Min time**: 16.4 ms
- **Max time**: 28.9 ms
- **Std dev**: 4.2 ms
- **Rounds**: 15

**Metrics**:
- Memory Mb: 36.5
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

- **Mean time**: 21.3 ms
- **Min time**: 15.0 ms
- **Max time**: 30.8 ms
- **Std dev**: 4.4 ms
- **Rounds**: 37

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 21.8 ms
- **Min time**: 15.9 ms
- **Max time**: 30.9 ms
- **Std dev**: 4.4 ms
- **Rounds**: 59

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 35.4 ms
- **Min time**: 27.5 ms
- **Max time**: 48.9 ms
- **Std dev**: 5.5 ms
- **Rounds**: 29

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 20.2 ms
- **Min time**: 14.2 ms
- **Max time**: 34.7 ms
- **Std dev**: 5.1 ms
- **Rounds**: 41

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Svedala

- **Mean time**: 397.7 ms
- **Min time**: 341.9 ms
- **Max time**: 465.3 ms
- **Std dev**: 49.7 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: svedala
- Operation: export
- Display Name: triplets
- Color: #1f77b4
