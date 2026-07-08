# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 4.48 s
- **Min time**: 4.23 s
- **Max time**: 4.86 s
- **Std dev**: 235.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 208.2
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

- **Mean time**: 178.9 μs
- **Min time**: 134.8 μs
- **Max time**: 542.1 μs
- **Std dev**: 55.5 μs
- **Rounds**: 1499

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 144.6 μs
- **Min time**: 123.3 μs
- **Max time**: 1.3 ms
- **Std dev**: 47.4 μs
- **Rounds**: 2953

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 421.3 μs
- **Min time**: 330.2 μs
- **Max time**: 1.5 ms
- **Std dev**: 111.6 μs
- **Rounds**: 1703

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 167.3 μs
- **Min time**: 122.0 μs
- **Max time**: 1.2 ms
- **Std dev**: 55.9 μs
- **Rounds**: 2645

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Svedala

- **Mean time**: 3.36 s
- **Min time**: 3.23 s
- **Max time**: 3.51 s
- **Std dev**: 106.9 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: svedala
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
