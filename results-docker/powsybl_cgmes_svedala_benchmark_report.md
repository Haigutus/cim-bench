# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Powsybl Cgmes Load Svedala

- **Mean time**: 251.1 ms
- **Min time**: 221.7 ms
- **Max time**: 293.6 ms
- **Std dev**: 30.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 610.3
- Triples: 95499
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Total Size Mb: 7.3
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Lines

- **Mean time**: 110.3 μs
- **Min time**: 50.1 μs
- **Max time**: 1.2 ms
- **Std dev**: 99.5 μs
- **Rounds**: 1874

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 55.1 μs
- **Min time**: 38.9 μs
- **Max time**: 321.3 μs
- **Std dev**: 18.4 μs
- **Rounds**: 1856

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 187.9 μs
- **Min time**: 101.8 μs
- **Max time**: 77.2 ms
- **Std dev**: 1.8 ms
- **Rounds**: 1851

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 56.8 μs
- **Min time**: 34.0 μs
- **Max time**: 13.7 ms
- **Std dev**: 286.3 μs
- **Rounds**: 2296

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8
