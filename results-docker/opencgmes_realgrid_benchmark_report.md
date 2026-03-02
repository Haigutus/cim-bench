# Benchmark Report

**Generated from**: `results-docker/opencgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Opencgmes Load Realgrid

- **Mean time**: 1.06 s
- **Min time**: 983.2 ms
- **Max time**: 1.18 s
- **Std dev**: 75.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4921.2
- Triples: 892131
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Lines

- **Mean time**: 1.9 ms
- **Min time**: 1.3 ms
- **Max time**: 37.8 ms
- **Std dev**: 3.3 ms
- **Rounds**: 127

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 324.9 μs
- **Min time**: 165.6 μs
- **Max time**: 1.8 ms
- **Std dev**: 144.1 μs
- **Rounds**: 813

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 1.2 ms
- **Min time**: 654.9 μs
- **Max time**: 82.1 ms
- **Std dev**: 3.7 ms
- **Rounds**: 478

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 378.9 μs
- **Min time**: 313.9 μs
- **Max time**: 9.9 ms
- **Std dev**: 293.8 μs
- **Rounds**: 1112

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63
