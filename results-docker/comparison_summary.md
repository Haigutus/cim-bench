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
| graphdb (Realgrid) | 5.60 s | 2457.4 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| graphdb (Svedala) | 712.3 ms | 1344.3 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| jena (Realgrid) | 1.58 s | 2586.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| jena (Svedala) | 120.1 ms | 402.0 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| libcimpp (Realgrid) | 19.53 s | 133.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Realgrid) | 2.01 s | 454.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Svedala) | 218.0 ms | 140.6 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| opencgmes (Realgrid) | 1.10 s | 3055.9 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| opencgmes (Svedala) | 88.4 ms | 293.5 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| powsybl_cgmes (Realgrid) | 1.77 s | 2721.5 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| powsybl_cgmes (Svedala) | 252.8 ms | 467.6 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.24 s | 2089.0 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 428.4 ms | 1566.6 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 23.27 s | 1078.4 MB | 7561 lines, 2694 gen, 13374 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 2.00 s | 207.5 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 159.1 ms | 370.5 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 10.1 ms | 82.9 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 10.80 s | 304.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 701.7 ms | 71.8 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimoxide (Realgrid) | cimoxide (Svedala) | gmss (Svedala) | graphdb (Realgrid) | graphdb (Svedala) | jena (Realgrid) | jena (Svedala) | libcimpp (Realgrid) | maplib (Realgrid) | maplib (Svedala) | opencgmes (Realgrid) | opencgmes (Svedala) | powsybl_cgmes (Realgrid) | powsybl_cgmes (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| get_generators | 9.3 ms | 292.4 μs | 106.6 μs | 409.6 μs | 137.9 μs | 519.2 μs | 165.9 μs | 5.4 ms | 459.0 μs | 331.3 μs | 521.7 μs | 160.7 μs | 288.3 μs | 110.1 μs | 2.2 ms | 265.9 μs | 443.7 μs | 68.8 μs | 7.4 ms | 1.5 ms | 0.1 μs | 0.1 μs |
| get_lines | 12.9 ms | 259.0 μs | 111.7 μs | 252.1 ms | 5.9 ms | 203.5 ms | 4.1 ms | 5.4 ms | 44.6 ms | 14.6 ms | 144.9 ms | 4.7 ms | 347.4 ms | 8.3 ms | 33.2 ms | 292.9 μs | 446.88 s | 805.7 ms | 12.6 ms | 1.7 ms | 0.1 μs | 0.0 μs |
| get_loads | 26.3 ms | 878.1 μs | 299.6 μs | 1.2 ms | 288.6 μs | 4.9 ms | 295.9 μs | 12.8 ms | 1.1 ms | 869.9 μs | 2.5 ms | 251.6 μs | 983.1 μs | 161.8 μs | 16.1 ms | 194.2 μs | 2.1 ms | 199.8 μs | 11.2 ms | 1.7 ms | 0.1 μs | 0.1 μs |
| get_substations | 7.4 ms | 286.6 μs | 100.5 μs | 718.6 μs | 82.4 μs | 864.4 μs | 64.3 μs | 5.4 ms | 485.3 μs | 355.0 μs | 744.9 μs | 81.7 μs | 330.9 μs | 74.5 μs | 3.5 ms | 120.9 μs | 750.0 μs | 66.3 μs | 6.4 ms | 1.0 ms | 0.1 μs | 0.1 μs |

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
