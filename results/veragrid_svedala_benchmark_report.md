# Benchmark Report

**Generated from**: `results/veragrid_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Veragrid Load Svedala

- **Mean time**: 1.43 s
- **Min time**: 1.15 s
- **Max time**: 1.70 s
- **Std dev**: 277.8 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 603.5
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
- **Max time**: 1.0 μs
- **Std dev**: 0.0 μs
- **Rounds**: 198021

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Generators

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 91989

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
- **Max time**: 7.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 156446

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 126823

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c
