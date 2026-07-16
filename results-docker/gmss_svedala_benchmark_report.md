# Benchmark Report

**Generated from**: `results-docker/gmss_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Gmss Load Svedala

- **Mean time**: 1.01 s
- **Min time**: 959.2 ms
- **Max time**: 1.07 s
- **Std dev**: 42.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 312.9
- Triples: 95499
- Lines: 97
- Generators: 78
- Loads: 146
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: gmss
- Library Version: 10.1.1.0
- Library Dependencies: {'dotnet': '10.0.9', 'GridLab.Abp.Rdf': '10.1.1.0', 'Volo.Abp.Core': '10.1.1.0'}
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4
- Tags: ['parser', 'query', 'sparql', 'c#']

### Gmss Get Lines

- **Mean time**: 2.92 s
- **Min time**: 2.74 s
- **Max time**: 3.20 s
- **Std dev**: 178.1 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Generators

- **Mean time**: 120.6 μs
- **Min time**: 98.7 μs
- **Max time**: 1.1 ms
- **Std dev**: 59.4 μs
- **Rounds**: 1361

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Loads

- **Mean time**: 284.7 μs
- **Min time**: 237.1 μs
- **Max time**: 2.0 ms
- **Std dev**: 100.6 μs
- **Rounds**: 2372

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Substations

- **Mean time**: 92.1 μs
- **Min time**: 79.6 μs
- **Max time**: 3.0 ms
- **Std dev**: 54.7 μs
- **Rounds**: 5234

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4
