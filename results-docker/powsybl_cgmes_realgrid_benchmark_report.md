# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Powsybl Cgmes Load Realgrid

- **Mean time**: 1.81 s
- **Min time**: 1.73 s
- **Max time**: 1.89 s
- **Std dev**: 67.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3739.9
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

- **Mean time**: 1.1 ms
- **Min time**: 739.0 μs
- **Max time**: 3.5 ms
- **Std dev**: 399.7 μs
- **Rounds**: 274

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 254.4 μs
- **Min time**: 197.3 μs
- **Max time**: 676.9 μs
- **Std dev**: 67.6 μs
- **Rounds**: 1109

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 1.1 ms
- **Min time**: 775.3 μs
- **Max time**: 2.6 ms
- **Std dev**: 249.7 μs
- **Rounds**: 238

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 304.6 μs
- **Min time**: 272.7 μs
- **Max time**: 655.6 μs
- **Std dev**: 53.0 μs
- **Rounds**: 661

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: realgrid
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Realgrid

- **Mean time**: 2.13 s
- **Min time**: 2.04 s
- **Max time**: 2.24 s
- **Std dev**: 92.0 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: realgrid
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
