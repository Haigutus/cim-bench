# Benchmark Report

**Generated from**: `results/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 17.23 s
- **Min time**: 16.80 s
- **Max time**: 17.82 s
- **Std dev**: 430.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 854.3
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

- **Mean time**: 1.7 ms
- **Min time**: 1.3 ms
- **Max time**: 8.4 ms
- **Std dev**: 1.1 ms
- **Rounds**: 210

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 285.6 μs
- **Min time**: 264.1 μs
- **Max time**: 555.2 μs
- **Std dev**: 14.5 μs
- **Rounds**: 1349

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 1.4 ms
- **Min time**: 1.2 ms
- **Max time**: 2.2 ms
- **Std dev**: 168.2 μs
- **Rounds**: 339

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 928.3 μs
- **Min time**: 836.2 μs
- **Max time**: 3.5 ms
- **Std dev**: 193.8 μs
- **Rounds**: 631

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
