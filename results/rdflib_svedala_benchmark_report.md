# Benchmark Report

**Generated from**: `results/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 952.9 ms
- **Min time**: 898.6 ms
- **Max time**: 1.02 s
- **Std dev**: 44.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 110.1
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

- **Mean time**: 58.6 μs
- **Min time**: 55.7 μs
- **Max time**: 328.5 μs
- **Std dev**: 8.2 μs
- **Rounds**: 4007

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 49.4 μs
- **Min time**: 46.7 μs
- **Max time**: 375.7 μs
- **Std dev**: 8.1 μs
- **Rounds**: 8729

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 140.3 μs
- **Min time**: 133.9 μs
- **Max time**: 737.3 μs
- **Std dev**: 21.0 μs
- **Rounds**: 3950

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 52.0 μs
- **Min time**: 49.5 μs
- **Max time**: 176.4 μs
- **Std dev**: 4.0 μs
- **Rounds**: 7781

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f
