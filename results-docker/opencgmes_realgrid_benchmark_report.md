# Benchmark Report

**Generated from**: `results-docker/opencgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Opencgmes Load Realgrid

- **Mean time**: 1.04 s
- **Min time**: 959.9 ms
- **Max time**: 1.20 s
- **Std dev**: 108.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3625.2
- Triples: 892131
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: opencgmes
- Library Version: 1.0.0-SNAPSHOT
- Library Dependencies: {'jpype1': '1.6.0', 'java': '21.0.10', 'jena': '5.5.0'}
- Java Version: 21.0.10
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Lines

- **Mean time**: 1.9 ms
- **Min time**: 855.1 μs
- **Max time**: 4.8 ms
- **Std dev**: 674.5 μs
- **Rounds**: 178

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 236.1 μs
- **Min time**: 152.2 μs
- **Max time**: 3.1 ms
- **Std dev**: 166.4 μs
- **Rounds**: 1595

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 947.6 μs
- **Min time**: 659.2 μs
- **Max time**: 3.4 ms
- **Std dev**: 385.9 μs
- **Rounds**: 446

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 382.5 μs
- **Min time**: 304.8 μs
- **Max time**: 40.5 ms
- **Std dev**: 1.1 ms
- **Rounds**: 1335

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Export Realgrid

- **Mean time**: 3.91 s
- **Min time**: 3.84 s
- **Max time**: 4.15 s
- **Std dev**: 133.0 ms
- **Rounds**: 5

**Metrics**:
- Library: opencgmes
- Dataset: realgrid
- Operation: export
- Display Name: OpenCGMES
- Color: #e91e63
