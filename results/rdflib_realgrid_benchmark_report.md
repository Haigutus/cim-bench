# Benchmark Report

**Generated from**: `results/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 15.25 s
- **Min time**: 14.85 s
- **Max time**: 15.80 s
- **Std dev**: 493.2 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 806.2
- Triples: 892139
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Lines

- **Mean time**: 1.5 ms
- **Min time**: 1.2 ms
- **Max time**: 4.2 ms
- **Std dev**: 557.9 μs
- **Rounds**: 330

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 275.6 μs
- **Min time**: 241.6 μs
- **Max time**: 1.6 ms
- **Std dev**: 44.9 μs
- **Rounds**: 1761

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 1.2 ms
- **Min time**: 1.1 ms
- **Max time**: 2.2 ms
- **Std dev**: 145.1 μs
- **Rounds**: 403

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 867.1 μs
- **Min time**: 718.4 μs
- **Max time**: 2.8 ms
- **Std dev**: 189.8 μs
- **Rounds**: 784

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
