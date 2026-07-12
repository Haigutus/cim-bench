# Benchmark Report

**Generated from**: `results-docker/gmss_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Gmss Load Svedala

- **Mean time**: 959.8 ms
- **Min time**: 912.9 ms
- **Max time**: 1.01 s
- **Std dev**: 43.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 298.1
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

- **Mean time**: 111.7 μs
- **Min time**: 89.8 μs
- **Max time**: 5.5 ms
- **Std dev**: 122.4 μs
- **Rounds**: 7173

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Generators

- **Mean time**: 106.6 μs
- **Min time**: 85.3 μs
- **Max time**: 2.4 ms
- **Std dev**: 98.6 μs
- **Rounds**: 6177

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Loads

- **Mean time**: 299.6 μs
- **Min time**: 236.4 μs
- **Max time**: 2.6 ms
- **Std dev**: 223.2 μs
- **Rounds**: 3136

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Substations

- **Mean time**: 100.5 μs
- **Min time**: 82.0 μs
- **Max time**: 2.1 ms
- **Std dev**: 105.9 μs
- **Rounds**: 7149

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4
