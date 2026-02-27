# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 813.4 ms
- **Min time**: 810.9 ms
- **Max time**: 817.5 ms
- **Std dev**: 2.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 134.9
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

- **Mean time**: 51.3 μs
- **Min time**: 49.4 μs
- **Max time**: 80.6 μs
- **Std dev**: 2.4 μs
- **Rounds**: 5832

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 43.8 μs
- **Min time**: 41.8 μs
- **Max time**: 118.8 μs
- **Std dev**: 3.5 μs
- **Rounds**: 10006

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 124.4 μs
- **Min time**: 119.1 μs
- **Max time**: 526.8 μs
- **Std dev**: 8.4 μs
- **Rounds**: 4870

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 46.3 μs
- **Min time**: 43.7 μs
- **Max time**: 549.9 μs
- **Std dev**: 8.3 μs
- **Rounds**: 8821

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f
