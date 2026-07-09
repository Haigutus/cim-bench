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

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 25.15 s
- **Min**: 18.33 s
- **Max**: 34.41 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 55.9 μs
- **Rounds**: 104178

#### Cimgraph Get Generators

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 43.5 μs
- **Rounds**: 133262

#### Cimgraph Get Loads

- **Mean**: 0.5 μs
- **Min**: 0.4 μs
- **Max**: 22.1 μs
- **Rounds**: 90245

#### Cimgraph Get Substations

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 18.5 μs
- **Rounds**: 182783

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 1.54 s
- **Min**: 1.33 s
- **Max**: 1.86 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 41.0 μs
- **Rounds**: 111895

#### Cimgraph Get Generators

- **Mean**: 0.4 μs
- **Min**: 0.2 μs
- **Max**: 21.5 μs
- **Rounds**: 124611

#### Cimgraph Get Loads

- **Mean**: 0.6 μs
- **Min**: 0.4 μs
- **Max**: 88.2 μs
- **Rounds**: 111273

#### Cimgraph Get Substations

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 19.2 μs
- **Rounds**: 199599

#### Cimgraph Export Svedala

- **Mean**: 1.72 s
- **Min**: 1.51 s
- **Max**: 1.91 s
- **Rounds**: 5

### jena (Realgrid)

#### Jena Load Realgrid

- **Mean**: 2.05 s
- **Min**: 1.77 s
- **Max**: 2.52 s
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 7.9 ms
- **Min**: 3.9 ms
- **Max**: 31.7 ms
- **Rounds**: 94

#### Jena Get Generators

- **Mean**: 1.7 ms
- **Min**: 917.4 μs
- **Max**: 3.9 ms
- **Rounds**: 189

#### Jena Get Loads

- **Mean**: 12.2 ms
- **Min**: 5.5 ms
- **Max**: 23.8 ms
- **Rounds**: 26

#### Jena Get Substations

- **Mean**: 2.9 ms
- **Min**: 2.0 ms
- **Max**: 9.3 ms
- **Rounds**: 143

#### Jena Export Realgrid

- **Mean**: 5.88 s
- **Min**: 4.77 s
- **Max**: 7.79 s
- **Rounds**: 5

### jena (Svedala)

#### Jena Load Svedala

- **Mean**: 259.7 ms
- **Min**: 213.2 ms
- **Max**: 303.0 ms
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 1.1 ms
- **Min**: 445.3 μs
- **Max**: 3.6 ms
- **Rounds**: 317

#### Jena Get Generators

- **Mean**: 452.2 μs
- **Min**: 159.0 μs
- **Max**: 3.1 ms
- **Rounds**: 846

#### Jena Get Loads

- **Mean**: 792.3 μs
- **Min**: 376.2 μs
- **Max**: 24.4 ms
- **Rounds**: 1024

#### Jena Get Substations

- **Mean**: 230.9 μs
- **Min**: 122.8 μs
- **Max**: 1.7 ms
- **Rounds**: 2753

#### Jena Export Svedala

- **Mean**: 832.2 ms
- **Min**: 749.2 ms
- **Max**: 940.5 ms
- **Rounds**: 5

### libcimpp (Realgrid)

#### Libcimpp Load Realgrid

- **Mean**: 22.74 s
- **Min**: 22.57 s
- **Max**: 22.96 s
- **Rounds**: 5

#### Libcimpp Get Lines

- **Mean**: 8.1 ms
- **Min**: 6.5 ms
- **Max**: 12.0 ms
- **Rounds**: 78

#### Libcimpp Get Generators

- **Mean**: 8.4 ms
- **Min**: 6.6 ms
- **Max**: 11.3 ms
- **Rounds**: 79

#### Libcimpp Get Loads

- **Mean**: 19.5 ms
- **Min**: 18.0 ms
- **Max**: 21.4 ms
- **Rounds**: 54

#### Libcimpp Get Substations

- **Mean**: 8.3 ms
- **Min**: 6.1 ms
- **Max**: 11.6 ms
- **Rounds**: 87

### maplib (Realgrid)

#### Maplib Load Realgrid

- **Mean**: 4.53 s
- **Min**: 4.42 s
- **Max**: 4.70 s
- **Rounds**: 5

#### Maplib Get Lines

- **Mean**: 1.8 ms
- **Min**: 1.1 ms
- **Max**: 3.7 ms
- **Rounds**: 525

#### Maplib Get Generators

- **Mean**: 1.3 ms
- **Min**: 916.3 μs
- **Max**: 3.6 ms
- **Rounds**: 718

#### Maplib Get Loads

- **Mean**: 3.2 ms
- **Min**: 2.1 ms
- **Max**: 6.7 ms
- **Rounds**: 309

#### Maplib Get Substations

- **Mean**: 1.5 ms
- **Min**: 990.3 μs
- **Max**: 5.4 ms
- **Rounds**: 651

#### Maplib Export Realgrid

- **Mean**: 54.74 s
- **Min**: 54.20 s
- **Max**: 55.50 s
- **Rounds**: 5

### maplib (Svedala)

#### Maplib Load Svedala

- **Mean**: 526.9 ms
- **Min**: 464.1 ms
- **Max**: 546.0 ms
- **Rounds**: 5

#### Maplib Get Lines

- **Mean**: 919.2 μs
- **Min**: 639.1 μs
- **Max**: 3.5 ms
- **Rounds**: 749

#### Maplib Get Generators

- **Mean**: 1.0 ms
- **Min**: 639.8 μs
- **Max**: 2.5 ms
- **Rounds**: 1009

#### Maplib Get Loads

- **Mean**: 2.4 ms
- **Min**: 1.6 ms
- **Max**: 4.1 ms
- **Rounds**: 397

#### Maplib Get Substations

- **Mean**: 975.5 μs
- **Min**: 663.0 μs
- **Max**: 2.5 ms
- **Rounds**: 940

#### Maplib Export Svedala

- **Mean**: 4.42 s
- **Min**: 4.22 s
- **Max**: 4.62 s
- **Rounds**: 5

### opencgmes (Realgrid)

#### Opencgmes Load Realgrid

- **Mean**: 2.18 s
- **Min**: 1.93 s
- **Max**: 2.43 s
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 13.2 ms
- **Min**: 5.1 ms
- **Max**: 32.3 ms
- **Rounds**: 39

#### Opencgmes Get Generators

- **Mean**: 2.8 ms
- **Min**: 1.1 ms
- **Max**: 9.5 ms
- **Rounds**: 85

#### Opencgmes Get Loads

- **Mean**: 7.5 ms
- **Min**: 4.0 ms
- **Max**: 15.0 ms
- **Rounds**: 61

#### Opencgmes Get Substations

- **Mean**: 4.6 ms
- **Min**: 1.9 ms
- **Max**: 14.3 ms
- **Rounds**: 67

#### Opencgmes Export Realgrid

- **Mean**: 7.56 s
- **Min**: 6.87 s
- **Max**: 8.50 s
- **Rounds**: 5

### opencgmes (Svedala)

#### Opencgmes Load Svedala

- **Mean**: 268.6 ms
- **Min**: 169.5 ms
- **Max**: 467.8 ms
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 1.4 ms
- **Min**: 547.2 μs
- **Max**: 5.4 ms
- **Rounds**: 191

#### Opencgmes Get Generators

- **Mean**: 644.0 μs
- **Min**: 192.4 μs
- **Max**: 4.4 ms
- **Rounds**: 706

#### Opencgmes Get Loads

- **Mean**: 909.9 μs
- **Min**: 431.5 μs
- **Max**: 23.4 ms
- **Rounds**: 861

#### Opencgmes Get Substations

- **Mean**: 247.7 μs
- **Min**: 168.3 μs
- **Max**: 3.0 ms
- **Rounds**: 1365

#### Opencgmes Export Svedala

- **Mean**: 801.6 ms
- **Min**: 717.9 ms
- **Max**: 920.1 ms
- **Rounds**: 5

### powsybl_cgmes (Realgrid)

#### Powsybl Cgmes Load Realgrid

- **Mean**: 3.53 s
- **Min**: 3.28 s
- **Max**: 3.73 s
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 3.4 ms
- **Min**: 1.8 ms
- **Max**: 152.4 ms
- **Rounds**: 220

#### Powsybl Cgmes Get Generators

- **Mean**: 903.6 μs
- **Min**: 549.0 μs
- **Max**: 3.1 ms
- **Rounds**: 248

#### Powsybl Cgmes Get Loads

- **Mean**: 2.8 ms
- **Min**: 2.2 ms
- **Max**: 6.5 ms
- **Rounds**: 124

#### Powsybl Cgmes Get Substations

- **Mean**: 909.5 μs
- **Min**: 739.0 μs
- **Max**: 2.2 ms
- **Rounds**: 376

#### Powsybl Cgmes Export Realgrid

- **Mean**: 3.88 s
- **Min**: 3.79 s
- **Max**: 4.00 s
- **Rounds**: 5

### powsybl_cgmes (Svedala)

#### Powsybl Cgmes Load Svedala

- **Mean**: 563.9 ms
- **Min**: 495.5 ms
- **Max**: 720.6 ms
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 520.4 μs
- **Min**: 140.1 μs
- **Max**: 2.7 ms
- **Rounds**: 921

#### Powsybl Cgmes Get Generators

- **Mean**: 241.9 μs
- **Min**: 106.1 μs
- **Max**: 33.0 ms
- **Rounds**: 2490

#### Powsybl Cgmes Get Loads

- **Mean**: 562.0 μs
- **Min**: 380.4 μs
- **Max**: 1.6 ms
- **Rounds**: 554

#### Powsybl Cgmes Get Substations

- **Mean**: 223.6 μs
- **Min**: 104.0 μs
- **Max**: 770.1 μs
- **Rounds**: 1715

#### Powsybl Cgmes Export Svedala

- **Mean**: 355.0 ms
- **Min**: 281.9 ms
- **Max**: 539.5 ms
- **Rounds**: 5

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 9.86 s
- **Min**: 8.82 s
- **Max**: 10.83 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 51.9 ms
- **Min**: 43.5 ms
- **Max**: 63.4 ms
- **Rounds**: 16

#### Pypowsybl Get Generators

- **Mean**: 6.8 ms
- **Min**: 4.4 ms
- **Max**: 11.3 ms
- **Rounds**: 129

#### Pypowsybl Get Loads

- **Mean**: 31.6 ms
- **Min**: 24.7 ms
- **Max**: 46.3 ms
- **Rounds**: 30

#### Pypowsybl Get Substations

- **Mean**: 10.4 ms
- **Min**: 8.1 ms
- **Max**: 15.2 ms
- **Rounds**: 103

#### Pypowsybl Export Realgrid

- **Mean**: 3.88 s
- **Min**: 3.52 s
- **Max**: 4.20 s
- **Rounds**: 5

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 1.34 s
- **Min**: 1.18 s
- **Max**: 1.50 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 1.5 ms
- **Min**: 900.6 μs
- **Max**: 3.2 ms
- **Rounds**: 440

#### Pypowsybl Get Generators

- **Mean**: 1.4 ms
- **Min**: 1.1 ms
- **Max**: 2.4 ms
- **Rounds**: 420

#### Pypowsybl Get Loads

- **Mean**: 1.0 ms
- **Min**: 596.0 μs
- **Max**: 2.5 ms
- **Rounds**: 555

#### Pypowsybl Get Substations

- **Mean**: 625.6 μs
- **Min**: 431.3 μs
- **Max**: 1.3 ms
- **Rounds**: 979

#### Pypowsybl Export Svedala

- **Mean**: 452.5 ms
- **Min**: 401.1 ms
- **Max**: 553.4 ms
- **Rounds**: 5

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 30.75 s
- **Min**: 24.95 s
- **Max**: 39.25 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 1.4 ms
- **Min**: 1.3 ms
- **Max**: 2.2 ms
- **Rounds**: 382

#### Rdflib Get Generators

- **Mean**: 483.3 μs
- **Min**: 443.4 μs
- **Max**: 762.4 μs
- **Rounds**: 875

#### Rdflib Get Loads

- **Mean**: 2.1 ms
- **Min**: 1.9 ms
- **Max**: 3.2 ms
- **Rounds**: 283

#### Rdflib Get Substations

- **Mean**: 710.8 μs
- **Min**: 670.1 μs
- **Max**: 1.4 ms
- **Rounds**: 844

#### Rdflib Export Realgrid

- **Mean**: 29.66 s
- **Min**: 24.04 s
- **Max**: 33.56 s
- **Rounds**: 5

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 4.74 s
- **Min**: 4.35 s
- **Max**: 5.16 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 186.2 μs
- **Min**: 131.6 μs
- **Max**: 935.8 μs
- **Rounds**: 2607

#### Rdflib Get Generators

- **Mean**: 172.7 μs
- **Min**: 124.5 μs
- **Max**: 758.0 μs
- **Rounds**: 3472

#### Rdflib Get Loads

- **Mean**: 509.0 μs
- **Min**: 353.0 μs
- **Max**: 2.3 ms
- **Rounds**: 1793

#### Rdflib Get Substations

- **Mean**: 170.5 μs
- **Min**: 120.9 μs
- **Max**: 970.0 μs
- **Rounds**: 2912

#### Rdflib Export Svedala

- **Mean**: 4.66 s
- **Min**: 4.50 s
- **Max**: 4.77 s
- **Rounds**: 5

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 178.3 ms
- **Min**: 171.4 ms
- **Max**: 187.7 ms
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 36.2 ms
- **Min**: 26.1 ms
- **Max**: 42.4 ms
- **Rounds**: 45

#### Triplets Get Generators

- **Mean**: 23.8 ms
- **Min**: 22.0 ms
- **Max**: 28.3 ms
- **Rounds**: 43

#### Triplets Get Loads

- **Mean**: 30.9 ms
- **Min**: 27.9 ms
- **Max**: 34.3 ms
- **Rounds**: 32

#### Triplets Get Substations

- **Mean**: 19.0 ms
- **Min**: 16.6 ms
- **Max**: 23.4 ms
- **Rounds**: 53

#### Triplets Export Realgrid

- **Mean**: 2.02 s
- **Min**: 1.96 s
- **Max**: 2.09 s
- **Rounds**: 5

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 21.9 ms
- **Min**: 17.6 ms
- **Max**: 25.8 ms
- **Rounds**: 25

#### Triplets Get Lines

- **Mean**: 6.7 ms
- **Min**: 4.8 ms
- **Max**: 13.7 ms
- **Rounds**: 147

#### Triplets Get Generators

- **Mean**: 5.9 ms
- **Min**: 3.9 ms
- **Max**: 8.7 ms
- **Rounds**: 153

#### Triplets Get Loads

- **Mean**: 6.7 ms
- **Min**: 4.2 ms
- **Max**: 10.8 ms
- **Rounds**: 149

#### Triplets Get Substations

- **Mean**: 5.1 ms
- **Min**: 3.6 ms
- **Max**: 10.5 ms
- **Rounds**: 200

#### Triplets Export Svedala

- **Mean**: 330.4 ms
- **Min**: 301.3 ms
- **Max**: 352.5 ms
- **Rounds**: 5

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 18.79 s
- **Min**: 16.56 s
- **Max**: 24.19 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 72.0 μs
- **Rounds**: 158706

#### Veragrid Get Generators

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 125.5 μs
- **Rounds**: 194552

#### Veragrid Get Loads

- **Mean**: 0.3 μs
- **Min**: 0.3 μs
- **Max**: 29.3 μs
- **Rounds**: 122325

#### Veragrid Get Substations

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 41.3 μs
- **Rounds**: 146349

#### Veragrid Export Realgrid

- **Mean**: 18.17 s
- **Min**: 17.14 s
- **Max**: 20.23 s
- **Rounds**: 5

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 1.70 s
- **Min**: 1.56 s
- **Max**: 2.03 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 2.6 μs
- **Rounds**: 55948

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 3.4 μs
- **Rounds**: 198414

#### Veragrid Get Loads

- **Mean**: 0.3 μs
- **Min**: 0.3 μs
- **Max**: 43.4 μs
- **Rounds**: 131493

#### Veragrid Get Substations

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 30.0 μs
- **Rounds**: 158428

#### Veragrid Export Svedala

- **Mean**: 1.52 s
- **Min**: 1.28 s
- **Max**: 1.67 s
- **Rounds**: 5
