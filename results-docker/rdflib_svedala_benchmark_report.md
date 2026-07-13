# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 2.00 s
- **Min time**: 1.96 s
- **Max time**: 2.05 s
- **Std dev**: 31.0 ms
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

- **Mean time**: 805.7 ms
- **Min time**: 767.5 ms
- **Max time**: 837.2 ms
- **Std dev**: 27.5 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 68.8 μs
- **Min time**: 61.6 μs
- **Max time**: 170.8 μs
- **Std dev**: 9.0 μs
- **Rounds**: 3386

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 199.8 μs
- **Min time**: 171.9 μs
- **Max time**: 1.3 ms
- **Std dev**: 60.1 μs
- **Rounds**: 3036

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 66.3 μs
- **Min time**: 59.0 μs
- **Max time**: 725.2 μs
- **Std dev**: 15.9 μs
- **Rounds**: 6612

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Svedala

- **Mean time**: 1.95 s
- **Min time**: 1.90 s
- **Max time**: 2.01 s
- **Std dev**: 39.9 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: svedala
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
