# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 19.13 s
- **Min time**: 18.97 s
- **Max time**: 19.31 s
- **Std dev**: 139.9 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1520.4
- Triples: 1146183
- Lines: 7561
- Generators: 2694
- Loads: 13374
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Lines

- **Mean time**: 1.2 ms
- **Min time**: 1.1 ms
- **Max time**: 1.6 ms
- **Std dev**: 46.1 μs
- **Rounds**: 389

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 419.7 μs
- **Min time**: 409.2 μs
- **Max time**: 683.6 μs
- **Std dev**: 19.5 μs
- **Rounds**: 1280

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
- **Max time**: 3.2 ms
- **Std dev**: 148.5 μs
- **Rounds**: 277

**Metrics**:
- Load Count: 13374
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 730.7 μs
- **Min time**: 708.9 μs
- **Max time**: 1.2 ms
- **Std dev**: 34.9 μs
- **Rounds**: 811

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
