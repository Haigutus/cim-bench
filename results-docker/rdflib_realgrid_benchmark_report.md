# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 50.86 s
- **Min time**: 46.09 s
- **Max time**: 63.32 s
- **Std dev**: 7.19 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1109.4
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

- **Mean time**: 2.8 ms
- **Min time**: 2.3 ms
- **Max time**: 6.0 ms
- **Std dev**: 598.6 μs
- **Rounds**: 257

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 928.2 μs
- **Min time**: 785.3 μs
- **Max time**: 1.8 ms
- **Std dev**: 134.5 μs
- **Rounds**: 632

**Metrics**:
- Generator Count: 2694
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 5.5 ms
- **Min time**: 4.3 ms
- **Max time**: 8.6 ms
- **Std dev**: 925.6 μs
- **Rounds**: 135

**Metrics**:
- Load Count: 13374
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 1.7 ms
- **Min time**: 1.4 ms
- **Max time**: 3.5 ms
- **Std dev**: 251.3 μs
- **Rounds**: 475

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Realgrid

- **Mean time**: 41.10 s
- **Min time**: 39.47 s
- **Max time**: 42.56 s
- **Std dev**: 1.37 s
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: realgrid
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
