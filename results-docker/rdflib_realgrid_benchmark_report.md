# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 18.79 s
- **Min time**: 18.63 s
- **Max time**: 18.88 s
- **Std dev**: 101.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1518.2
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
- **Max time**: 1.8 ms
- **Std dev**: 51.7 μs
- **Rounds**: 400

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 402.7 μs
- **Min time**: 392.3 μs
- **Max time**: 821.4 μs
- **Std dev**: 18.9 μs
- **Rounds**: 1298

**Metrics**:
- Generator Count: 2694
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 1.9 ms
- **Min time**: 1.9 ms
- **Max time**: 2.7 ms
- **Std dev**: 98.3 μs
- **Rounds**: 297

**Metrics**:
- Load Count: 13374
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 729.9 μs
- **Min time**: 676.6 μs
- **Max time**: 1.9 ms
- **Std dev**: 109.5 μs
- **Rounds**: 838

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
