# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 1.66 s
- **Min time**: 1.64 s
- **Max time**: 1.69 s
- **Std dev**: 20.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 207.5
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

- **Mean time**: 61.2 μs
- **Min time**: 56.5 μs
- **Max time**: 191.3 μs
- **Std dev**: 7.2 μs
- **Rounds**: 5400

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 57.4 μs
- **Min time**: 53.8 μs
- **Max time**: 134.9 μs
- **Std dev**: 4.9 μs
- **Rounds**: 8322

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 156.3 μs
- **Min time**: 150.7 μs
- **Max time**: 274.1 μs
- **Std dev**: 9.1 μs
- **Rounds**: 3865

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 54.1 μs
- **Min time**: 50.6 μs
- **Max time**: 102.4 μs
- **Std dev**: 4.0 μs
- **Rounds**: 8877

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Svedala

- **Mean time**: 1.65 s
- **Min time**: 1.62 s
- **Max time**: 1.72 s
- **Std dev**: 41.5 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: svedala
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
