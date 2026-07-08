# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 30.75 s
- **Min time**: 24.95 s
- **Max time**: 39.25 s
- **Std dev**: 5.62 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1088.5
- Triples: 1146183
- Lines: 7561
- Generators: 2694
- Loads: 13374
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: rdflib
- Library Version: 7.6.0
- Library Dependencies: {}
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'python']

### Rdflib Get Lines

- **Mean time**: 1.4 ms
- **Min time**: 1.3 ms
- **Max time**: 2.2 ms
- **Std dev**: 141.0 μs
- **Rounds**: 382

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 483.3 μs
- **Min time**: 443.4 μs
- **Max time**: 762.4 μs
- **Std dev**: 39.2 μs
- **Rounds**: 875

**Metrics**:
- Generator Count: 2694
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 2.1 ms
- **Min time**: 1.9 ms
- **Max time**: 3.2 ms
- **Std dev**: 197.8 μs
- **Rounds**: 283

**Metrics**:
- Load Count: 13374
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 710.8 μs
- **Min time**: 670.1 μs
- **Max time**: 1.4 ms
- **Std dev**: 53.4 μs
- **Rounds**: 844

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Realgrid

- **Mean time**: 29.66 s
- **Min time**: 24.04 s
- **Max time**: 33.56 s
- **Std dev**: 3.61 s
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: realgrid
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
