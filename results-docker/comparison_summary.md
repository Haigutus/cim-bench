# Benchmark Comparison Report

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.19.11-200.fc43.x86_64

## Performance Comparison

### Load Performance

| Library | Load Time (mean) | Memory (MB) | Elements | Notes |
|---------|------------------|-------------|----------|-------|
| cimgraph (Realgrid) | 25.86 s | 3175.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimgraph (Svedala) | 905.6 ms | 211.6 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| jena (Realgrid) | 1.59 s | 2525.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| jena (Svedala) | 124.1 ms | 427.9 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| libcimpp (Realgrid) | 20.11 s | 134.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Realgrid) | 2.18 s | 576.3 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Svedala) | 254.0 ms | 179.5 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| opencgmes (Realgrid) | 1.04 s | 3625.2 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| opencgmes (Svedala) | 79.2 ms | 351.4 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| powsybl_cgmes (Realgrid) | 1.75 s | 3159.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| powsybl_cgmes (Svedala) | 245.4 ms | 449.3 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.32 s | 1640.2 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 419.7 ms | 1047.8 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 19.42 s | 1522.6 MB | 7561 lines, 2694 gen, 13374 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 1.64 s | 285.5 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.36 s | 591.3 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 118.0 ms | 43.3 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 6.90 s | 634.0 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 470.4 ms | 82.1 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | jena (Realgrid) | jena (Svedala) | libcimpp (Realgrid) | maplib (Realgrid) | maplib (Svedala) | opencgmes (Realgrid) | opencgmes (Svedala) | powsybl_cgmes (Realgrid) | powsybl_cgmes (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.1 μs | 565.1 μs | 104.2 μs | 6.8 ms | 452.2 μs | 341.4 μs | 236.1 μs | 172.2 μs | 248.5 μs | 53.2 μs | 2.7 ms | 266.9 μs | 442.2 μs | 51.3 μs | 268.8 ms | 21.4 ms | 0.1 μs | 0.1 μs |
| get_lines | 0.1 μs | 0.1 μs | 3.0 ms | 380.6 μs | 6.8 ms | 609.0 μs | 366.4 μs | 1.9 ms | 438.4 μs | 1.2 ms | 142.0 μs | 36.4 ms | 284.8 μs | 1.2 ms | 57.3 μs | 306.5 ms | 21.2 ms | 0.1 μs | 0.0 μs |
| get_loads | 0.2 μs | 0.2 μs | 2.4 ms | 205.3 μs | 16.3 ms | 1.2 ms | 948.0 μs | 947.6 μs | 295.7 μs | 1.0 ms | 149.0 μs | 21.3 ms | 189.8 μs | 2.3 ms | 140.9 μs | 625.7 ms | 42.7 ms | 0.1 μs | 0.1 μs |
| get_substations | 0.1 μs | 0.1 μs | 894.9 μs | 109.8 μs | 7.2 ms | 517.6 μs | 380.7 μs | 382.5 μs | 70.5 μs | 335.3 μs | 50.6 μs | 4.5 ms | 121.9 μs | 770.4 μs | 49.3 μs | 254.6 ms | 21.0 ms | 0.1 μs | 0.1 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 25.86 s
- **Min**: 13.57 s
- **Max**: 59.81 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 35.0 μs
- **Rounds**: 143823

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 28.9 μs
- **Rounds**: 162023

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 17.8 μs
- **Rounds**: 164420

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.0 μs
- **Rounds**: 59731

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 905.6 ms
- **Min**: 831.7 ms
- **Max**: 1.01 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 11.1 μs
- **Rounds**: 114326

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.4 μs
- **Rounds**: 74322

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 29.3 μs
- **Rounds**: 108015

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.7 μs
- **Rounds**: 59200

#### Cimgraph Export Svedala

- **Mean**: 541.2 ms
- **Min**: 523.5 ms
- **Max**: 561.7 ms
- **Rounds**: 5

### jena (Realgrid)

#### Jena Load Realgrid

- **Mean**: 1.59 s
- **Min**: 1.58 s
- **Max**: 1.62 s
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 3.0 ms
- **Min**: 1.7 ms
- **Max**: 9.0 ms
- **Rounds**: 86

#### Jena Get Generators

- **Mean**: 565.1 μs
- **Min**: 351.6 μs
- **Max**: 25.8 ms
- **Rounds**: 462

#### Jena Get Loads

- **Mean**: 2.4 ms
- **Min**: 1.3 ms
- **Max**: 6.4 ms
- **Rounds**: 134

#### Jena Get Substations

- **Mean**: 894.9 μs
- **Min**: 769.1 μs
- **Max**: 3.8 ms
- **Rounds**: 268

#### Jena Export Realgrid

- **Mean**: 4.38 s
- **Min**: 4.29 s
- **Max**: 4.49 s
- **Rounds**: 5

### jena (Svedala)

#### Jena Load Svedala

- **Mean**: 124.1 ms
- **Min**: 107.2 ms
- **Max**: 162.6 ms
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 380.6 μs
- **Min**: 139.2 μs
- **Max**: 20.9 ms
- **Rounds**: 595

#### Jena Get Generators

- **Mean**: 104.2 μs
- **Min**: 65.6 μs
- **Max**: 1.8 ms
- **Rounds**: 2673

#### Jena Get Loads

- **Mean**: 205.3 μs
- **Min**: 169.8 μs
- **Max**: 13.7 ms
- **Rounds**: 1420

#### Jena Get Substations

- **Mean**: 109.8 μs
- **Min**: 48.2 μs
- **Max**: 73.9 ms
- **Rounds**: 3993

#### Jena Export Svedala

- **Mean**: 434.9 ms
- **Min**: 410.2 ms
- **Max**: 522.2 ms
- **Rounds**: 5

### libcimpp (Realgrid)

#### Libcimpp Load Realgrid

- **Mean**: 20.11 s
- **Min**: 19.93 s
- **Max**: 20.23 s
- **Rounds**: 5

#### Libcimpp Get Lines

- **Mean**: 6.8 ms
- **Min**: 3.6 ms
- **Max**: 13.4 ms
- **Rounds**: 78

#### Libcimpp Get Generators

- **Mean**: 6.8 ms
- **Min**: 3.7 ms
- **Max**: 14.0 ms
- **Rounds**: 72

#### Libcimpp Get Loads

- **Mean**: 16.3 ms
- **Min**: 9.8 ms
- **Max**: 23.2 ms
- **Rounds**: 60

#### Libcimpp Get Substations

- **Mean**: 7.2 ms
- **Min**: 3.7 ms
- **Max**: 16.8 ms
- **Rounds**: 111

### maplib (Realgrid)

#### Maplib Load Realgrid

- **Mean**: 2.18 s
- **Min**: 2.15 s
- **Max**: 2.22 s
- **Rounds**: 5

#### Maplib Get Lines

- **Mean**: 609.0 μs
- **Min**: 434.9 μs
- **Max**: 3.1 ms
- **Rounds**: 958

#### Maplib Get Generators

- **Mean**: 452.2 μs
- **Min**: 327.0 μs
- **Max**: 3.2 ms
- **Rounds**: 1590

#### Maplib Get Loads

- **Mean**: 1.2 ms
- **Min**: 864.5 μs
- **Max**: 4.1 ms
- **Rounds**: 766

#### Maplib Get Substations

- **Mean**: 517.6 μs
- **Min**: 383.0 μs
- **Max**: 2.2 ms
- **Rounds**: 1964

#### Maplib Export Realgrid

- **Mean**: 16.79 s
- **Min**: 16.71 s
- **Max**: 16.96 s
- **Rounds**: 5

### maplib (Svedala)

#### Maplib Load Svedala

- **Mean**: 254.0 ms
- **Min**: 243.3 ms
- **Max**: 270.9 ms
- **Rounds**: 5

#### Maplib Get Lines

- **Mean**: 366.4 μs
- **Min**: 251.3 μs
- **Max**: 2.0 ms
- **Rounds**: 1438

#### Maplib Get Generators

- **Mean**: 341.4 μs
- **Min**: 246.0 μs
- **Max**: 3.1 ms
- **Rounds**: 1767

#### Maplib Get Loads

- **Mean**: 948.0 μs
- **Min**: 742.2 μs
- **Max**: 3.8 ms
- **Rounds**: 799

#### Maplib Get Substations

- **Mean**: 380.7 μs
- **Min**: 255.7 μs
- **Max**: 1.5 ms
- **Rounds**: 2565

#### Maplib Export Svedala

- **Mean**: 1.41 s
- **Min**: 1.38 s
- **Max**: 1.42 s
- **Rounds**: 5

### opencgmes (Realgrid)

#### Opencgmes Load Realgrid

- **Mean**: 1.04 s
- **Min**: 959.9 ms
- **Max**: 1.20 s
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 1.9 ms
- **Min**: 855.1 μs
- **Max**: 4.8 ms
- **Rounds**: 178

#### Opencgmes Get Generators

- **Mean**: 236.1 μs
- **Min**: 152.2 μs
- **Max**: 3.1 ms
- **Rounds**: 1595

#### Opencgmes Get Loads

- **Mean**: 947.6 μs
- **Min**: 659.2 μs
- **Max**: 3.4 ms
- **Rounds**: 446

#### Opencgmes Get Substations

- **Mean**: 382.5 μs
- **Min**: 304.8 μs
- **Max**: 40.5 ms
- **Rounds**: 1335

#### Opencgmes Export Realgrid

- **Mean**: 3.91 s
- **Min**: 3.84 s
- **Max**: 4.15 s
- **Rounds**: 5

### opencgmes (Svedala)

#### Opencgmes Load Svedala

- **Mean**: 79.2 ms
- **Min**: 66.5 ms
- **Max**: 96.7 ms
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 438.4 μs
- **Min**: 155.5 μs
- **Max**: 65.6 ms
- **Rounds**: 666

#### Opencgmes Get Generators

- **Mean**: 172.2 μs
- **Min**: 70.5 μs
- **Max**: 80.8 ms
- **Rounds**: 1554

#### Opencgmes Get Loads

- **Mean**: 295.7 μs
- **Min**: 151.8 μs
- **Max**: 54.2 ms
- **Rounds**: 1899

#### Opencgmes Get Substations

- **Mean**: 70.5 μs
- **Min**: 41.9 μs
- **Max**: 23.7 ms
- **Rounds**: 6089

#### Opencgmes Export Svedala

- **Mean**: 365.6 ms
- **Min**: 329.1 ms
- **Max**: 419.1 ms
- **Rounds**: 5

### powsybl_cgmes (Realgrid)

#### Powsybl Cgmes Load Realgrid

- **Mean**: 1.75 s
- **Min**: 1.65 s
- **Max**: 1.83 s
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 1.2 ms
- **Min**: 788.5 μs
- **Max**: 2.7 ms
- **Rounds**: 273

#### Powsybl Cgmes Get Generators

- **Mean**: 248.5 μs
- **Min**: 199.1 μs
- **Max**: 1.5 ms
- **Rounds**: 1145

#### Powsybl Cgmes Get Loads

- **Mean**: 1.0 ms
- **Min**: 868.6 μs
- **Max**: 3.1 ms
- **Rounds**: 233

#### Powsybl Cgmes Get Substations

- **Mean**: 335.3 μs
- **Min**: 291.4 μs
- **Max**: 627.0 μs
- **Rounds**: 638

#### Powsybl Cgmes Export Realgrid

- **Mean**: 2.11 s
- **Min**: 2.04 s
- **Max**: 2.27 s
- **Rounds**: 5

### powsybl_cgmes (Svedala)

#### Powsybl Cgmes Load Svedala

- **Mean**: 245.4 ms
- **Min**: 224.4 ms
- **Max**: 285.9 ms
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 142.0 μs
- **Min**: 56.2 μs
- **Max**: 1.6 ms
- **Rounds**: 1491

#### Powsybl Cgmes Get Generators

- **Mean**: 53.2 μs
- **Min**: 39.7 μs
- **Max**: 447.1 μs
- **Rounds**: 4434

#### Powsybl Cgmes Get Loads

- **Mean**: 149.0 μs
- **Min**: 119.4 μs
- **Max**: 350.5 μs
- **Rounds**: 854

#### Powsybl Cgmes Get Substations

- **Mean**: 50.6 μs
- **Min**: 39.9 μs
- **Max**: 336.7 μs
- **Rounds**: 2878

#### Powsybl Cgmes Export Svedala

- **Mean**: 188.4 ms
- **Min**: 165.7 ms
- **Max**: 251.7 ms
- **Rounds**: 5

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.32 s
- **Min**: 4.22 s
- **Max**: 4.44 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 36.4 ms
- **Min**: 33.0 ms
- **Max**: 44.5 ms
- **Rounds**: 31

#### Pypowsybl Get Generators

- **Mean**: 2.7 ms
- **Min**: 2.2 ms
- **Max**: 17.2 ms
- **Rounds**: 223

#### Pypowsybl Get Loads

- **Mean**: 21.3 ms
- **Min**: 17.7 ms
- **Max**: 33.8 ms
- **Rounds**: 53

#### Pypowsybl Get Substations

- **Mean**: 4.5 ms
- **Min**: 3.3 ms
- **Max**: 11.6 ms
- **Rounds**: 122

#### Pypowsybl Export Realgrid

- **Mean**: 1.59 s
- **Min**: 1.57 s
- **Max**: 1.62 s
- **Rounds**: 5

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 419.7 ms
- **Min**: 401.7 ms
- **Max**: 437.0 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 284.8 μs
- **Min**: 271.5 μs
- **Max**: 503.0 μs
- **Rounds**: 1162

#### Pypowsybl Get Generators

- **Mean**: 266.9 μs
- **Min**: 247.7 μs
- **Max**: 1.5 ms
- **Rounds**: 1603

#### Pypowsybl Get Loads

- **Mean**: 189.8 μs
- **Min**: 178.4 μs
- **Max**: 558.3 μs
- **Rounds**: 1773

#### Pypowsybl Get Substations

- **Mean**: 121.9 μs
- **Min**: 112.2 μs
- **Max**: 969.5 μs
- **Rounds**: 3562

#### Pypowsybl Export Svedala

- **Mean**: 139.0 ms
- **Min**: 136.1 ms
- **Max**: 143.2 ms
- **Rounds**: 8

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 19.42 s
- **Min**: 18.88 s
- **Max**: 20.08 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 1.2 ms
- **Min**: 1.2 ms
- **Max**: 1.9 ms
- **Rounds**: 381

#### Rdflib Get Generators

- **Mean**: 442.2 μs
- **Min**: 422.6 μs
- **Max**: 525.6 μs
- **Rounds**: 1178

#### Rdflib Get Loads

- **Mean**: 2.3 ms
- **Min**: 2.1 ms
- **Max**: 3.6 ms
- **Rounds**: 279

#### Rdflib Get Substations

- **Mean**: 770.4 μs
- **Min**: 734.0 μs
- **Max**: 1.5 ms
- **Rounds**: 775

#### Rdflib Export Realgrid

- **Mean**: 18.69 s
- **Min**: 18.55 s
- **Max**: 19.08 s
- **Rounds**: 5

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 1.64 s
- **Min**: 1.63 s
- **Max**: 1.65 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 57.3 μs
- **Min**: 51.6 μs
- **Max**: 141.8 μs
- **Rounds**: 4996

#### Rdflib Get Generators

- **Mean**: 51.3 μs
- **Min**: 47.7 μs
- **Max**: 517.2 μs
- **Rounds**: 8257

#### Rdflib Get Loads

- **Mean**: 140.9 μs
- **Min**: 134.0 μs
- **Max**: 361.1 μs
- **Rounds**: 4316

#### Rdflib Get Substations

- **Mean**: 49.3 μs
- **Min**: 44.8 μs
- **Max**: 464.6 μs
- **Rounds**: 9325

#### Rdflib Export Svedala

- **Mean**: 1.60 s
- **Min**: 1.58 s
- **Max**: 1.64 s
- **Rounds**: 5

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.36 s
- **Min**: 1.22 s
- **Max**: 1.43 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 306.5 ms
- **Min**: 304.2 ms
- **Max**: 308.9 ms
- **Rounds**: 5

#### Triplets Get Generators

- **Mean**: 268.8 ms
- **Min**: 265.7 ms
- **Max**: 273.2 ms
- **Rounds**: 5

#### Triplets Get Loads

- **Mean**: 625.7 ms
- **Min**: 615.9 ms
- **Max**: 640.1 ms
- **Rounds**: 5

#### Triplets Get Substations

- **Mean**: 254.6 ms
- **Min**: 250.6 ms
- **Max**: 263.8 ms
- **Rounds**: 5

#### Triplets Export Realgrid

- **Mean**: 5.78 s
- **Min**: 5.69 s
- **Max**: 5.91 s
- **Rounds**: 5

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 118.0 ms
- **Min**: 102.1 ms
- **Max**: 124.3 ms
- **Rounds**: 11

#### Triplets Get Lines

- **Mean**: 21.2 ms
- **Min**: 20.3 ms
- **Max**: 25.7 ms
- **Rounds**: 47

#### Triplets Get Generators

- **Mean**: 21.4 ms
- **Min**: 20.8 ms
- **Max**: 23.2 ms
- **Rounds**: 41

#### Triplets Get Loads

- **Mean**: 42.7 ms
- **Min**: 40.7 ms
- **Max**: 46.8 ms
- **Rounds**: 22

#### Triplets Get Substations

- **Mean**: 21.0 ms
- **Min**: 19.8 ms
- **Max**: 25.5 ms
- **Rounds**: 46

#### Triplets Export Svedala

- **Mean**: 607.4 ms
- **Min**: 580.8 ms
- **Max**: 623.8 ms
- **Rounds**: 5

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 6.90 s
- **Min**: 5.74 s
- **Max**: 7.29 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 96628

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.7 μs
- **Rounds**: 86274

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 8.2 μs
- **Rounds**: 167196

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 5.2 μs
- **Rounds**: 176026

#### Veragrid Export Realgrid

- **Mean**: 12.55 s
- **Min**: 8.96 s
- **Max**: 17.41 s
- **Rounds**: 5

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 470.4 ms
- **Min**: 416.8 ms
- **Max**: 525.7 ms
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 105619

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.7 μs
- **Rounds**: 88567

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 12.6 μs
- **Rounds**: 157679

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.5 μs
- **Rounds**: 88410

#### Veragrid Export Svedala

- **Mean**: 1.08 s
- **Min**: 918.0 ms
- **Max**: 1.24 s
- **Rounds**: 5
