# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 159.1 ms
- **Min time**: 156.6 ms
- **Max time**: 164.7 ms
- **Std dev**: 3.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 370.5
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

- **Mean time**: 12.6 ms
- **Min time**: 11.6 ms
- **Max time**: 15.5 ms
- **Std dev**: 786.2 μs
- **Rounds**: 68

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 7.4 ms
- **Min time**: 6.4 ms
- **Max time**: 9.2 ms
- **Std dev**: 483.9 μs
- **Rounds**: 106

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 11.2 ms
- **Min time**: 9.8 ms
- **Max time**: 13.7 ms
- **Std dev**: 923.2 μs
- **Rounds**: 95

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 6.4 ms
- **Min time**: 5.4 ms
- **Max time**: 8.3 ms
- **Std dev**: 444.4 μs
- **Rounds**: 171

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Realgrid

- **Mean time**: 946.1 ms
- **Min time**: 938.4 ms
- **Max time**: 963.4 ms
- **Std dev**: 9.9 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: realgrid
- Operation: export
- Display Name: triplets
- Color: #1f77b4
