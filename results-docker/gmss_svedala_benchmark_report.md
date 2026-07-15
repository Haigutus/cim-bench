# Benchmark Report

**Generated from**: `results-docker/gmss_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Gmss Load Svedala

- **Mean time**: 982.6 ms
- **Min time**: 929.2 ms
- **Max time**: 1.05 s
- **Std dev**: 49.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 299.3
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
- Tags: ['parser', 'query', 'typed-model', 'c#']

### Gmss Get Lines

- **Mean time**: 106.1 μs
- **Min time**: 88.2 μs
- **Max time**: 3.9 ms
- **Std dev**: 104.2 μs
- **Rounds**: 5817

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Generators

- **Mean time**: 102.4 μs
- **Min time**: 84.0 μs
- **Max time**: 1.8 ms
- **Std dev**: 92.7 μs
- **Rounds**: 7511

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Loads

- **Mean time**: 282.5 μs
- **Min time**: 230.2 μs
- **Max time**: 2.1 ms
- **Std dev**: 180.1 μs
- **Rounds**: 3337

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Substations

- **Mean time**: 96.1 μs
- **Min time**: 78.6 μs
- **Max time**: 2.1 ms
- **Std dev**: 100.2 μs
- **Rounds**: 8024

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4
