# Benchmark Report

**Generated from**: `results-docker/veragrid_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Veragrid Load Svedala

- **Mean time**: 1.70 s
- **Min time**: 1.56 s
- **Max time**: 2.03 s
- **Std dev**: 188.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 74.8
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

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 2.6 μs
- **Std dev**: 0.0 μs
- **Rounds**: 55948

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
- **Max time**: 3.4 μs
- **Std dev**: 0.1 μs
- **Rounds**: 198414

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
- **Max time**: 43.4 μs
- **Std dev**: 0.2 μs
- **Rounds**: 131493

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.2 μs
- **Min time**: 0.2 μs
- **Max time**: 30.0 μs
- **Std dev**: 0.1 μs
- **Rounds**: 158428

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Export Svedala

- **Mean time**: 1.52 s
- **Min time**: 1.28 s
- **Max time**: 1.67 s
- **Std dev**: 144.0 ms
- **Rounds**: 5

**Metrics**:
- Library: veragrid
- Dataset: svedala
- Operation: export
- Display Name: VeraGrid
- Color: #2ca02c
