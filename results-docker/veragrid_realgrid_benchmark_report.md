# Benchmark Report

**Generated from**: `results-docker/veragrid_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Veragrid Load Realgrid

- **Mean time**: 10.80 s
- **Min time**: 10.57 s
- **Max time**: 11.11 s
- **Std dev**: 228.4 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 304.7
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Cgmes Version: 2.4.15
- Dataset Size Mb: 86.5
- Library: veragrid
- Library Version: 6.3.0
- Library Dependencies: {'numpy': '2.4.6', 'PySide6': '6.11.1', 'requests': '2.34.2', 'urllib3': '2.7.0', 'websockets': '16.0', 'opencv-python': '5.0.0.93', 'packaging': '26.2', 'VeraGridEngine': '6.3.0'}
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c
- Tags: ['parser', 'serializer', 'query', 'powerflow-tool', 'python']

### Veragrid Get Lines

- **Mean time**: 0.1 μs
- **Min time**: 0.0 μs
- **Max time**: 0.9 μs
- **Std dev**: 0.0 μs
- **Rounds**: 106975

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
- **Max time**: 17.8 μs
- **Std dev**: 0.0 μs
- **Rounds**: 198413

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
- **Max time**: 1.2 μs
- **Std dev**: 0.0 μs
- **Rounds**: 57857

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
- **Rounds**: 105955

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Export Realgrid

- **Mean time**: 16.73 s
- **Min time**: 16.49 s
- **Max time**: 17.02 s
- **Std dev**: 196.1 ms
- **Rounds**: 5

**Metrics**:
- Library: veragrid
- Dataset: realgrid
- Operation: export
- Display Name: VeraGrid
- Color: #2ca02c
