# Benchmark Comparison Report

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.6
- **System**: Linux 7.1.3-100.fc43.x86_64

## Performance Comparison

### Load Performance

| Library | Load Time (mean) | Memory (MB) | Elements | Notes |
|---------|------------------|-------------|----------|-------|
| cimoxide (Realgrid) | 1.26 s | 537.4 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimoxide (Svedala) | 103.8 ms | 60.6 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| gmss (Svedala) | 959.8 ms | 298.1 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| graphdb (Realgrid) | 5.86 s | 1050.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| graphdb (Svedala) | 818.4 ms | 1764.0 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| jena (Realgrid) | 1.60 s | 2208.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| jena (Svedala) | 131.7 ms | 387.1 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| libcimpp (Realgrid) | 19.53 s | 133.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Realgrid) | 2.03 s | 441.4 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Svedala) | 223.5 ms | 139.6 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| opencgmes (Realgrid) | 1.09 s | 3133.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| opencgmes (Svedala) | 100.3 ms | 247.4 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| powsybl_cgmes (Realgrid) | 1.81 s | 3739.9 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| powsybl_cgmes (Svedala) | 240.6 ms | 445.2 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.24 s | 2089.0 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 428.4 ms | 1566.6 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 19.74 s | 1092.7 MB | 7561 lines, 2694 gen, 13374 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 1.66 s | 207.5 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 159.1 ms | 370.5 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 10.1 ms | 82.9 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 10.80 s | 304.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 701.7 ms | 71.8 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimoxide (Realgrid) | cimoxide (Svedala) | gmss (Svedala) | graphdb (Realgrid) | graphdb (Svedala) | jena (Realgrid) | jena (Svedala) | libcimpp (Realgrid) | maplib (Realgrid) | maplib (Svedala) | opencgmes (Realgrid) | opencgmes (Svedala) | powsybl_cgmes (Realgrid) | powsybl_cgmes (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| get_generators | 9.3 ms | 292.4 μs | 106.6 μs | 319.1 μs | 116.7 μs | 506.0 μs | 100.3 μs | 5.4 ms | 485.6 μs | 351.1 μs | 775.6 μs | 96.9 μs | 254.4 μs | 60.2 μs | 2.2 ms | 265.9 μs | 416.1 μs | 57.4 μs | 7.4 ms | 1.5 ms | 0.1 μs | 0.1 μs |
| get_lines | 12.9 ms | 259.0 μs | 111.7 μs | 1.8 ms | 355.3 μs | 3.5 ms | 280.0 μs | 5.4 ms | 618.4 μs | 363.6 μs | 3.7 ms | 290.5 μs | 1.1 ms | 149.1 μs | 33.2 ms | 292.9 μs | 1.2 ms | 61.2 μs | 12.6 ms | 1.7 ms | 0.1 μs | 0.0 μs |
| get_loads | 26.3 ms | 878.1 μs | 299.6 μs | 1.1 ms | 205.7 μs | 1.9 ms | 268.9 μs | 12.8 ms | 1.2 ms | 897.6 μs | 2.2 ms | 217.8 μs | 1.1 ms | 173.7 μs | 16.1 ms | 194.2 μs | 2.1 ms | 156.3 μs | 11.2 ms | 1.7 ms | 0.1 μs | 0.1 μs |
| get_substations | 7.4 ms | 286.6 μs | 100.5 μs | 876.5 μs | 80.5 μs | 866.7 μs | 57.6 μs | 5.4 ms | 524.3 μs | 385.3 μs | 812.7 μs | 84.9 μs | 304.6 μs | 45.7 μs | 3.5 ms | 120.9 μs | 707.5 μs | 54.1 μs | 6.4 ms | 1.0 ms | 0.1 μs | 0.1 μs |

## CLI Tools

Benchmarked as subprocesses (full process lifecycle per run) - 
**not comparable** with the in-process library numbers above.

| Tool | Operation | Time (mean) | Peak RSS (MB) | Version |
|------|-----------|-------------|---------------|---------|
| cimgo (Realgrid) | validate | 4.34 s | 717.1 | N/A |
| cimgo (Realgrid) | convert | 3.69 s | 621.7 | N/A |
| cimgo (Svedala) | validate | 279.9 ms | 43.9 | N/A |
| cimgo (Svedala) | convert | 379.6 ms | 76.8 | N/A |
| pocket_rdf (Realgrid) | serialize | 28.47 s | 1250.0 | N/A |
| pocket_rdf (Realgrid) | query | 26.06 s | 1241.1 | N/A |
| pocket_rdf (Svedala) | serialize | 2.31 s | 142.0 | N/A |
| pocket_rdf (Svedala) | query | 2.21 s | 142.4 | N/A |

Per-tool details: see the `*_benchmark_report.md` files in this directory.
