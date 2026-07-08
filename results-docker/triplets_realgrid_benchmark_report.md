# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 505.2 ms
- **Min time**: 452.4 ms
- **Max time**: 562.1 ms
- **Std dev**: 49.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 241.0
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

- **Mean time**: 181.0 ms
- **Min time**: 170.0 ms
- **Max time**: 190.0 ms
- **Std dev**: 8.8 ms
- **Rounds**: 6

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 142.7 ms
- **Min time**: 128.9 ms
- **Max time**: 153.7 ms
- **Std dev**: 7.9 ms
- **Rounds**: 8

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 222.8 ms
- **Min time**: 215.2 ms
- **Max time**: 235.0 ms
- **Std dev**: 8.5 ms
- **Rounds**: 5

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 132.6 ms
- **Min time**: 119.6 ms
- **Max time**: 140.1 ms
- **Std dev**: 7.5 ms
- **Rounds**: 8

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Realgrid

- **Mean time**: 2.49 s
- **Min time**: 2.34 s
- **Max time**: 2.59 s
- **Std dev**: 90.7 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: realgrid
- Operation: export
- Display Name: triplets
- Color: #1f77b4
