# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Powsybl Cgmes Load Realgrid

- **Mean time**: 1.75 s
- **Min time**: 1.65 s
- **Max time**: 1.83 s
- **Std dev**: 71.4 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3159.7
- Triples: 1146183
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: powsybl_cgmes
- Library Version: 7.1.1
- Library Dependencies: {'jpype1': '1.6.0', 'java': '21.0.10'}
- Java Version: 21.0.10
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Lines

- **Mean time**: 1.2 ms
- **Min time**: 788.5 μs
- **Max time**: 2.7 ms
- **Std dev**: 292.5 μs
- **Rounds**: 273

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 248.5 μs
- **Min time**: 199.1 μs
- **Max time**: 1.5 ms
- **Std dev**: 86.7 μs
- **Rounds**: 1145

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 1.0 ms
- **Min time**: 868.6 μs
- **Max time**: 3.1 ms
- **Std dev**: 231.8 μs
- **Rounds**: 233

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 335.3 μs
- **Min time**: 291.4 μs
- **Max time**: 627.0 μs
- **Std dev**: 46.2 μs
- **Rounds**: 638

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Realgrid

- **Mean time**: 2.11 s
- **Min time**: 2.04 s
- **Max time**: 2.27 s
- **Std dev**: 103.7 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: realgrid
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
