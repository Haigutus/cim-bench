# Benchmark Report

**Generated from**: `results-docker/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 123.5 ms
- **Min time**: 107.1 ms
- **Max time**: 139.3 ms
- **Std dev**: 8.6 ms
- **Rounds**: 10

**Metrics**:
- Memory Mb: 44.6
- Triplets Count: 95539
- Unique Objects: 14540
- Instances: 5
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Total Size Mb: 7.3
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Lines

- **Mean time**: 5.8 ms
- **Min time**: 5.1 ms
- **Max time**: 7.2 ms
- **Std dev**: 467.6 μs
- **Rounds**: 78

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 5.9 ms
- **Min time**: 5.1 ms
- **Max time**: 8.4 ms
- **Std dev**: 422.9 μs
- **Rounds**: 163

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 16.4 ms
- **Min time**: 14.9 ms
- **Max time**: 22.4 ms
- **Std dev**: 1.3 ms
- **Rounds**: 50

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 5.7 ms
- **Min time**: 4.9 ms
- **Max time**: 9.7 ms
- **Std dev**: 676.5 μs
- **Rounds**: 158

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4
