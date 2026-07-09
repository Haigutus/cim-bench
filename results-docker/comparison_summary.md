# Benchmark Comparison Report

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.0.12-101.fc43.x86_64

## Performance Comparison

### Load Performance

| Library | Load Time (mean) | Memory (MB) | Elements | Notes |
|---------|------------------|-------------|----------|-------|
| cimgraph (Realgrid) | 25.15 s | 2642.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimgraph (Svedala) | 1.54 s | 179.1 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| jena (Realgrid) | 2.05 s | 3942.1 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| jena (Svedala) | 259.7 ms | 495.6 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| libcimpp (Realgrid) | 22.74 s | 132.9 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Realgrid) | 4.53 s | 356.3 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Svedala) | 526.9 ms | 128.4 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| opencgmes (Realgrid) | 2.18 s | 4391.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| opencgmes (Svedala) | 268.6 ms | 255.8 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| powsybl_cgmes (Realgrid) | 3.53 s | 4907.5 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| powsybl_cgmes (Svedala) | 563.9 ms | 325.7 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 9.86 s | 6201.0 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 1.34 s | 978.6 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 30.75 s | 1088.5 MB | 7561 lines, 2694 gen, 13374 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 4.74 s | 208.0 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 178.3 ms | 382.3 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 21.9 ms | 90.4 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 18.79 s | 319.9 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 1.70 s | 74.8 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | jena (Realgrid) | jena (Svedala) | libcimpp (Realgrid) | maplib (Realgrid) | maplib (Svedala) | opencgmes (Realgrid) | opencgmes (Svedala) | powsybl_cgmes (Realgrid) | powsybl_cgmes (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.2 μs | 0.4 μs | 1.7 ms | 452.2 μs | 8.4 ms | 1.3 ms | 1.0 ms | 2.8 ms | 644.0 μs | 903.6 μs | 241.9 μs | 6.8 ms | 1.4 ms | 483.3 μs | 172.7 μs | 23.8 ms | 5.9 ms | 0.3 μs | 0.1 μs |
| get_lines | 0.2 μs | 0.3 μs | 7.9 ms | 1.1 ms | 8.1 ms | 1.8 ms | 919.2 μs | 13.2 ms | 1.4 ms | 3.4 ms | 520.4 μs | 51.9 ms | 1.5 ms | 1.4 ms | 186.2 μs | 36.2 ms | 6.7 ms | 0.2 μs | 0.1 μs |
| get_loads | 0.5 μs | 0.6 μs | 12.2 ms | 792.3 μs | 19.5 ms | 3.2 ms | 2.4 ms | 7.5 ms | 909.9 μs | 2.8 ms | 562.0 μs | 31.6 ms | 1.0 ms | 2.1 ms | 509.0 μs | 30.9 ms | 6.7 ms | 0.3 μs | 0.3 μs |
| get_substations | 0.3 μs | 0.2 μs | 2.9 ms | 230.9 μs | 8.3 ms | 1.5 ms | 975.5 μs | 4.6 ms | 247.7 μs | 909.5 μs | 223.6 μs | 10.4 ms | 625.6 μs | 710.8 μs | 170.5 μs | 19.0 ms | 5.1 ms | 0.3 μs | 0.2 μs |

Per-tool details: see the `*_benchmark_report.md` files in this directory.
