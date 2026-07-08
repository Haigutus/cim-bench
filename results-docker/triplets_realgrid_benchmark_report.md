# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 448.1 ms
- **Min time**: 404.4 ms
- **Max time**: 474.4 ms
- **Std dev**: 28.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 226.1
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
- Library Dependencies: {'pandas': '3.0.3', 'lxml': '6.1.1'}
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4
- Tags: ['parser', 'serializer', 'query', 'python']

### Triplets Get Lines

- **Mean time**: 174.5 ms
- **Min time**: 132.1 ms
- **Max time**: 220.8 ms
- **Std dev**: 34.0 ms
- **Rounds**: 6

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 189.4 ms
- **Min time**: 139.7 ms
- **Max time**: 218.9 ms
- **Std dev**: 24.7 ms
- **Rounds**: 9

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 230.1 ms
- **Min time**: 168.7 ms
- **Max time**: 273.7 ms
- **Std dev**: 45.7 ms
- **Rounds**: 5

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 157.9 ms
- **Min time**: 136.8 ms
- **Max time**: 172.6 ms
- **Std dev**: 14.5 ms
- **Rounds**: 7

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Realgrid

- **Mean time**: 2.94 s
- **Min time**: 2.86 s
- **Max time**: 3.01 s
- **Std dev**: 57.2 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: realgrid
- Operation: export
- Display Name: triplets
- Color: #1f77b4
