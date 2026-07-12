# Benchmark Report

**Generated from**: `results-docker/cimgo_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Results

### Cimgo Validate Svedala

- **Mean time**: 279.9 ms
- **Min time**: 275.8 ms
- **Max time**: 284.8 ms
- **Std dev**: 3.3 ms
- **Rounds**: 5

**Metrics**:
- Tool Type: cli
- Tags: ['cli', 'validator', 'serializer', 'go']
- Library: cimgo
- Operation: validate
- Dataset: svedala
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Display Name: cimgo
- Color: #2ecc71
- Binary: /usr/local/bin/cimcli-linux-amd64
- Memory Mb: 43.9

### Cimgo Convert Svedala

- **Mean time**: 379.6 ms
- **Min time**: 349.6 ms
- **Max time**: 398.8 ms
- **Std dev**: 21.7 ms
- **Rounds**: 5

**Metrics**:
- Tool Type: cli
- Tags: ['cli', 'validator', 'serializer', 'go']
- Library: cimgo
- Operation: convert
- Dataset: svedala
- Dataset Size Mb: 7.3
- Cgmes Version: 3.0
- Display Name: cimgo
- Color: #2ecc71
- Binary: /usr/local/bin/cimcli-linux-amd64
- Memory Mb: 76.8
