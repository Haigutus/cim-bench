# Benchmark Report

**Generated from**: `results/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 1.62 s
- **Min time**: 1.60 s
- **Max time**: 1.66 s
- **Std dev**: 22.5 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 228.4
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

- **Mean time**: 53.2 μs
- **Min time**: 49.3 μs
- **Max time**: 242.3 μs
- **Std dev**: 6.5 μs
- **Rounds**: 6066

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 50.0 μs
- **Min time**: 47.8 μs
- **Max time**: 104.5 μs
- **Std dev**: 3.6 μs
- **Rounds**: 8431

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 135.5 μs
- **Min time**: 124.6 μs
- **Max time**: 403.0 μs
- **Std dev**: 11.7 μs
- **Rounds**: 4440

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 47.7 μs
- **Min time**: 44.8 μs
- **Max time**: 132.9 μs
- **Std dev**: 4.5 μs
- **Rounds**: 9351

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f
