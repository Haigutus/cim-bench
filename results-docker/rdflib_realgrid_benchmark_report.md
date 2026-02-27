# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 17.61 s
- **Min time**: 17.47 s
- **Max time**: 17.82 s
- **Std dev**: 157.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 930.9
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

- **Mean time**: 1.4 ms
- **Min time**: 1.3 ms
- **Max time**: 2.5 ms
- **Std dev**: 83.5 μs
- **Rounds**: 328

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 276.4 μs
- **Min time**: 264.1 μs
- **Max time**: 417.4 μs
- **Std dev**: 15.9 μs
- **Rounds**: 1392

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 1.5 ms
- **Min time**: 1.2 ms
- **Max time**: 5.2 ms
- **Std dev**: 527.2 μs
- **Rounds**: 243

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 896.9 μs
- **Min time**: 838.5 μs
- **Max time**: 2.3 ms
- **Std dev**: 155.9 μs
- **Rounds**: 536

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
