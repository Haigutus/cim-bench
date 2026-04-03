# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 19.42 s
- **Min time**: 18.88 s
- **Max time**: 20.08 s
- **Std dev**: 447.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1522.6
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

### Rdflib Get Lines

- **Mean time**: 1.2 ms
- **Min time**: 1.2 ms
- **Max time**: 1.9 ms
- **Std dev**: 80.0 μs
- **Rounds**: 381

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 442.2 μs
- **Min time**: 422.6 μs
- **Max time**: 525.6 μs
- **Std dev**: 11.1 μs
- **Rounds**: 1178

**Metrics**:
- Generator Count: 2694
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 2.3 ms
- **Min time**: 2.1 ms
- **Max time**: 3.6 ms
- **Std dev**: 232.9 μs
- **Rounds**: 279

**Metrics**:
- Load Count: 13374
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 770.4 μs
- **Min time**: 734.0 μs
- **Max time**: 1.5 ms
- **Std dev**: 39.8 μs
- **Rounds**: 775

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Realgrid

- **Mean time**: 18.69 s
- **Min time**: 18.55 s
- **Max time**: 19.08 s
- **Std dev**: 220.0 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: realgrid
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
