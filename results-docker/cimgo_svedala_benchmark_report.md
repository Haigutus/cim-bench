# Benchmark Report

**Generated from**: `results-docker/cimgo_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Results

### Cimgo Validate Svedala

- **Mean time**: 541.3 ms
- **Min time**: 519.8 ms
- **Max time**: 560.1 ms
- **Std dev**: 15.8 ms
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
- Memory Mb: 42.9

### Cimgo Convert Svedala

- **Mean time**: 735.1 ms
- **Min time**: 677.1 ms
- **Max time**: 762.0 ms
- **Std dev**: 35.7 ms
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
- Memory Mb: 76.0
