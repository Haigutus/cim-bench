# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Powsybl Cgmes Load Svedala

- **Mean time**: 270.2 ms
- **Min time**: 239.6 ms
- **Max time**: 303.4 ms
- **Std dev**: 23.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 679.0
- Triples: 95499
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Total Size Mb: 7.3
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #9b59b6

### Powsybl Cgmes Get Lines

- **Mean time**: 149.7 μs
- **Min time**: 57.7 μs
- **Max time**: 843.8 μs
- **Std dev**: 112.3 μs
- **Rounds**: 1297

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #9b59b6

### Powsybl Cgmes Get Generators

- **Mean time**: 62.0 μs
- **Min time**: 40.8 μs
- **Max time**: 894.8 μs
- **Std dev**: 26.3 μs
- **Rounds**: 4621

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #9b59b6

### Powsybl Cgmes Get Loads

- **Mean time**: 159.4 μs
- **Min time**: 106.4 μs
- **Max time**: 1.0 ms
- **Std dev**: 68.5 μs
- **Rounds**: 706

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #9b59b6

### Powsybl Cgmes Get Substations

- **Mean time**: 67.0 μs
- **Min time**: 34.6 μs
- **Max time**: 51.7 ms
- **Std dev**: 776.9 μs
- **Rounds**: 5831

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #9b59b6
