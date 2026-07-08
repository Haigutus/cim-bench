# Benchmark Report

**Generated from**: `results-docker/veragrid_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Veragrid Load Svedala

- **Mean time**: 1.76 s
- **Min time**: 1.59 s
- **Max time**: 1.92 s
- **Std dev**: 131.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 74.9
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Cgmes Version: 3.0
- Dataset Size Mb: 7.3
- Library: veragrid
- Library Version: 6.3.0
- Library Dependencies: {'numpy': '2.4.6', 'PySide6': '6.11.1', 'requests': '2.34.2', 'urllib3': '2.7.0', 'websockets': '16.0', 'opencv-python': '5.0.0.93', 'packaging': '26.2', 'VeraGridEngine': '6.3.0'}
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c
- Tags: ['parser', 'serializer', 'query', 'powerflow-tool', 'python']

### Veragrid Get Lines

- **Mean time**: 0.3 μs
- **Min time**: 0.2 μs
- **Max time**: 61.7 μs
- **Std dev**: 0.2 μs
- **Rounds**: 122474

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Generators

- **Mean time**: 0.3 μs
- **Min time**: 0.2 μs
- **Max time**: 63.4 μs
- **Std dev**: 0.3 μs
- **Rounds**: 170328

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Loads

- **Mean time**: 0.3 μs
- **Min time**: 0.3 μs
- **Max time**: 11.7 μs
- **Std dev**: 0.1 μs
- **Rounds**: 110169

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.3 μs
- **Min time**: 0.2 μs
- **Max time**: 22.4 μs
- **Std dev**: 0.2 μs
- **Rounds**: 88567

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Export Svedala

- **Mean time**: 2.90 s
- **Min time**: 2.48 s
- **Max time**: 3.18 s
- **Std dev**: 291.0 ms
- **Rounds**: 5

**Metrics**:
- Library: veragrid
- Dataset: svedala
- Operation: export
- Display Name: VeraGrid
- Color: #2ca02c
