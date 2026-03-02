# Benchmark Report

**Generated from**: `results/veragrid_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Veragrid Load Realgrid

- **Mean time**: 19.88 s
- **Min time**: 17.87 s
- **Max time**: 21.99 s
- **Std dev**: 1.67 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1890.3
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Cgmes Version: UNSERIALIZABLE[2.4.15]
- Dataset Size Mb: 86.5
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Lines

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.2 μs
- **Std dev**: 0.0 μs
- **Rounds**: 113033

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Generators

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.2 μs
- **Std dev**: 0.0 μs
- **Rounds**: 114456

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Loads

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 35.0 μs
- **Std dev**: 0.2 μs
- **Rounds**: 168607

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.9 μs
- **Std dev**: 0.0 μs
- **Rounds**: 196080

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c
