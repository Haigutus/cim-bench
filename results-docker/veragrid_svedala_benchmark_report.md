# Benchmark Report

**Generated from**: `results-docker/veragrid_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Veragrid Load Svedala

- **Mean time**: 921.0 ms
- **Min time**: 646.6 ms
- **Max time**: 1.15 s
- **Std dev**: 247.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 664.7
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Cgmes Version: UNSERIALIZABLE[3.0.0]
- Total Size Mb: 7.3
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Lines

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.8 μs
- **Std dev**: 0.0 μs
- **Rounds**: 112778

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Generators

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.6 μs
- **Std dev**: 0.0 μs
- **Rounds**: 90417

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Loads

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 9.1 μs
- **Std dev**: 0.1 μs
- **Rounds**: 199602

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.8 μs
- **Std dev**: 0.0 μs
- **Rounds**: 198021

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c
