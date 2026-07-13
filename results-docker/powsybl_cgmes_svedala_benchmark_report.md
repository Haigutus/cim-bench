# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Powsybl Cgmes Load Svedala

- **Mean time**: 252.8 ms
- **Min time**: 224.6 ms
- **Max time**: 326.0 ms
- **Std dev**: 41.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 467.6
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

- **Mean time**: 8.3 ms
- **Min time**: 4.4 ms
- **Max time**: 32.9 ms
- **Std dev**: 4.9 ms
- **Rounds**: 44

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 110.1 μs
- **Min time**: 51.9 μs
- **Max time**: 2.6 ms
- **Std dev**: 105.3 μs
- **Rounds**: 1587

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 161.8 μs
- **Min time**: 117.5 μs
- **Max time**: 1.1 ms
- **Std dev**: 61.3 μs
- **Rounds**: 1651

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 74.5 μs
- **Min time**: 31.4 μs
- **Max time**: 59.7 ms
- **Std dev**: 1.3 ms
- **Rounds**: 2388

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Svedala

- **Mean time**: 168.5 ms
- **Min time**: 132.9 ms
- **Max time**: 215.9 ms
- **Std dev**: 34.6 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: svedala
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
