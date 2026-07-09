# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 4.74 s
- **Min time**: 4.35 s
- **Max time**: 5.16 s
- **Std dev**: 312.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 208.0
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

- **Mean time**: 186.2 μs
- **Min time**: 131.6 μs
- **Max time**: 935.8 μs
- **Std dev**: 81.5 μs
- **Rounds**: 2607

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 172.7 μs
- **Min time**: 124.5 μs
- **Max time**: 758.0 μs
- **Std dev**: 68.2 μs
- **Rounds**: 3472

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 509.0 μs
- **Min time**: 353.0 μs
- **Max time**: 2.3 ms
- **Std dev**: 222.6 μs
- **Rounds**: 1793

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 170.5 μs
- **Min time**: 120.9 μs
- **Max time**: 970.0 μs
- **Std dev**: 69.0 μs
- **Rounds**: 2912

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Svedala

- **Mean time**: 4.66 s
- **Min time**: 4.50 s
- **Max time**: 4.77 s
- **Std dev**: 111.3 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: svedala
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
