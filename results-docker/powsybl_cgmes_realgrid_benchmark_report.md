# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Powsybl Cgmes Load Realgrid

- **Mean time**: 1.82 s
- **Min time**: 1.74 s
- **Max time**: 1.90 s
- **Std dev**: 60.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3064.3
- Triples: 1146183
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Lines

- **Mean time**: 918.1 μs
- **Min time**: 594.8 μs
- **Max time**: 2.1 ms
- **Std dev**: 178.1 μs
- **Rounds**: 305

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 193.2 μs
- **Min time**: 156.4 μs
- **Max time**: 2.9 ms
- **Std dev**: 110.5 μs
- **Rounds**: 1184

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 1.6 ms
- **Min time**: 1.1 ms
- **Max time**: 62.3 ms
- **Std dev**: 3.7 ms
- **Rounds**: 272

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 389.7 μs
- **Min time**: 295.5 μs
- **Max time**: 1.5 ms
- **Std dev**: 72.4 μs
- **Rounds**: 631

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8
