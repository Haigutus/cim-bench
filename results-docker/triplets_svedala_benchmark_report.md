# Benchmark Report

**Generated from**: `results-docker/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 10.1 ms
- **Min time**: 7.7 ms
- **Max time**: 13.9 ms
- **Std dev**: 1.9 ms
- **Rounds**: 18

**Metrics**:
- Memory Mb: 82.9
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

- **Mean time**: 1.7 ms
- **Min time**: 1.1 ms
- **Max time**: 3.1 ms
- **Std dev**: 286.5 μs
- **Rounds**: 367

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 1.5 ms
- **Min time**: 1.1 ms
- **Max time**: 2.9 ms
- **Std dev**: 205.6 μs
- **Rounds**: 577

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 1.7 ms
- **Min time**: 1.2 ms
- **Max time**: 2.9 ms
- **Std dev**: 323.2 μs
- **Rounds**: 479

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 1.0 ms
- **Min time**: 739.6 μs
- **Max time**: 1.9 ms
- **Std dev**: 178.1 μs
- **Rounds**: 882

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Svedala

- **Mean time**: 147.8 ms
- **Min time**: 136.5 ms
- **Max time**: 153.1 ms
- **Std dev**: 5.4 ms
- **Rounds**: 7

**Metrics**:
- Library: triplets
- Dataset: svedala
- Operation: export
- Display Name: triplets
- Color: #1f77b4
