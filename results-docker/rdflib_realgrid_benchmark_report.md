# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 14.87 s
- **Min time**: 14.66 s
- **Max time**: 15.05 s
- **Std dev**: 141.9 ms
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

- **Mean time**: 1.3 ms
- **Min time**: 1.2 ms
- **Max time**: 2.1 ms
- **Std dev**: 122.0 μs
- **Rounds**: 388

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 239.2 μs
- **Min time**: 227.2 μs
- **Max time**: 485.9 μs
- **Std dev**: 15.2 μs
- **Rounds**: 1785

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 1.1 ms
- **Min time**: 1.1 ms
- **Max time**: 2.5 ms
- **Std dev**: 82.6 μs
- **Rounds**: 479

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 772.3 μs
- **Min time**: 726.8 μs
- **Max time**: 1.8 ms
- **Std dev**: 94.7 μs
- **Rounds**: 797

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
