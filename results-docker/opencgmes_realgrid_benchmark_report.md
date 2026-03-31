# Benchmark Report

**Generated from**: `results-docker/opencgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Opencgmes Load Realgrid

- **Mean time**: 1.07 s
- **Min time**: 908.9 ms
- **Max time**: 1.23 s
- **Std dev**: 120.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 5330.6
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

- **Mean time**: 1.6 ms
- **Min time**: 1.1 ms
- **Max time**: 4.7 ms
- **Std dev**: 454.2 μs
- **Rounds**: 147

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 279.6 μs
- **Min time**: 162.2 μs
- **Max time**: 3.2 ms
- **Std dev**: 187.6 μs
- **Rounds**: 1065

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 875.1 μs
- **Min time**: 656.7 μs
- **Max time**: 3.6 ms
- **Std dev**: 292.1 μs
- **Rounds**: 470

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 357.3 μs
- **Min time**: 327.3 μs
- **Max time**: 1.1 ms
- **Std dev**: 52.2 μs
- **Rounds**: 1338

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63
