# Benchmark Comparison Report

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.3
- **System**: Linux 6.18.10-200.fc43.x86_64

## Performance Comparison

### Load Performance

| Library | Load Time (mean) | Memory (MB) | Elements | Notes |
|---------|------------------|-------------|----------|-------|
| cimgraph (Realgrid) | 12.98 s | 3254.1 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimgraph (Svedala) | 912.0 ms | 191.3 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| jena (Realgrid) | 1.57 s | 3928.2 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| jena (Svedala) | 132.0 ms | 721.1 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| opencgmes (Realgrid) | 1.06 s | 4921.2 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| opencgmes (Svedala) | 90.2 ms | 413.0 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| powsybl_cgmes (Realgrid) | 1.85 s | 4223.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| powsybl_cgmes (Svedala) | 270.2 ms | 679.0 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.61 s | 4496.6 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 475.8 ms | 1160.2 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 19.13 s | 1520.4 MB | 7561 lines, 2694 gen, 13374 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 1.59 s | 285.3 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.45 s | 593.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 131.5 ms | 43.3 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 13.40 s | 2914.4 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 921.0 ms | 664.7 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | jena (Realgrid) | jena (Svedala) | opencgmes (Realgrid) | opencgmes (Svedala) | powsybl_cgmes (Realgrid) | powsybl_cgmes (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.1 μs | 382.1 μs | 112.6 μs | 324.9 μs | 136.7 μs | 220.5 μs | 62.0 μs | 2.8 ms | 285.9 μs | 419.7 μs | 50.7 μs | 278.2 ms | 25.9 ms | 0.1 μs | 0.1 μs |
| get_lines | 0.1 μs | 0.1 μs | 1.9 ms | 339.6 μs | 1.9 ms | 455.7 μs | 1.2 ms | 149.7 μs | 33.1 ms | 299.3 μs | 1.2 ms | 52.5 μs | 339.3 ms | 24.8 ms | 0.0 μs | 0.0 μs |
| get_loads | 0.2 μs | 0.2 μs | 1.2 ms | 365.6 μs | 1.2 ms | 273.0 μs | 1.1 ms | 159.4 μs | 20.2 ms | 215.8 μs | 2.1 ms | 138.1 μs | 655.3 ms | 54.9 ms | 0.1 μs | 0.1 μs |
| get_substations | 0.1 μs | 0.1 μs | 635.2 μs | 138.5 μs | 378.9 μs | 141.0 μs | 339.0 μs | 67.0 μs | 3.9 ms | 132.0 μs | 730.7 μs | 47.8 μs | 263.9 ms | 24.2 ms | 0.1 μs | 0.1 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 12.98 s
- **Min**: 11.89 s
- **Max**: 14.32 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 57.3 μs
- **Rounds**: 142389

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 53.4 μs
- **Rounds**: 157679

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.1 μs
- **Max**: 9.2 μs
- **Rounds**: 191571

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 100.2 μs
- **Rounds**: 173281

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 912.0 ms
- **Min**: 847.0 ms
- **Max**: 1.03 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 14.5 μs
- **Rounds**: 191571

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.7 μs
- **Rounds**: 74544

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 105.8 μs
- **Rounds**: 104069

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.6 μs
- **Rounds**: 69701

### jena (Realgrid)

#### Jena Load Realgrid

- **Mean**: 1.57 s
- **Min**: 1.51 s
- **Max**: 1.63 s
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 1.9 ms
- **Min**: 903.4 μs
- **Max**: 60.7 ms
- **Rounds**: 182

#### Jena Get Generators

- **Mean**: 382.1 μs
- **Min**: 222.7 μs
- **Max**: 39.2 ms
- **Rounds**: 1036

#### Jena Get Loads

- **Mean**: 1.2 ms
- **Min**: 969.4 μs
- **Max**: 3.6 ms
- **Rounds**: 337

#### Jena Get Substations

- **Mean**: 635.2 μs
- **Min**: 563.0 μs
- **Max**: 2.3 ms
- **Rounds**: 692

### jena (Svedala)

#### Jena Load Svedala

- **Mean**: 132.0 ms
- **Min**: 126.9 ms
- **Max**: 141.7 ms
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 339.6 μs
- **Min**: 175.6 μs
- **Max**: 1.5 ms
- **Rounds**: 553

#### Jena Get Generators

- **Mean**: 112.6 μs
- **Min**: 71.5 μs
- **Max**: 963.4 μs
- **Rounds**: 2783

#### Jena Get Loads

- **Mean**: 365.6 μs
- **Min**: 196.1 μs
- **Max**: 64.8 ms
- **Rounds**: 1643

#### Jena Get Substations

- **Mean**: 138.5 μs
- **Min**: 49.8 μs
- **Max**: 155.1 ms
- **Rounds**: 3553

### opencgmes (Realgrid)

#### Opencgmes Load Realgrid

- **Mean**: 1.06 s
- **Min**: 983.2 ms
- **Max**: 1.18 s
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 1.9 ms
- **Min**: 1.3 ms
- **Max**: 37.8 ms
- **Rounds**: 127

#### Opencgmes Get Generators

- **Mean**: 324.9 μs
- **Min**: 165.6 μs
- **Max**: 1.8 ms
- **Rounds**: 813

#### Opencgmes Get Loads

- **Mean**: 1.2 ms
- **Min**: 654.9 μs
- **Max**: 82.1 ms
- **Rounds**: 478

#### Opencgmes Get Substations

- **Mean**: 378.9 μs
- **Min**: 313.9 μs
- **Max**: 9.9 ms
- **Rounds**: 1112

### opencgmes (Svedala)

#### Opencgmes Load Svedala

- **Mean**: 90.2 ms
- **Min**: 68.0 ms
- **Max**: 126.2 ms
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 455.7 μs
- **Min**: 162.8 μs
- **Max**: 4.1 ms
- **Rounds**: 624

#### Opencgmes Get Generators

- **Mean**: 136.7 μs
- **Min**: 72.7 μs
- **Max**: 15.5 ms
- **Rounds**: 1687

#### Opencgmes Get Loads

- **Mean**: 273.0 μs
- **Min**: 196.1 μs
- **Max**: 1.7 ms
- **Rounds**: 860

#### Opencgmes Get Substations

- **Mean**: 141.0 μs
- **Min**: 52.1 μs
- **Max**: 105.7 ms
- **Rounds**: 6046

### powsybl_cgmes (Realgrid)

#### Powsybl Cgmes Load Realgrid

- **Mean**: 1.85 s
- **Min**: 1.81 s
- **Max**: 1.93 s
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 1.2 ms
- **Min**: 651.6 μs
- **Max**: 3.4 ms
- **Rounds**: 281

#### Powsybl Cgmes Get Generators

- **Mean**: 220.5 μs
- **Min**: 158.9 μs
- **Max**: 1.3 ms
- **Rounds**: 1190

#### Powsybl Cgmes Get Loads

- **Mean**: 1.1 ms
- **Min**: 872.5 μs
- **Max**: 5.3 ms
- **Rounds**: 266

#### Powsybl Cgmes Get Substations

- **Mean**: 339.0 μs
- **Min**: 299.0 μs
- **Max**: 631.9 μs
- **Rounds**: 651

### powsybl_cgmes (Svedala)

#### Powsybl Cgmes Load Svedala

- **Mean**: 270.2 ms
- **Min**: 239.6 ms
- **Max**: 303.4 ms
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 149.7 μs
- **Min**: 57.7 μs
- **Max**: 843.8 μs
- **Rounds**: 1297

#### Powsybl Cgmes Get Generators

- **Mean**: 62.0 μs
- **Min**: 40.8 μs
- **Max**: 894.8 μs
- **Rounds**: 4621

#### Powsybl Cgmes Get Loads

- **Mean**: 159.4 μs
- **Min**: 106.4 μs
- **Max**: 1.0 ms
- **Rounds**: 706

#### Powsybl Cgmes Get Substations

- **Mean**: 67.0 μs
- **Min**: 34.6 μs
- **Max**: 51.7 ms
- **Rounds**: 5831

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.61 s
- **Min**: 4.46 s
- **Max**: 4.71 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 33.1 ms
- **Min**: 32.0 ms
- **Max**: 36.7 ms
- **Rounds**: 29

#### Pypowsybl Get Generators

- **Mean**: 2.8 ms
- **Min**: 2.3 ms
- **Max**: 22.3 ms
- **Rounds**: 213

#### Pypowsybl Get Loads

- **Mean**: 20.2 ms
- **Min**: 18.4 ms
- **Max**: 30.8 ms
- **Rounds**: 44

#### Pypowsybl Get Substations

- **Mean**: 3.9 ms
- **Min**: 3.3 ms
- **Max**: 15.0 ms
- **Rounds**: 148

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 475.8 ms
- **Min**: 439.5 ms
- **Max**: 503.4 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 299.3 μs
- **Min**: 277.7 μs
- **Max**: 640.9 μs
- **Rounds**: 1020

#### Pypowsybl Get Generators

- **Mean**: 285.9 μs
- **Min**: 262.3 μs
- **Max**: 736.7 μs
- **Rounds**: 1778

#### Pypowsybl Get Loads

- **Mean**: 215.8 μs
- **Min**: 184.9 μs
- **Max**: 24.6 ms
- **Rounds**: 2315

#### Pypowsybl Get Substations

- **Mean**: 132.0 μs
- **Min**: 118.0 μs
- **Max**: 780.5 μs
- **Rounds**: 3192

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 19.13 s
- **Min**: 18.97 s
- **Max**: 19.31 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 1.2 ms
- **Min**: 1.1 ms
- **Max**: 1.6 ms
- **Rounds**: 389

#### Rdflib Get Generators

- **Mean**: 419.7 μs
- **Min**: 409.2 μs
- **Max**: 683.6 μs
- **Rounds**: 1280

#### Rdflib Get Loads

- **Mean**: 2.1 ms
- **Min**: 2.0 ms
- **Max**: 3.2 ms
- **Rounds**: 277

#### Rdflib Get Substations

- **Mean**: 730.7 μs
- **Min**: 708.9 μs
- **Max**: 1.2 ms
- **Rounds**: 811

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 1.59 s
- **Min**: 1.58 s
- **Max**: 1.61 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 52.5 μs
- **Min**: 49.8 μs
- **Max**: 135.2 μs
- **Rounds**: 5221

#### Rdflib Get Generators

- **Mean**: 50.7 μs
- **Min**: 47.4 μs
- **Max**: 215.3 μs
- **Rounds**: 8388

#### Rdflib Get Loads

- **Mean**: 138.1 μs
- **Min**: 130.5 μs
- **Max**: 343.5 μs
- **Rounds**: 4503

#### Rdflib Get Substations

- **Mean**: 47.8 μs
- **Min**: 44.4 μs
- **Max**: 398.3 μs
- **Rounds**: 7615

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.45 s
- **Min**: 1.31 s
- **Max**: 1.53 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 339.3 ms
- **Min**: 326.6 ms
- **Max**: 354.8 ms
- **Rounds**: 5

#### Triplets Get Generators

- **Mean**: 278.2 ms
- **Min**: 276.4 ms
- **Max**: 280.5 ms
- **Rounds**: 5

#### Triplets Get Loads

- **Mean**: 655.3 ms
- **Min**: 647.8 ms
- **Max**: 668.3 ms
- **Rounds**: 5

#### Triplets Get Substations

- **Mean**: 263.9 ms
- **Min**: 258.7 ms
- **Max**: 271.3 ms
- **Rounds**: 5

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 131.5 ms
- **Min**: 117.5 ms
- **Max**: 138.6 ms
- **Rounds**: 9

#### Triplets Get Lines

- **Mean**: 24.8 ms
- **Min**: 21.7 ms
- **Max**: 28.3 ms
- **Rounds**: 33

#### Triplets Get Generators

- **Mean**: 25.9 ms
- **Min**: 22.8 ms
- **Max**: 32.5 ms
- **Rounds**: 35

#### Triplets Get Loads

- **Mean**: 54.9 ms
- **Min**: 47.1 ms
- **Max**: 65.3 ms
- **Rounds**: 17

#### Triplets Get Substations

- **Mean**: 24.2 ms
- **Min**: 20.9 ms
- **Max**: 28.0 ms
- **Rounds**: 38

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 13.40 s
- **Min**: 8.18 s
- **Max**: 20.75 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 112397

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.2 μs
- **Rounds**: 94788

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 5.1 μs
- **Rounds**: 174795

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 95512

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 921.0 ms
- **Min**: 646.6 ms
- **Max**: 1.15 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.8 μs
- **Rounds**: 112778

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 90417

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 9.1 μs
- **Rounds**: 199602

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.8 μs
- **Rounds**: 198021
