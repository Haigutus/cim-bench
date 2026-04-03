# Benchmark Report

**Generated from**: `results-docker/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.36 s
- **Min time**: 1.22 s
- **Max time**: 1.43 s
- **Std dev**: 88.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 591.3
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
- Library Version: 0.0.17
- Library Dependencies: {'pandas': '3.0.2', 'lxml': '6.0.2', 'aniso8601': '10.0.1'}
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Lines

- **Mean time**: 306.5 ms
- **Min time**: 304.2 ms
- **Max time**: 308.9 ms
- **Std dev**: 1.8 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 268.8 ms
- **Min time**: 265.7 ms
- **Max time**: 273.2 ms
- **Std dev**: 3.3 ms
- **Rounds**: 5

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 625.7 ms
- **Min time**: 615.9 ms
- **Max time**: 640.1 ms
- **Std dev**: 9.9 ms
- **Rounds**: 5

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 254.6 ms
- **Min time**: 250.6 ms
- **Max time**: 263.8 ms
- **Std dev**: 5.3 ms
- **Rounds**: 5

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
- Display Name: triplets
- Color: #1f77b4

### Triplets Export Realgrid

- **Mean time**: 5.78 s
- **Min time**: 5.69 s
- **Max time**: 5.91 s
- **Std dev**: 82.4 ms
- **Rounds**: 5

**Metrics**:
- Library: triplets
- Dataset: realgrid
- Operation: export
- Display Name: triplets
- Color: #1f77b4
