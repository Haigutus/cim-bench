# Benchmark Report

**Generated from**: `results-docker/veragrid_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Veragrid Load Realgrid

- **Mean time**: 22.71 s
- **Min time**: 18.13 s
- **Max time**: 29.02 s
- **Std dev**: 5.46 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 308.9
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

- **Mean time**: 0.2 μs
- **Min time**: 0.2 μs
- **Max time**: 8.1 μs
- **Std dev**: 0.1 μs
- **Rounds**: 157432

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Generators

- **Mean time**: 0.2 μs
- **Min time**: 0.2 μs
- **Max time**: 57.1 μs
- **Std dev**: 0.2 μs
- **Rounds**: 155473

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Loads

- **Mean time**: 0.3 μs
- **Min time**: 0.2 μs
- **Max time**: 178.4 μs
- **Std dev**: 0.6 μs
- **Rounds**: 126503

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.2 μs
- **Min time**: 0.2 μs
- **Max time**: 36.5 μs
- **Std dev**: 0.2 μs
- **Rounds**: 143823

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Export Realgrid

- **Mean time**: 19.94 s
- **Min time**: 18.61 s
- **Max time**: 22.04 s
- **Std dev**: 1.42 s
- **Rounds**: 5

**Metrics**:
- Library: veragrid
- Dataset: realgrid
- Operation: export
- Display Name: VeraGrid
- Color: #2ca02c
