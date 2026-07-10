# Benchmark Report

**Generated from**: `results-docker/powsybl_cgmes_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Powsybl Cgmes Load Svedala

- **Mean time**: 240.6 ms
- **Min time**: 222.3 ms
- **Max time**: 274.8 ms
- **Std dev**: 20.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 445.2
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

- **Mean time**: 149.1 μs
- **Min time**: 59.0 μs
- **Max time**: 1.5 ms
- **Std dev**: 136.0 μs
- **Rounds**: 1393

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Generators

- **Mean time**: 60.2 μs
- **Min time**: 42.1 μs
- **Max time**: 571.8 μs
- **Std dev**: 26.1 μs
- **Rounds**: 3968

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Loads

- **Mean time**: 173.7 μs
- **Min time**: 141.4 μs
- **Max time**: 1.3 ms
- **Std dev**: 46.2 μs
- **Rounds**: 1125

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Get Substations

- **Mean time**: 45.7 μs
- **Min time**: 28.3 μs
- **Max time**: 148.5 μs
- **Std dev**: 10.6 μs
- **Rounds**: 2847

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: powsybl_cgmes
- Dataset: svedala
- Display Name: PowSyBL CGMES
- Color: #17a2b8

### Powsybl Cgmes Export Svedala

- **Mean time**: 150.5 ms
- **Min time**: 130.3 ms
- **Max time**: 175.3 ms
- **Std dev**: 17.6 ms
- **Rounds**: 5

**Metrics**:
- Library: powsybl_cgmes
- Dataset: svedala
- Operation: export
- Display Name: PowSyBL CGMES
- Color: #17a2b8
