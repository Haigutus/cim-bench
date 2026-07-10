# Benchmark Report

**Generated from**: `results-docker/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 19.74 s
- **Min time**: 19.35 s
- **Max time**: 20.19 s
- **Std dev**: 392.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1092.7
- Triples: 1146183
- Lines: 7561
- Generators: 2694
- Loads: 13374
- Substations: 4875
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Library: rdflib
- Library Version: 7.6.0
- Library Dependencies: {}
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
- Tags: ['parser', 'serializer', 'query', 'sparql', 'triplestore', 'python']

### Rdflib Get Lines

- **Mean time**: 1.2 ms
- **Min time**: 1.1 ms
- **Max time**: 2.6 ms
- **Std dev**: 172.5 μs
- **Rounds**: 409

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 416.1 μs
- **Min time**: 402.9 μs
- **Max time**: 616.6 μs
- **Std dev**: 24.4 μs
- **Rounds**: 1062

**Metrics**:
- Generator Count: 2694
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 2.1 ms
- **Min time**: 1.9 ms
- **Max time**: 3.8 ms
- **Std dev**: 449.1 μs
- **Rounds**: 202

**Metrics**:
- Load Count: 13374
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 707.5 μs
- **Min time**: 697.2 μs
- **Max time**: 1.3 ms
- **Std dev**: 30.2 μs
- **Rounds**: 572

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Export Realgrid

- **Mean time**: 19.06 s
- **Min time**: 18.96 s
- **Max time**: 19.21 s
- **Std dev**: 101.0 ms
- **Rounds**: 5

**Metrics**:
- Library: rdflib
- Dataset: realgrid
- Operation: export
- Display Name: RDFlib
- Color: #f1c40f
