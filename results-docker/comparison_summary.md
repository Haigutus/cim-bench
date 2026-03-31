# Benchmark Comparison Report

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.9-200.fc43.x86_64

## Performance Comparison

### Load Performance

| Library | Load Time (mean) | Memory (MB) | Elements | Notes |
|---------|------------------|-------------|----------|-------|
| cimgraph (Realgrid) | 12.87 s | 3258.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimgraph (Svedala) | 909.0 ms | 204.8 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| jena (Realgrid) | 1.58 s | 5105.4 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| jena (Realgrid) | 6.86 s | N/A | N/A |  |
| jena (Svedala) | 136.8 ms | 692.0 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| jena (Svedala) | 695.9 ms | N/A | N/A |  |
| libcimpp (Realgrid) | 21.35 s | 134.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Realgrid) | 2.14 s | 551.5 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Realgrid) | 308.6 ms | N/A | N/A |  |
| maplib (Svedala) | 251.2 ms | 175.9 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| maplib (Svedala) | 57.7 ms | N/A | N/A |  |
| opencgmes (Realgrid) | 1.07 s | 5330.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| opencgmes (Realgrid) | 3.96 s | N/A | N/A |  |
| opencgmes (Svedala) | 80.1 ms | 532.9 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| opencgmes (Svedala) | 349.4 ms | N/A | N/A |  |
| powsybl_cgmes (Realgrid) | 1.82 s | 3064.3 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| powsybl_cgmes (Realgrid) | 2.17 s | N/A | N/A |  |
| powsybl_cgmes (Svedala) | 251.1 ms | 610.3 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| powsybl_cgmes (Svedala) | 155.9 ms | N/A | N/A |  |
| pypowsybl (Realgrid) | 4.57 s | 4801.7 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Realgrid) | 2.97 s | N/A | N/A |  |
| pypowsybl (Svedala) | 413.2 ms | 951.9 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| pypowsybl (Svedala) | 338.9 ms | N/A | N/A |  |
| rdflib (Realgrid) | 18.79 s | 1518.2 MB | 7561 lines, 2694 gen, 13374 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Realgrid) | 17.94 s | N/A | N/A |  |
| rdflib (Svedala) | 1.56 s | 285.7 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Svedala) | 1.50 s | N/A | N/A |  |
| triplets (Realgrid) | 1.35 s | 594.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Realgrid) | 5.52 s | N/A | N/A |  |
| triplets (Svedala) | 116.1 ms | 43.2 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| triplets (Svedala) | 584.1 ms | N/A | N/A |  |
| veragrid (Realgrid) | 6.23 s | 1293.3 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Realgrid) | 12.99 s | N/A | N/A |  |
| veragrid (Svedala) | 436.2 ms | 452.0 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| veragrid (Svedala) | 919.2 ms | N/A | N/A |  |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | jena (Realgrid) | jena (Svedala) | libcimpp (Realgrid) | maplib (Realgrid) | maplib (Svedala) | opencgmes (Realgrid) | opencgmes (Svedala) | powsybl_cgmes (Realgrid) | powsybl_cgmes (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.1 μs | 291.1 μs | 89.0 μs | 5.2 ms | 411.2 μs | 324.0 μs | 279.6 μs | 154.7 μs | 193.2 μs | 55.1 μs | 2.7 ms | 284.5 μs | 402.7 μs | 49.4 μs | 274.7 ms | 21.1 ms | 0.1 μs | 0.1 μs |
| get_lines | 0.1 μs | 0.1 μs | 1.6 ms | 350.6 μs | 5.0 ms | 548.2 μs | 331.6 μs | 1.6 ms | 329.5 μs | 918.1 μs | 110.3 μs | 35.8 ms | 302.4 μs | 1.1 ms | 51.9 μs | 325.0 ms | 21.1 ms | 0.1 μs | 0.0 μs |
| get_loads | 0.2 μs | 0.2 μs | 1.0 ms | 239.6 μs | 11.0 ms | 1.1 ms | 910.3 μs | 875.1 μs | 301.6 μs | 1.6 ms | 187.9 μs | 20.5 ms | 211.5 μs | 1.9 ms | 134.6 μs | 645.5 ms | 41.3 ms | 0.1 μs | 0.1 μs |
| get_substations | 0.1 μs | 0.1 μs | 498.9 μs | 56.5 μs | 4.7 ms | 481.1 μs | 342.4 μs | 357.3 μs | 62.1 μs | 389.7 μs | 56.8 μs | 4.0 ms | 119.8 μs | 729.9 μs | 46.6 μs | 246.3 ms | 20.7 ms | 0.1 μs | 0.1 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 12.87 s
- **Min**: 11.86 s
- **Max**: 14.03 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 4.0 μs
- **Rounds**: 145922

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 24.3 μs
- **Rounds**: 189036

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 14.4 μs
- **Rounds**: 179534

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.6 μs
- **Rounds**: 68555

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 909.0 ms
- **Min**: 830.0 ms
- **Max**: 1.03 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.2 μs
- **Rounds**: 74544

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.5 μs
- **Rounds**: 73769

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 26.4 μs
- **Rounds**: 137476

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 2.3 μs
- **Rounds**: 67944

### jena (Realgrid)

#### Jena Load Realgrid

- **Mean**: 1.58 s
- **Min**: 1.52 s
- **Max**: 1.62 s
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 1.6 ms
- **Min**: 939.1 μs
- **Max**: 41.7 ms
- **Rounds**: 186

#### Jena Get Generators

- **Mean**: 291.1 μs
- **Min**: 169.9 μs
- **Max**: 30.5 ms
- **Rounds**: 1317

#### Jena Get Loads

- **Mean**: 1.0 ms
- **Min**: 805.5 μs
- **Max**: 2.8 ms
- **Rounds**: 345

#### Jena Get Substations

- **Mean**: 498.9 μs
- **Min**: 437.6 μs
- **Max**: 1.5 ms
- **Rounds**: 623

### jena (Realgrid)

#### Jena Export Realgrid

- **Mean**: 6.86 s
- **Min**: 6.58 s
- **Max**: 7.26 s
- **Rounds**: 5

### jena (Svedala)

#### Jena Load Svedala

- **Mean**: 136.8 ms
- **Min**: 102.8 ms
- **Max**: 157.0 ms
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 350.6 μs
- **Min**: 123.6 μs
- **Max**: 17.2 ms
- **Rounds**: 746

#### Jena Get Generators

- **Mean**: 89.0 μs
- **Min**: 65.2 μs
- **Max**: 1.4 ms
- **Rounds**: 3806

#### Jena Get Loads

- **Mean**: 239.6 μs
- **Min**: 150.9 μs
- **Max**: 24.4 ms
- **Rounds**: 2069

#### Jena Get Substations

- **Mean**: 56.5 μs
- **Min**: 42.7 μs
- **Max**: 20.7 ms
- **Rounds**: 5708

### jena (Svedala)

#### Jena Export Svedala

- **Mean**: 695.9 ms
- **Min**: 581.7 ms
- **Max**: 845.4 ms
- **Rounds**: 5

### libcimpp (Realgrid)

#### Libcimpp Load Realgrid

- **Mean**: 21.35 s
- **Min**: 21.29 s
- **Max**: 21.45 s
- **Rounds**: 5

#### Libcimpp Get Lines

- **Mean**: 5.0 ms
- **Min**: 4.2 ms
- **Max**: 12.2 ms
- **Rounds**: 79

#### Libcimpp Get Generators

- **Mean**: 5.2 ms
- **Min**: 4.4 ms
- **Max**: 10.4 ms
- **Rounds**: 75

#### Libcimpp Get Loads

- **Mean**: 11.0 ms
- **Min**: 9.9 ms
- **Max**: 16.9 ms
- **Rounds**: 52

#### Libcimpp Get Substations

- **Mean**: 4.7 ms
- **Min**: 3.9 ms
- **Max**: 9.6 ms
- **Rounds**: 107

### maplib (Realgrid)

#### Maplib Load Realgrid

- **Mean**: 2.14 s
- **Min**: 2.09 s
- **Max**: 2.17 s
- **Rounds**: 5

#### Maplib Get Lines

- **Mean**: 548.2 μs
- **Min**: 400.5 μs
- **Max**: 1.2 ms
- **Rounds**: 1522

#### Maplib Get Generators

- **Mean**: 411.2 μs
- **Min**: 308.2 μs
- **Max**: 3.0 ms
- **Rounds**: 1891

#### Maplib Get Loads

- **Mean**: 1.1 ms
- **Min**: 826.3 μs
- **Max**: 2.3 ms
- **Rounds**: 878

#### Maplib Get Substations

- **Mean**: 481.1 μs
- **Min**: 351.3 μs
- **Max**: 1.3 ms
- **Rounds**: 1797

### maplib (Realgrid)

#### Maplib Export Realgrid

- **Mean**: 308.6 ms
- **Min**: 270.0 ms
- **Max**: 363.7 ms
- **Rounds**: 6

### maplib (Svedala)

#### Maplib Load Svedala

- **Mean**: 251.2 ms
- **Min**: 243.4 ms
- **Max**: 260.0 ms
- **Rounds**: 5

#### Maplib Get Lines

- **Mean**: 331.6 μs
- **Min**: 235.8 μs
- **Max**: 3.1 ms
- **Rounds**: 1467

#### Maplib Get Generators

- **Mean**: 324.0 μs
- **Min**: 238.0 μs
- **Max**: 836.7 μs
- **Rounds**: 2264

#### Maplib Get Loads

- **Mean**: 910.3 μs
- **Min**: 718.5 μs
- **Max**: 2.1 ms
- **Rounds**: 960

#### Maplib Get Substations

- **Mean**: 342.4 μs
- **Min**: 256.0 μs
- **Max**: 2.5 ms
- **Rounds**: 1913

### maplib (Svedala)

#### Maplib Export Svedala

- **Mean**: 57.7 ms
- **Min**: 50.8 ms
- **Max**: 75.0 ms
- **Rounds**: 17

### opencgmes (Realgrid)

#### Opencgmes Load Realgrid

- **Mean**: 1.07 s
- **Min**: 908.9 ms
- **Max**: 1.23 s
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 1.6 ms
- **Min**: 1.1 ms
- **Max**: 4.7 ms
- **Rounds**: 147

#### Opencgmes Get Generators

- **Mean**: 279.6 μs
- **Min**: 162.2 μs
- **Max**: 3.2 ms
- **Rounds**: 1065

#### Opencgmes Get Loads

- **Mean**: 875.1 μs
- **Min**: 656.7 μs
- **Max**: 3.6 ms
- **Rounds**: 470

#### Opencgmes Get Substations

- **Mean**: 357.3 μs
- **Min**: 327.3 μs
- **Max**: 1.1 ms
- **Rounds**: 1338

### opencgmes (Realgrid)

#### Opencgmes Export Realgrid

- **Mean**: 3.96 s
- **Min**: 3.80 s
- **Max**: 4.12 s
- **Rounds**: 5

### opencgmes (Svedala)

#### Opencgmes Load Svedala

- **Mean**: 80.1 ms
- **Min**: 73.7 ms
- **Max**: 97.4 ms
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 329.5 μs
- **Min**: 103.5 μs
- **Max**: 2.5 ms
- **Rounds**: 665

#### Opencgmes Get Generators

- **Mean**: 154.7 μs
- **Min**: 74.1 μs
- **Max**: 91.4 ms
- **Rounds**: 3962

#### Opencgmes Get Loads

- **Mean**: 301.6 μs
- **Min**: 184.1 μs
- **Max**: 63.8 ms
- **Rounds**: 2103

#### Opencgmes Get Substations

- **Mean**: 62.1 μs
- **Min**: 42.9 μs
- **Max**: 12.9 ms
- **Rounds**: 2444

### opencgmes (Svedala)

#### Opencgmes Export Svedala

- **Mean**: 349.4 ms
- **Min**: 335.6 ms
- **Max**: 380.2 ms
- **Rounds**: 5

### powsybl_cgmes (Realgrid)

#### Powsybl Cgmes Load Realgrid

- **Mean**: 1.82 s
- **Min**: 1.74 s
- **Max**: 1.90 s
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 918.1 μs
- **Min**: 594.8 μs
- **Max**: 2.1 ms
- **Rounds**: 305

#### Powsybl Cgmes Get Generators

- **Mean**: 193.2 μs
- **Min**: 156.4 μs
- **Max**: 2.9 ms
- **Rounds**: 1184

#### Powsybl Cgmes Get Loads

- **Mean**: 1.6 ms
- **Min**: 1.1 ms
- **Max**: 62.3 ms
- **Rounds**: 272

#### Powsybl Cgmes Get Substations

- **Mean**: 389.7 μs
- **Min**: 295.5 μs
- **Max**: 1.5 ms
- **Rounds**: 631

### powsybl_cgmes (Realgrid)

#### Powsybl Cgmes Export Realgrid

- **Mean**: 2.17 s
- **Min**: 1.98 s
- **Max**: 2.27 s
- **Rounds**: 5

### powsybl_cgmes (Svedala)

#### Powsybl Cgmes Load Svedala

- **Mean**: 251.1 ms
- **Min**: 221.7 ms
- **Max**: 293.6 ms
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 110.3 μs
- **Min**: 50.1 μs
- **Max**: 1.2 ms
- **Rounds**: 1874

#### Powsybl Cgmes Get Generators

- **Mean**: 55.1 μs
- **Min**: 38.9 μs
- **Max**: 321.3 μs
- **Rounds**: 1856

#### Powsybl Cgmes Get Loads

- **Mean**: 187.9 μs
- **Min**: 101.8 μs
- **Max**: 77.2 ms
- **Rounds**: 1851

#### Powsybl Cgmes Get Substations

- **Mean**: 56.8 μs
- **Min**: 34.0 μs
- **Max**: 13.7 ms
- **Rounds**: 2296

### powsybl_cgmes (Svedala)

#### Powsybl Cgmes Export Svedala

- **Mean**: 155.9 ms
- **Min**: 135.7 ms
- **Max**: 177.0 ms
- **Rounds**: 5

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.57 s
- **Min**: 4.41 s
- **Max**: 4.74 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 35.8 ms
- **Min**: 34.6 ms
- **Max**: 38.2 ms
- **Rounds**: 29

#### Pypowsybl Get Generators

- **Mean**: 2.7 ms
- **Min**: 2.4 ms
- **Max**: 6.4 ms
- **Rounds**: 171

#### Pypowsybl Get Loads

- **Mean**: 20.5 ms
- **Min**: 16.8 ms
- **Max**: 70.3 ms
- **Rounds**: 42

#### Pypowsybl Get Substations

- **Mean**: 4.0 ms
- **Min**: 3.4 ms
- **Max**: 9.9 ms
- **Rounds**: 153

### pypowsybl (Realgrid)

#### Pypowsybl Export Realgrid

- **Mean**: 2.97 s
- **Min**: 2.94 s
- **Max**: 2.99 s
- **Rounds**: 5

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 413.2 ms
- **Min**: 382.2 ms
- **Max**: 445.8 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 302.4 μs
- **Min**: 277.9 μs
- **Max**: 1.5 ms
- **Rounds**: 1126

#### Pypowsybl Get Generators

- **Mean**: 284.5 μs
- **Min**: 262.8 μs
- **Max**: 1.2 ms
- **Rounds**: 1713

#### Pypowsybl Get Loads

- **Mean**: 211.5 μs
- **Min**: 187.4 μs
- **Max**: 25.4 ms
- **Rounds**: 2397

#### Pypowsybl Get Substations

- **Mean**: 119.8 μs
- **Min**: 111.6 μs
- **Max**: 714.9 μs
- **Rounds**: 3318

### pypowsybl (Svedala)

#### Pypowsybl Export Svedala

- **Mean**: 338.9 ms
- **Min**: 332.5 ms
- **Max**: 343.5 ms
- **Rounds**: 5

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 18.79 s
- **Min**: 18.63 s
- **Max**: 18.88 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 1.1 ms
- **Min**: 1.1 ms
- **Max**: 1.8 ms
- **Rounds**: 400

#### Rdflib Get Generators

- **Mean**: 402.7 μs
- **Min**: 392.3 μs
- **Max**: 821.4 μs
- **Rounds**: 1298

#### Rdflib Get Loads

- **Mean**: 1.9 ms
- **Min**: 1.9 ms
- **Max**: 2.7 ms
- **Rounds**: 297

#### Rdflib Get Substations

- **Mean**: 729.9 μs
- **Min**: 676.6 μs
- **Max**: 1.9 ms
- **Rounds**: 838

### rdflib (Realgrid)

#### Rdflib Export Realgrid

- **Mean**: 17.94 s
- **Min**: 17.72 s
- **Max**: 18.57 s
- **Rounds**: 5

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 1.56 s
- **Min**: 1.54 s
- **Max**: 1.58 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 51.9 μs
- **Min**: 49.4 μs
- **Max**: 135.4 μs
- **Rounds**: 5009

#### Rdflib Get Generators

- **Mean**: 49.4 μs
- **Min**: 47.2 μs
- **Max**: 136.9 μs
- **Rounds**: 7547

#### Rdflib Get Loads

- **Mean**: 134.6 μs
- **Min**: 129.8 μs
- **Max**: 313.6 μs
- **Rounds**: 4333

#### Rdflib Get Substations

- **Mean**: 46.6 μs
- **Min**: 44.4 μs
- **Max**: 133.7 μs
- **Rounds**: 9314

### rdflib (Svedala)

#### Rdflib Export Svedala

- **Mean**: 1.50 s
- **Min**: 1.50 s
- **Max**: 1.51 s
- **Rounds**: 5

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.35 s
- **Min**: 1.22 s
- **Max**: 1.42 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 325.0 ms
- **Min**: 304.5 ms
- **Max**: 357.4 ms
- **Rounds**: 5

#### Triplets Get Generators

- **Mean**: 274.7 ms
- **Min**: 261.8 ms
- **Max**: 291.5 ms
- **Rounds**: 5

#### Triplets Get Loads

- **Mean**: 645.5 ms
- **Min**: 614.6 ms
- **Max**: 715.3 ms
- **Rounds**: 5

#### Triplets Get Substations

- **Mean**: 246.3 ms
- **Min**: 240.7 ms
- **Max**: 255.6 ms
- **Rounds**: 5

### triplets (Realgrid)

#### Triplets Export Realgrid

- **Mean**: 5.52 s
- **Min**: 5.47 s
- **Max**: 5.59 s
- **Rounds**: 5

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 116.1 ms
- **Min**: 101.8 ms
- **Max**: 121.3 ms
- **Rounds**: 11

#### Triplets Get Lines

- **Mean**: 21.1 ms
- **Min**: 20.2 ms
- **Max**: 29.2 ms
- **Rounds**: 46

#### Triplets Get Generators

- **Mean**: 21.1 ms
- **Min**: 20.4 ms
- **Max**: 22.1 ms
- **Rounds**: 45

#### Triplets Get Loads

- **Mean**: 41.3 ms
- **Min**: 39.8 ms
- **Max**: 44.1 ms
- **Rounds**: 22

#### Triplets Get Substations

- **Mean**: 20.7 ms
- **Min**: 19.8 ms
- **Max**: 22.0 ms
- **Rounds**: 44

### triplets (Svedala)

#### Triplets Export Svedala

- **Mean**: 584.1 ms
- **Min**: 568.9 ms
- **Max**: 598.5 ms
- **Rounds**: 5

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 6.23 s
- **Min**: 5.53 s
- **Max**: 6.85 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.2 μs
- **Rounds**: 108614

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.3 μs
- **Rounds**: 87018

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 7.4 μs
- **Rounds**: 183824

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.2 μs
- **Rounds**: 90082

### veragrid (Realgrid)

#### Veragrid Export Realgrid

- **Mean**: 12.99 s
- **Min**: 9.09 s
- **Max**: 16.79 s
- **Rounds**: 5

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 436.2 ms
- **Min**: 393.6 ms
- **Max**: 458.1 ms
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.4 μs
- **Rounds**: 107794

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 92507

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 6.0 μs
- **Rounds**: 142390

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.3 μs
- **Rounds**: 93721

### veragrid (Svedala)

#### Veragrid Export Svedala

- **Mean**: 919.2 ms
- **Min**: 862.4 ms
- **Max**: 972.9 ms
- **Rounds**: 5
