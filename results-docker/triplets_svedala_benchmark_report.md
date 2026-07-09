# Benchmark Report

**Generated from**: `results-docker/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 21.9 ms
- **Min time**: 17.6 ms
- **Max time**: 25.8 ms
- **Std dev**: 2.4 ms
- **Rounds**: 25

**Metrics**:
- Memory Mb: 90.4
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
- Library Dependencies: {'pandas': '3.0.3', 'lxml': '6.1.1', 'polars': '1.42.1', 'pyarrow': '24.0.0'}
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4
- Tags: ['parser', 'serializer', 'query', 'python']

### Triplets Get Lines

- **Mean time**: 6.7 ms
- **Min time**: 4.8 ms
- **Max time**: 13.7 ms
- **Std dev**: 1.3 ms
- **Rounds**: 147

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 5.9 ms
- **Min time**: 3.9 ms
- **Max time**: 8.7 ms
- **Std dev**: 822.0 μs
- **Rounds**: 153

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 6.7 ms
- **Min time**: 4.2 ms
- **Max time**: 10.8 ms
- **Std dev**: 1.1 ms
- **Rounds**: 149

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 5.1 ms
- **Min time**: 3.6 ms
- **Max time**: 10.5 ms
- **Std dev**: 1.0 ms
- **Rounds**: 200

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Svedala

- **Mean time**: 330.4 ms
- **Min time**: 301.3 ms
- **Max time**: 352.5 ms
- **Std dev**: 18.4 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: svedala
- Operation: export
- Display Name: triplets
- Color: #1f77b4
