# Benchmark Report

**Generated from**: `results-docker/gmss_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Gmss Load Svedala

- **Mean time**: 1.59 s
- **Min time**: 1.34 s
- **Max time**: 1.83 s
- **Std dev**: 193.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 290.1
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

### Gmss Get Lines

- **Mean time**: 152.7 μs
- **Min time**: 117.7 μs
- **Max time**: 5.3 ms
- **Std dev**: 152.9 μs
- **Rounds**: 5363

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Generators

- **Mean time**: 122.6 μs
- **Min time**: 102.5 μs
- **Max time**: 1.5 ms
- **Std dev**: 101.3 μs
- **Rounds**: 4545

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Loads

- **Mean time**: 340.7 μs
- **Min time**: 274.9 μs
- **Max time**: 2.8 ms
- **Std dev**: 202.6 μs
- **Rounds**: 2844

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4

### Gmss Get Substations

- **Mean time**: 111.2 μs
- **Min time**: 93.8 μs
- **Max time**: 1.9 ms
- **Std dev**: 101.4 μs
- **Rounds**: 6792

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: gmss
- Dataset: svedala
- Display Name: GMSS CIM
- Color: #512bd4
