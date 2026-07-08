# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 4.42 s
- **Min time**: 4.19 s
- **Max time**: 4.71 s
- **Std dev**: 188.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 208.1
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
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'python']

### Rdflib Get Lines

- **Mean time**: 156.7 μs
- **Min time**: 122.2 μs
- **Max time**: 466.1 μs
- **Std dev**: 39.6 μs
- **Rounds**: 2259

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 147.4 μs
- **Min time**: 115.1 μs
- **Max time**: 635.5 μs
- **Std dev**: 34.5 μs
- **Rounds**: 4119

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 401.1 μs
- **Min time**: 326.1 μs
- **Max time**: 1.6 ms
- **Std dev**: 95.1 μs
- **Rounds**: 1752

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 211.5 μs
- **Min time**: 116.2 μs
- **Max time**: 1.0 ms
- **Std dev**: 81.4 μs
- **Rounds**: 3844

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Svedala

- **Mean time**: 4.18 s
- **Min time**: 4.03 s
- **Max time**: 4.31 s
- **Std dev**: 100.0 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: svedala
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
