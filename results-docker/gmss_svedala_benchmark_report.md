# Benchmark Report

**Generated from**: `results-docker/gmss_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Gmss Load Svedala

- **Mean time**: 975.5 ms
- **Min time**: 917.2 ms
- **Max time**: 1.01 s
- **Std dev**: 46.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 394.1
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

- **Mean time**: 3.06 s
- **Min time**: 2.90 s
- **Max time**: 3.17 s
- **Std dev**: 99.8 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Generators

- **Mean time**: 117.8 μs
- **Min time**: 96.3 μs
- **Max time**: 671.8 μs
- **Std dev**: 51.0 μs
- **Rounds**: 1879

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Loads

- **Mean time**: 283.2 μs
- **Min time**: 232.2 μs
- **Max time**: 1.2 ms
- **Std dev**: 85.2 μs
- **Rounds**: 2407

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Substations

- **Mean time**: 90.7 μs
- **Min time**: 77.5 μs
- **Max time**: 889.6 μs
- **Std dev**: 41.8 μs
- **Rounds**: 4259

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4
