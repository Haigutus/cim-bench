# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Powsybl Cgmes Load Svedala

- **Mean time**: 563.9 ms
- **Min time**: 495.5 ms
- **Max time**: 720.6 ms
- **Std dev**: 92.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 325.7
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

- **Mean time**: 520.4 μs
- **Min time**: 140.1 μs
- **Max time**: 2.7 ms
- **Std dev**: 387.8 μs
- **Rounds**: 921

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 241.9 μs
- **Min time**: 106.1 μs
- **Max time**: 33.0 ms
- **Std dev**: 665.1 μs
- **Rounds**: 2490

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 562.0 μs
- **Min time**: 380.4 μs
- **Max time**: 1.6 ms
- **Std dev**: 161.3 μs
- **Rounds**: 554

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 223.6 μs
- **Min time**: 104.0 μs
- **Max time**: 770.1 μs
- **Std dev**: 58.9 μs
- **Rounds**: 1715

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Svedala

- **Mean time**: 355.0 ms
- **Min time**: 281.9 ms
- **Max time**: 539.5 ms
- **Std dev**: 105.6 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: svedala
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
