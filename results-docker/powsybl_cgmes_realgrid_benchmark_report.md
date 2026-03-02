# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Powsybl Cgmes Load Realgrid

- **Mean time**: 1.85 s
- **Min time**: 1.81 s
- **Max time**: 1.93 s
- **Std dev**: 46.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4223.6
- Triples: 1146183
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #9b59b6

### Powsybl Cgmes Get Lines

- **Mean time**: 1.2 ms
- **Min time**: 651.6 μs
- **Max time**: 3.4 ms
- **Std dev**: 425.4 μs
- **Rounds**: 281

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #9b59b6

### Powsybl Cgmes Get Generators

- **Mean time**: 220.5 μs
- **Min time**: 158.9 μs
- **Max time**: 1.3 ms
- **Std dev**: 103.7 μs
- **Rounds**: 1190

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #9b59b6

### Powsybl Cgmes Get Loads

- **Mean time**: 1.1 ms
- **Min time**: 872.5 μs
- **Max time**: 5.3 ms
- **Std dev**: 442.8 μs
- **Rounds**: 266

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #9b59b6

### Powsybl Cgmes Get Substations

- **Mean time**: 339.0 μs
- **Min time**: 299.0 μs
- **Max time**: 631.9 μs
- **Std dev**: 50.4 μs
- **Rounds**: 651

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #9b59b6
