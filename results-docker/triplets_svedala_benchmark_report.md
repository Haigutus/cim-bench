# Benchmark Report

**Generated from**: `results-docker/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 138.1 ms
- **Min time**: 127.7 ms
- **Max time**: 144.6 ms
- **Std dev**: 6.0 ms
- **Rounds**: 9

**Metrics**:
- Memory Mb: 44.2
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

- **Mean time**: 6.1 ms
- **Min time**: 5.3 ms
- **Max time**: 8.0 ms
- **Std dev**: 533.0 μs
- **Rounds**: 71

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Generators

- **Mean time**: 6.5 ms
- **Min time**: 5.6 ms
- **Max time**: 8.3 ms
- **Std dev**: 553.1 μs
- **Rounds**: 152

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Loads

- **Mean time**: 17.6 ms
- **Min time**: 15.9 ms
- **Max time**: 21.9 ms
- **Std dev**: 1.4 ms
- **Rounds**: 38

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4

### Triplets Get Substations

- **Mean time**: 5.7 ms
- **Min time**: 5.0 ms
- **Max time**: 7.9 ms
- **Std dev**: 393.3 μs
- **Rounds**: 169

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
- Display Name: triplets
- Color: #1f77b4
