# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 1.56 s
- **Min time**: 1.54 s
- **Max time**: 1.58 s
- **Std dev**: 16.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 285.7
- Triples: 95499
- Lines: 97
- Generators: 78
- Loads: 146
- Substations: 57
- Total Size Mb: 7.3
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Lines

- **Mean time**: 51.9 μs
- **Min time**: 49.4 μs
- **Max time**: 135.4 μs
- **Std dev**: 4.4 μs
- **Rounds**: 5009

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 49.4 μs
- **Min time**: 47.2 μs
- **Max time**: 136.9 μs
- **Std dev**: 4.2 μs
- **Rounds**: 7547

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 134.6 μs
- **Min time**: 129.8 μs
- **Max time**: 313.6 μs
- **Std dev**: 9.3 μs
- **Rounds**: 4333

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 46.6 μs
- **Min time**: 44.4 μs
- **Max time**: 133.7 μs
- **Std dev**: 3.8 μs
- **Rounds**: 9314

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f
