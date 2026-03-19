# Benchmark Report

**Generated from**: `results-docker/opencgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.8-200.fc43.x86_64

## Results

### Opencgmes Load Realgrid

- **Mean time**: 1.24 s
- **Min time**: 1.12 s
- **Max time**: 1.30 s
- **Std dev**: 73.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 5526.9
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

- **Mean time**: 2.5 ms
- **Min time**: 917.6 μs
- **Max time**: 34.0 ms
- **Std dev**: 2.6 ms
- **Rounds**: 176

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Generators

- **Mean time**: 248.9 μs
- **Min time**: 156.7 μs
- **Max time**: 1.8 ms
- **Std dev**: 134.7 μs
- **Rounds**: 1268

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Loads

- **Mean time**: 914.1 μs
- **Min time**: 640.9 μs
- **Max time**: 58.5 ms
- **Std dev**: 2.6 ms
- **Rounds**: 500

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63

### Opencgmes Get Substations

- **Mean time**: 467.6 μs
- **Min time**: 334.3 μs
- **Max time**: 18.5 ms
- **Std dev**: 526.6 μs
- **Rounds**: 1277

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: opencgmes
- Dataset: realgrid
- Display Name: OpenCGMES
- Color: #e91e63
