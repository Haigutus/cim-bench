# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 1.59 s
- **Min time**: 1.58 s
- **Max time**: 1.61 s
- **Std dev**: 13.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 285.3
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

- **Mean time**: 52.5 μs
- **Min time**: 49.8 μs
- **Max time**: 135.2 μs
- **Std dev**: 4.6 μs
- **Rounds**: 5221

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 50.7 μs
- **Min time**: 47.4 μs
- **Max time**: 215.3 μs
- **Std dev**: 7.8 μs
- **Rounds**: 8388

**Metrics**:
- Generator Count: 78
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 138.1 μs
- **Min time**: 130.5 μs
- **Max time**: 343.5 μs
- **Std dev**: 15.8 μs
- **Rounds**: 4503

**Metrics**:
- Load Count: 146
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 47.8 μs
- **Min time**: 44.4 μs
- **Max time**: 398.3 μs
- **Std dev**: 9.2 μs
- **Rounds**: 7615

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f
