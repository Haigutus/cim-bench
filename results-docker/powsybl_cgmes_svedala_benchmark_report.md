# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Powsybl Cgmes Load Svedala

- **Mean time**: 245.4 ms
- **Min time**: 224.4 ms
- **Max time**: 285.9 ms
- **Std dev**: 25.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 449.3
- Triples: 95499
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: powsybl_cgmes
- Library Version: 7.1.1
- Library Dependencies: {'jpype1': '1.6.0', 'java': '21.0.10'}
- Java Version: 21.0.10
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Lines

- **Mean time**: 142.0 μs
- **Min time**: 56.2 μs
- **Max time**: 1.6 ms
- **Std dev**: 130.4 μs
- **Rounds**: 1491

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 53.2 μs
- **Min time**: 39.7 μs
- **Max time**: 447.1 μs
- **Std dev**: 17.2 μs
- **Rounds**: 4434

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 149.0 μs
- **Min time**: 119.4 μs
- **Max time**: 350.5 μs
- **Std dev**: 27.1 μs
- **Rounds**: 854

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 50.6 μs
- **Min time**: 39.9 μs
- **Max time**: 336.7 μs
- **Std dev**: 16.1 μs
- **Rounds**: 2878

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Svedala

- **Mean time**: 188.4 ms
- **Min time**: 165.7 ms
- **Max time**: 251.7 ms
- **Std dev**: 35.9 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: svedala
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
