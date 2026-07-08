# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Powsybl Cgmes Load Svedala

- **Mean time**: 673.3 ms
- **Min time**: 606.1 ms
- **Max time**: 699.6 ms
- **Std dev**: 39.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 612.4
- Triples: 95499
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: powsybl_cgmes
- Library Version: 7.1.1
- Library Dependencies: {'jpype1': '1.7.1', 'java': '21.0.11'}
- Java Version: 21.0.11
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'java']

### Powsybl Cgmes Get Lines

- **Mean time**: 562.6 μs
- **Min time**: 127.1 μs
- **Max time**: 2.6 ms
- **Std dev**: 364.8 μs
- **Rounds**: 861

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 245.8 μs
- **Min time**: 141.2 μs
- **Max time**: 1.7 ms
- **Std dev**: 137.5 μs
- **Rounds**: 799

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 718.3 μs
- **Min time**: 293.5 μs
- **Max time**: 1.8 ms
- **Std dev**: 229.5 μs
- **Rounds**: 603

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 154.6 μs
- **Min time**: 93.9 μs
- **Max time**: 1.5 ms
- **Std dev**: 77.0 μs
- **Rounds**: 2022

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Svedala

- **Mean time**: 398.3 ms
- **Min time**: 320.7 ms
- **Max time**: 597.5 ms
- **Std dev**: 116.9 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: svedala
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
