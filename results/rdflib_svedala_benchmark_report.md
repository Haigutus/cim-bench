# Benchmark Report

**Generated from**: `results/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 856.4 ms
- **Min time**: 841.1 ms
- **Max time**: 872.8 ms
- **Std dev**: 15.9 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 100.7
- Triples: 47710
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Total Size Mb: 7.3
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Lines

- **Mean time**: 53.4 μs
- **Min time**: 50.9 μs
- **Max time**: 184.4 μs
- **Std dev**: 4.9 μs
- **Rounds**: 3695

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 45.8 μs
- **Min time**: 40.8 μs
- **Max time**: 173.6 μs
- **Std dev**: 6.3 μs
- **Rounds**: 9122

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 129.8 μs
- **Min time**: 120.6 μs
- **Max time**: 387.3 μs
- **Std dev**: 16.6 μs
- **Rounds**: 4619

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 47.5 μs
- **Min time**: 42.4 μs
- **Max time**: 146.2 μs
- **Std dev**: 4.5 μs
- **Rounds**: 8624

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f
