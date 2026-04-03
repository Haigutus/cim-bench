# Benchmark Report

**Generated from**: `results-docker/veragrid_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Veragrid Load Svedala

- **Mean time**: 470.4 ms
- **Min time**: 416.8 ms
- **Max time**: 525.7 ms
- **Std dev**: 40.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 82.1
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Cgmes Version: 3.0
- Dataset Size Mb: 7.3
- Library: veragrid
- Library Version: 5.6.38
- Library Dependencies: {'setuptools': '82.0.1', 'wheel': '0.46.3', 'PySide6': '6.11.0', 'websockets': '16.0', 'opencv-python': '4.13.0.92', 'packaging': '26.0', 'VeraGridEngine': '5.6.38'}
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Lines

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 105619

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Generators

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 0.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 88567

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
- **Max time**: 12.6 μs
- **Std dev**: 0.0 μs
- **Rounds**: 157679

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 0.5 μs
- **Std dev**: 0.0 μs
- **Rounds**: 88410

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Export Svedala

- **Mean time**: 1.08 s
- **Min time**: 918.0 ms
- **Max time**: 1.24 s
- **Std dev**: 122.7 ms
- **Rounds**: 5

**Metrics**:
- Library: veragrid
- Dataset: svedala
- Operation: export
- Display Name: VeraGrid
- Color: #2ca02c
