# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 23.27 s
- **Min time**: 20.62 s
- **Max time**: 24.37 s
- **Std dev**: 1.54 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1078.4
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

- **Mean time**: 446.88 s
- **Min time**: 385.43 s
- **Max time**: 515.45 s
- **Std dev**: 54.18 s
- **Rounds**: 5

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 443.7 μs
- **Min time**: 427.9 μs
- **Max time**: 1.0 ms
- **Std dev**: 29.0 μs
- **Rounds**: 857

**Metrics**:
- Generator Count: 2694
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 2.1 ms
- **Min time**: 2.0 ms
- **Max time**: 3.1 ms
- **Std dev**: 104.9 μs
- **Rounds**: 245

**Metrics**:
- Load Count: 13374
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 750.0 μs
- **Min time**: 717.3 μs
- **Max time**: 1.7 ms
- **Std dev**: 85.2 μs
- **Rounds**: 776

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Realgrid

- **Mean time**: 18.61 s
- **Min time**: 18.59 s
- **Max time**: 18.63 s
- **Std dev**: 22.1 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: realgrid
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
