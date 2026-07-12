# Benchmark Report

**Generated from**: `results-docker/cimgo_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Cimgo Validate Realgrid

- **Mean time**: 4.34 s
- **Min time**: 4.07 s
- **Max time**: 4.61 s
- **Std dev**: 221.0 ms
- **Rounds**: 5

**Metrics**:
- Tool Type: cli
- Tags: ['cli', 'validator', 'serializer', 'go']
- Library: cimgo
- Operation: validate
- Dataset: realgrid
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Display Name: cimgo
- Color: #2ecc71
- Binary: /usr/local/bin/cimcli-linux-amd64
- Memory Mb: 717.1

### Cimgo Convert Realgrid

- **Mean time**: 3.69 s
- **Min time**: 3.63 s
- **Max time**: 3.76 s
- **Std dev**: 45.9 ms
- **Rounds**: 5

**Metrics**:
- Tool Type: cli
- Tags: ['cli', 'validator', 'serializer', 'go']
- Library: cimgo
- Operation: convert
- Dataset: realgrid
- Dataset Size Mb: 86.5
- Cgmes Version: 2.4.15
- Display Name: cimgo
- Color: #2ecc71
- Binary: /usr/local/bin/cimcli-linux-amd64
- Memory Mb: 621.7
