# Benchmark Report

**Generated from**: `results-docker/pocket_rdf_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Pocket Rdf Serialize Realgrid

- **Mean time**: 28.47 s
- **Min time**: 28.34 s
- **Max time**: 28.76 s
- **Std dev**: 172.8 ms
- **Rounds**: 5

**Metrics**:
- Tool Type: cli
- Tags: ['cli', 'serializer', 'query', 'sparql', 'python']
- Library: pocket_rdf
- Operation: serialize
- Dataset: realgrid
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Display Name: pocket-rdf
- Color: #16a085
- Binary: /app/.venv/bin/pocket-rdf
- Memory Mb: 1250.0

### Pocket Rdf Query Realgrid

- **Mean time**: 26.06 s
- **Min time**: 26.02 s
- **Max time**: 26.12 s
- **Std dev**: 40.5 ms
- **Rounds**: 5

**Metrics**:
- Tool Type: cli
- Tags: ['cli', 'serializer', 'query', 'sparql', 'python']
- Library: pocket_rdf
- Operation: query
- Dataset: realgrid
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Display Name: pocket-rdf
- Color: #16a085
- Binary: /app/.venv/bin/pocket-rdf
- Memory Mb: 1241.1
