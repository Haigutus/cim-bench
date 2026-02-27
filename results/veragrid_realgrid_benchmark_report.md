# Benchmark Report

**Generated from**: `results/veragrid_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Veragrid Load Realgrid

- **Mean time**: 17.06 s
- **Min time**: 16.02 s
- **Max time**: 17.77 s
- **Std dev**: 924.3 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 2689.8
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
- **Rounds**: 101021

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
- **Max time**: 0.3 μs
- **Std dev**: 0.0 μs
- **Rounds**: 101647

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
- **Max time**: 0.4 μs
- **Std dev**: 0.0 μs
- **Rounds**: 59447

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
- **Max time**: 3.6 μs
- **Std dev**: 0.0 μs
- **Rounds**: 103757

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c
