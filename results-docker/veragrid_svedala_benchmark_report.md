# Benchmark Report

**Generated from**: `results-docker/veragrid_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Veragrid Load Svedala

- **Mean time**: 701.7 ms
- **Min time**: 645.6 ms
- **Max time**: 918.3 ms
- **Std dev**: 121.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 71.8
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

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 107910

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
- **Max time**: 1.1 μs
- **Std dev**: 0.0 μs
- **Rounds**: 91651

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
- **Max time**: 12.0 μs
- **Std dev**: 0.1 μs
- **Rounds**: 134699

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
- **Max time**: 0.6 μs
- **Std dev**: 0.0 μs
- **Rounds**: 82899

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: veragrid
- Dataset: svedala
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Export Svedala

- **Mean time**: 1.54 s
- **Min time**: 1.33 s
- **Max time**: 1.64 s
- **Std dev**: 119.3 ms
- **Rounds**: 5

**Metrics**:
- Library: veragrid
- Dataset: svedala
- Operation: export
- Display Name: VeraGrid
- Color: #2ca02c
