# Benchmark Report

**Generated from**: `results-docker/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 961.2 ms
- **Min time**: 941.7 ms
- **Max time**: 991.7 ms
- **Std dev**: 22.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 135.2
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

- **Mean time**: 62.4 μs
- **Min time**: 58.3 μs
- **Max time**: 168.0 μs
- **Std dev**: 9.1 μs
- **Rounds**: 4068

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 53.0 μs
- **Min time**: 49.0 μs
- **Max time**: 1.0 ms
- **Std dev**: 14.3 μs
- **Rounds**: 8084

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 148.8 μs
- **Min time**: 140.7 μs
- **Max time**: 369.9 μs
- **Std dev**: 14.7 μs
- **Rounds**: 3921

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 54.9 μs
- **Min time**: 52.1 μs
- **Max time**: 169.5 μs
- **Std dev**: 4.5 μs
- **Rounds**: 7516

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f
