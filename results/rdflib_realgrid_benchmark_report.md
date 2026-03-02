# Benchmark Report

**Generated from**: `results/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 19.13 s
- **Min time**: 18.71 s
- **Max time**: 19.64 s
- **Std dev**: 397.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1095.7
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

- **Mean time**: 1.1 ms
- **Min time**: 1.1 ms
- **Max time**: 2.6 ms
- **Std dev**: 126.1 μs
- **Rounds**: 412

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 416.8 μs
- **Min time**: 404.1 μs
- **Max time**: 597.7 μs
- **Std dev**: 20.3 μs
- **Rounds**: 921

**Metrics**:
- Generator Count: 2694
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 2.0 ms
- **Min time**: 1.9 ms
- **Max time**: 3.1 ms
- **Std dev**: 174.1 μs
- **Rounds**: 294

**Metrics**:
- Load Count: 13374
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 748.8 μs
- **Min time**: 683.8 μs
- **Max time**: 1.8 ms
- **Std dev**: 143.2 μs
- **Rounds**: 891

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
