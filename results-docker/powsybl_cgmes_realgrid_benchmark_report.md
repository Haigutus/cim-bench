# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Powsybl Cgmes Load Realgrid

- **Mean time**: 1.77 s
- **Min time**: 1.72 s
- **Max time**: 1.80 s
- **Std dev**: 28.4 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2721.5
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

- **Mean time**: 347.4 ms
- **Min time**: 306.8 ms
- **Max time**: 419.1 ms
- **Std dev**: 46.2 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 288.3 μs
- **Min time**: 165.4 μs
- **Max time**: 1.1 ms
- **Std dev**: 110.0 μs
- **Rounds**: 599

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 983.1 μs
- **Min time**: 879.8 μs
- **Max time**: 2.1 ms
- **Std dev**: 111.3 μs
- **Rounds**: 231

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 330.9 μs
- **Min time**: 287.0 μs
- **Max time**: 1.6 ms
- **Std dev**: 80.5 μs
- **Rounds**: 682

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Realgrid

- **Mean time**: 2.17 s
- **Min time**: 2.09 s
- **Max time**: 2.34 s
- **Std dev**: 99.5 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: realgrid
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
