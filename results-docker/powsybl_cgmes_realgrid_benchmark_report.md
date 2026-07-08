# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Powsybl Cgmes Load Realgrid

- **Mean time**: 3.53 s
- **Min time**: 3.28 s
- **Max time**: 3.73 s
- **Std dev**: 196.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4907.5
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

- **Mean time**: 3.4 ms
- **Min time**: 1.8 ms
- **Max time**: 152.4 ms
- **Std dev**: 10.1 ms
- **Rounds**: 220

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 903.6 μs
- **Min time**: 549.0 μs
- **Max time**: 3.1 ms
- **Std dev**: 407.5 μs
- **Rounds**: 248

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 2.8 ms
- **Min time**: 2.2 ms
- **Max time**: 6.5 ms
- **Std dev**: 596.7 μs
- **Rounds**: 124

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 909.5 μs
- **Min time**: 739.0 μs
- **Max time**: 2.2 ms
- **Std dev**: 215.0 μs
- **Rounds**: 376

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Realgrid

- **Mean time**: 3.88 s
- **Min time**: 3.79 s
- **Max time**: 4.00 s
- **Std dev**: 77.0 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: realgrid
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
