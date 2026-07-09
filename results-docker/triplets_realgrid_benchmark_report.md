# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 178.3 ms
- **Min time**: 171.4 ms
- **Max time**: 187.7 ms
- **Std dev**: 6.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 382.3
- Triplets Count: 1146215
- Unique Objects: 149174
- Instances: 4
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: triplets
- Library Version: 0.1.0
- Library Dependencies: {'pandas': '3.0.3', 'lxml': '6.1.1', 'polars': '1.42.1', 'pyarrow': '24.0.0'}
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4
- Tags: ['parser', 'serializer', 'query', 'python']

### Triplets Get Lines

- **Mean time**: 36.2 ms
- **Min time**: 26.1 ms
- **Max time**: 42.4 ms
- **Std dev**: 2.9 ms
- **Rounds**: 45

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 23.8 ms
- **Min time**: 22.0 ms
- **Max time**: 28.3 ms
- **Std dev**: 1.3 ms
- **Rounds**: 43

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 30.9 ms
- **Min time**: 27.9 ms
- **Max time**: 34.3 ms
- **Std dev**: 1.5 ms
- **Rounds**: 32

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 19.0 ms
- **Min time**: 16.6 ms
- **Max time**: 23.4 ms
- **Std dev**: 1.4 ms
- **Rounds**: 53

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Realgrid

- **Mean time**: 2.02 s
- **Min time**: 1.96 s
- **Max time**: 2.09 s
- **Std dev**: 55.4 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: realgrid
- Operation: export
- Display Name: triplets
- Color: #1f77b4
