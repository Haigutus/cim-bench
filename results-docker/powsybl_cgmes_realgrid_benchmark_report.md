# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Powsybl Cgmes Load Realgrid

- **Mean time**: 3.57 s
- **Min time**: 3.09 s
- **Max time**: 3.92 s
- **Std dev**: 343.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4855.0
- Triples: 1146183
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: powsybl_cgmes
- Library Version: 7.1.1
- Library Dependencies: {'jpype1': '1.7.1', 'java': '21.0.11'}
- Java Version: 21.0.11
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'java']

### Powsybl Cgmes Get Lines

- **Mean time**: 4.1 ms
- **Min time**: 1.8 ms
- **Max time**: 193.5 ms
- **Std dev**: 13.2 ms
- **Rounds**: 210

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 761.0 μs
- **Min time**: 380.6 μs
- **Max time**: 3.4 ms
- **Std dev**: 498.7 μs
- **Rounds**: 603

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 2.8 ms
- **Min time**: 2.0 ms
- **Max time**: 7.5 ms
- **Std dev**: 795.3 μs
- **Rounds**: 161

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 803.0 μs
- **Min time**: 638.7 μs
- **Max time**: 1.6 ms
- **Std dev**: 164.9 μs
- **Rounds**: 375

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Realgrid

- **Mean time**: 3.94 s
- **Min time**: 3.65 s
- **Max time**: 4.62 s
- **Std dev**: 385.7 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: realgrid
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
