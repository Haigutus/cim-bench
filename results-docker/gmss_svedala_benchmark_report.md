# Benchmark Report

**Generated from**: `results-docker/gmss_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.14
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Gmss Load Svedala

- **Mean time**: 2.01 s
- **Min time**: 1.87 s
- **Max time**: 2.15 s
- **Std dev**: 126.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 369.6
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

- **Mean time**: 280.7 μs
- **Min time**: 210.5 μs
- **Max time**: 9.7 ms
- **Std dev**: 364.4 μs
- **Rounds**: 1302

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Generators

- **Mean time**: 277.0 μs
- **Min time**: 198.1 μs
- **Max time**: 4.9 ms
- **Std dev**: 274.2 μs
- **Rounds**: 2796

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Loads

- **Mean time**: 717.8 μs
- **Min time**: 506.6 μs
- **Max time**: 7.9 ms
- **Std dev**: 495.8 μs
- **Rounds**: 1366

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Substations

- **Mean time**: 340.4 μs
- **Min time**: 183.7 μs
- **Max time**: 6.9 ms
- **Std dev**: 345.9 μs
- **Rounds**: 2615

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4
