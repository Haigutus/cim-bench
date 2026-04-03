# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 1.64 s
- **Min time**: 1.63 s
- **Max time**: 1.65 s
- **Std dev**: 11.6 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 285.5
- Triples: 95499
- Lines: 97
- Generators: 78
- Loads: 146
- Substations: 57
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Library: rdflib
- Library Version: 7.6.0
- Library Dependencies: {}
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Lines

- **Mean time**: 57.3 μs
- **Min time**: 51.6 μs
- **Max time**: 141.8 μs
- **Std dev**: 10.2 μs
- **Rounds**: 4996

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 51.3 μs
- **Min time**: 47.7 μs
- **Max time**: 517.2 μs
- **Std dev**: 7.6 μs
- **Rounds**: 8257

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 140.9 μs
- **Min time**: 134.0 μs
- **Max time**: 361.1 μs
- **Std dev**: 14.5 μs
- **Rounds**: 4316

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 49.3 μs
- **Min time**: 44.8 μs
- **Max time**: 464.6 μs
- **Std dev**: 10.5 μs
- **Rounds**: 9325

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Svedala

- **Mean time**: 1.60 s
- **Min time**: 1.58 s
- **Max time**: 1.64 s
- **Std dev**: 26.0 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: svedala
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
