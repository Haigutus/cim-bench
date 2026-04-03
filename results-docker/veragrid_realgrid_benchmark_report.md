# Benchmark Report

**Generated from**: `results-docker/veragrid_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Veragrid Load Realgrid

- **Mean time**: 6.90 s
- **Min time**: 5.74 s
- **Max time**: 7.29 s
- **Std dev**: 656.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 634.0
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Cgmes Version: 2.4.15
- Dataset Size Mb: 86.5
- Library: veragrid
- Library Version: 5.6.38
- Library Dependencies: {'setuptools': '82.0.1', 'wheel': '0.46.3', 'PySide6': '6.11.0', 'websockets': '16.0', 'opencv-python': '4.13.0.92', 'packaging': '26.0', 'VeraGridEngine': '5.6.38'}
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Lines

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.6 μs
- **Std dev**: 0.0 μs
- **Rounds**: 96628

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Generators

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 1.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 86274

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
- **Max time**: 8.2 μs
- **Std dev**: 0.0 μs
- **Rounds**: 167196

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 5.2 μs
- **Std dev**: 0.0 μs
- **Rounds**: 176026

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Export Realgrid

- **Mean time**: 12.55 s
- **Min time**: 8.96 s
- **Max time**: 17.41 s
- **Std dev**: 3.41 s
- **Rounds**: 5

**Metrics**:
- Library: veragrid
- Dataset: realgrid
- Operation: export
- Display Name: VeraGrid
- Color: #2ca02c
