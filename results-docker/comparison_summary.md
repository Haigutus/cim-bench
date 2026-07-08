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
| cimgraph (Realgrid) | 34.65 s | 2608.4 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimgraph (Svedala) | 4.05 s | 179.1 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| jena (Realgrid) | 3.23 s | 3352.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| jena (Svedala) | 343.5 ms | 492.5 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| libcimpp (Realgrid) | 23.95 s | 132.1 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Realgrid) | 4.86 s | 360.1 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| maplib (Svedala) | 663.4 ms | 125.5 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| opencgmes (Realgrid) | 2.50 s | 3891.2 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| opencgmes (Svedala) | 251.0 ms | 275.1 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| powsybl_cgmes (Realgrid) | 3.57 s | 4855.0 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| powsybl_cgmes (Svedala) | 673.3 ms | 612.4 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 11.69 s | 7619.7 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 1.12 s | 989.3 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 50.86 s | 1109.4 MB | 7561 lines, 2694 gen, 13374 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 4.48 s | 208.2 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 505.2 ms | 241.0 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 21.8 ms | 36.5 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 22.71 s | 308.9 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 1.76 s | 74.9 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | jena (Realgrid) | jena (Svedala) | libcimpp (Realgrid) | maplib (Realgrid) | maplib (Svedala) | opencgmes (Realgrid) | opencgmes (Svedala) | powsybl_cgmes (Realgrid) | powsybl_cgmes (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.4 μs | 2.4 ms | 467.3 μs | 7.3 ms | 1.4 ms | 1.1 ms | 2.1 ms | 394.7 μs | 761.0 μs | 245.8 μs | 9.0 ms | 704.9 μs | 928.2 μs | 144.6 μs | 142.7 ms | 21.8 ms | 0.2 μs | 0.3 μs |
| get_lines | 0.1 μs | 0.3 μs | 9.9 ms | 1.1 ms | 8.2 ms | 2.0 ms | 1.1 ms | 13.1 ms | 1.2 ms | 4.1 ms | 562.6 μs | 72.8 ms | 714.6 μs | 2.8 ms | 178.9 μs | 181.0 ms | 21.3 ms | 0.2 μs | 0.3 μs |
| get_loads | 0.2 μs | 0.7 μs | 13.2 ms | 897.0 μs | 19.2 ms | 3.8 ms | 2.6 ms | 9.4 ms | 854.4 μs | 2.8 ms | 718.3 μs | 40.5 ms | 509.4 μs | 5.5 ms | 421.3 μs | 222.8 ms | 35.4 ms | 0.3 μs | 0.3 μs |
| get_substations | 0.1 μs | 0.5 μs | 2.8 ms | 238.7 μs | 8.3 ms | 1.9 ms | 1.3 ms | 2.1 ms | 449.7 μs | 803.0 μs | 154.6 μs | 13.1 ms | 353.5 μs | 1.7 ms | 167.3 μs | 132.6 ms | 20.2 ms | 0.2 μs | 0.3 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 34.65 s
- **Min**: 17.65 s
- **Max**: 55.87 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 19.7 μs
- **Rounds**: 171205

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.0 μs
- **Rounds**: 77610

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 27.7 μs
- **Rounds**: 120701

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 9.0 μs
- **Rounds**: 61767

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 4.05 s
- **Min**: 3.35 s
- **Max**: 4.70 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 47.2 μs
- **Rounds**: 119533

#### Cimgraph Get Generators

- **Mean**: 0.4 μs
- **Min**: 0.2 μs
- **Max**: 53.0 μs
- **Rounds**: 110902

#### Cimgraph Get Loads

- **Mean**: 0.7 μs
- **Min**: 0.4 μs
- **Max**: 18.4 μs
- **Rounds**: 77797

#### Cimgraph Get Substations

- **Mean**: 0.5 μs
- **Min**: 0.2 μs
- **Max**: 47.2 μs
- **Rounds**: 99011

#### Cimgraph Export Svedala

- **Mean**: 2.40 s
- **Min**: 2.16 s
- **Max**: 2.72 s
- **Rounds**: 5

### jena (Realgrid)

#### Jena Load Realgrid

- **Mean**: 3.23 s
- **Min**: 2.90 s
- **Max**: 3.63 s
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 9.9 ms
- **Min**: 5.8 ms
- **Max**: 20.3 ms
- **Rounds**: 50

#### Jena Get Generators

- **Mean**: 2.4 ms
- **Min**: 1.1 ms
- **Max**: 5.7 ms
- **Rounds**: 160

#### Jena Get Loads

- **Mean**: 13.2 ms
- **Min**: 3.8 ms
- **Max**: 136.8 ms
- **Rounds**: 54

#### Jena Get Substations

- **Mean**: 2.8 ms
- **Min**: 1.8 ms
- **Max**: 7.8 ms
- **Rounds**: 172

#### Jena Export Realgrid

- **Mean**: 6.13 s
- **Min**: 4.84 s
- **Max**: 7.55 s
- **Rounds**: 5

### jena (Svedala)

#### Jena Load Svedala

- **Mean**: 343.5 ms
- **Min**: 313.3 ms
- **Max**: 432.1 ms
- **Rounds**: 5

#### Jena Get Lines

- **Mean**: 1.1 ms
- **Min**: 497.0 μs
- **Max**: 3.9 ms
- **Rounds**: 265

#### Jena Get Generators

- **Mean**: 467.3 μs
- **Min**: 186.7 μs
- **Max**: 5.1 ms
- **Rounds**: 1208

#### Jena Get Loads

- **Mean**: 897.0 μs
- **Min**: 385.9 μs
- **Max**: 44.4 ms
- **Rounds**: 905

#### Jena Get Substations

- **Mean**: 238.7 μs
- **Min**: 135.6 μs
- **Max**: 1.0 ms
- **Rounds**: 3000

#### Jena Export Svedala

- **Mean**: 1.40 s
- **Min**: 1.17 s
- **Max**: 1.65 s
- **Rounds**: 5

### libcimpp (Realgrid)

#### Libcimpp Load Realgrid

- **Mean**: 23.95 s
- **Min**: 21.18 s
- **Max**: 28.09 s
- **Rounds**: 5

#### Libcimpp Get Lines

- **Mean**: 8.2 ms
- **Min**: 4.4 ms
- **Max**: 13.4 ms
- **Rounds**: 71

#### Libcimpp Get Generators

- **Mean**: 7.3 ms
- **Min**: 4.5 ms
- **Max**: 12.8 ms
- **Rounds**: 88

#### Libcimpp Get Loads

- **Mean**: 19.2 ms
- **Min**: 16.2 ms
- **Max**: 21.8 ms
- **Rounds**: 60

#### Libcimpp Get Substations

- **Mean**: 8.3 ms
- **Min**: 4.8 ms
- **Max**: 13.5 ms
- **Rounds**: 91

### maplib (Realgrid)

#### Maplib Load Realgrid

- **Mean**: 4.86 s
- **Min**: 4.60 s
- **Max**: 5.47 s
- **Rounds**: 5

#### Maplib Get Lines

- **Mean**: 2.0 ms
- **Min**: 1.3 ms
- **Max**: 4.1 ms
- **Rounds**: 352

#### Maplib Get Generators

- **Mean**: 1.4 ms
- **Min**: 946.6 μs
- **Max**: 4.2 ms
- **Rounds**: 616

#### Maplib Get Loads

- **Mean**: 3.8 ms
- **Min**: 2.3 ms
- **Max**: 14.6 ms
- **Rounds**: 188

#### Maplib Get Substations

- **Mean**: 1.9 ms
- **Min**: 1.1 ms
- **Max**: 5.6 ms
- **Rounds**: 300

#### Maplib Export Realgrid

- **Mean**: 67.61 s
- **Min**: 55.60 s
- **Max**: 74.44 s
- **Rounds**: 5

### maplib (Svedala)

#### Maplib Load Svedala

- **Mean**: 663.4 ms
- **Min**: 598.0 ms
- **Max**: 750.3 ms
- **Rounds**: 5

#### Maplib Get Lines

- **Mean**: 1.1 ms
- **Min**: 649.7 μs
- **Max**: 2.9 ms
- **Rounds**: 587

#### Maplib Get Generators

- **Mean**: 1.1 ms
- **Min**: 638.3 μs
- **Max**: 3.8 ms
- **Rounds**: 801

#### Maplib Get Loads

- **Mean**: 2.6 ms
- **Min**: 1.6 ms
- **Max**: 5.2 ms
- **Rounds**: 241

#### Maplib Get Substations

- **Mean**: 1.3 ms
- **Min**: 788.1 μs
- **Max**: 6.4 ms
- **Rounds**: 973

#### Maplib Export Svedala

- **Mean**: 4.75 s
- **Min**: 4.43 s
- **Max**: 5.20 s
- **Rounds**: 5

### opencgmes (Realgrid)

#### Opencgmes Load Realgrid

- **Mean**: 2.50 s
- **Min**: 2.18 s
- **Max**: 3.03 s
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 13.1 ms
- **Min**: 7.2 ms
- **Max**: 32.3 ms
- **Rounds**: 39

#### Opencgmes Get Generators

- **Mean**: 2.1 ms
- **Min**: 982.4 μs
- **Max**: 6.0 ms
- **Rounds**: 137

#### Opencgmes Get Loads

- **Mean**: 9.4 ms
- **Min**: 3.4 ms
- **Max**: 124.3 ms
- **Rounds**: 80

#### Opencgmes Get Substations

- **Mean**: 2.1 ms
- **Min**: 1.3 ms
- **Max**: 18.4 ms
- **Rounds**: 199

#### Opencgmes Export Realgrid

- **Mean**: 6.56 s
- **Min**: 5.60 s
- **Max**: 7.58 s
- **Rounds**: 5

### opencgmes (Svedala)

#### Opencgmes Load Svedala

- **Mean**: 251.0 ms
- **Min**: 143.3 ms
- **Max**: 472.5 ms
- **Rounds**: 5

#### Opencgmes Get Lines

- **Mean**: 1.2 ms
- **Min**: 538.3 μs
- **Max**: 4.5 ms
- **Rounds**: 213

#### Opencgmes Get Generators

- **Mean**: 394.7 μs
- **Min**: 150.4 μs
- **Max**: 4.6 ms
- **Rounds**: 1444

#### Opencgmes Get Loads

- **Mean**: 854.4 μs
- **Min**: 512.8 μs
- **Max**: 3.6 ms
- **Rounds**: 643

#### Opencgmes Get Substations

- **Mean**: 449.7 μs
- **Min**: 163.1 μs
- **Max**: 164.8 ms
- **Rounds**: 1768

#### Opencgmes Export Svedala

- **Mean**: 842.3 ms
- **Min**: 690.2 ms
- **Max**: 1.01 s
- **Rounds**: 5

### powsybl_cgmes (Realgrid)

#### Powsybl Cgmes Load Realgrid

- **Mean**: 3.57 s
- **Min**: 3.09 s
- **Max**: 3.92 s
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 4.1 ms
- **Min**: 1.8 ms
- **Max**: 193.5 ms
- **Rounds**: 210

#### Powsybl Cgmes Get Generators

- **Mean**: 761.0 μs
- **Min**: 380.6 μs
- **Max**: 3.4 ms
- **Rounds**: 603

#### Powsybl Cgmes Get Loads

- **Mean**: 2.8 ms
- **Min**: 2.0 ms
- **Max**: 7.5 ms
- **Rounds**: 161

#### Powsybl Cgmes Get Substations

- **Mean**: 803.0 μs
- **Min**: 638.7 μs
- **Max**: 1.6 ms
- **Rounds**: 375

#### Powsybl Cgmes Export Realgrid

- **Mean**: 3.94 s
- **Min**: 3.65 s
- **Max**: 4.62 s
- **Rounds**: 5

### powsybl_cgmes (Svedala)

#### Powsybl Cgmes Load Svedala

- **Mean**: 673.3 ms
- **Min**: 606.1 ms
- **Max**: 699.6 ms
- **Rounds**: 5

#### Powsybl Cgmes Get Lines

- **Mean**: 562.6 μs
- **Min**: 127.1 μs
- **Max**: 2.6 ms
- **Rounds**: 861

#### Powsybl Cgmes Get Generators

- **Mean**: 245.8 μs
- **Min**: 141.2 μs
- **Max**: 1.7 ms
- **Rounds**: 799

#### Powsybl Cgmes Get Loads

- **Mean**: 718.3 μs
- **Min**: 293.5 μs
- **Max**: 1.8 ms
- **Rounds**: 603

#### Powsybl Cgmes Get Substations

- **Mean**: 154.6 μs
- **Min**: 93.9 μs
- **Max**: 1.5 ms
- **Rounds**: 2022

#### Powsybl Cgmes Export Svedala

- **Mean**: 398.3 ms
- **Min**: 320.7 ms
- **Max**: 597.5 ms
- **Rounds**: 5

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 11.69 s
- **Min**: 10.92 s
- **Max**: 12.24 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 72.8 ms
- **Min**: 47.0 ms
- **Max**: 90.3 ms
- **Rounds**: 17

#### Pypowsybl Get Generators

- **Mean**: 9.0 ms
- **Min**: 5.4 ms
- **Max**: 16.9 ms
- **Rounds**: 97

#### Pypowsybl Get Loads

- **Mean**: 40.5 ms
- **Min**: 30.2 ms
- **Max**: 52.6 ms
- **Rounds**: 20

#### Pypowsybl Get Substations

- **Mean**: 13.1 ms
- **Min**: 8.4 ms
- **Max**: 20.6 ms
- **Rounds**: 60

#### Pypowsybl Export Realgrid

- **Mean**: 2.65 s
- **Min**: 1.94 s
- **Max**: 4.43 s
- **Rounds**: 5

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 1.12 s
- **Min**: 1.07 s
- **Max**: 1.20 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 714.6 μs
- **Min**: 599.3 μs
- **Max**: 2.0 ms
- **Rounds**: 493

#### Pypowsybl Get Generators

- **Mean**: 704.9 μs
- **Min**: 582.0 μs
- **Max**: 1.6 ms
- **Rounds**: 708

#### Pypowsybl Get Loads

- **Mean**: 509.4 μs
- **Min**: 400.3 μs
- **Max**: 1.3 ms
- **Rounds**: 1161

#### Pypowsybl Get Substations

- **Mean**: 353.5 μs
- **Min**: 254.7 μs
- **Max**: 1.8 ms
- **Rounds**: 1577

#### Pypowsybl Export Svedala

- **Mean**: 456.5 ms
- **Min**: 371.0 ms
- **Max**: 565.0 ms
- **Rounds**: 5

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 50.86 s
- **Min**: 46.09 s
- **Max**: 63.32 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 2.8 ms
- **Min**: 2.3 ms
- **Max**: 6.0 ms
- **Rounds**: 257

#### Rdflib Get Generators

- **Mean**: 928.2 μs
- **Min**: 785.3 μs
- **Max**: 1.8 ms
- **Rounds**: 632

#### Rdflib Get Loads

- **Mean**: 5.5 ms
- **Min**: 4.3 ms
- **Max**: 8.6 ms
- **Rounds**: 135

#### Rdflib Get Substations

- **Mean**: 1.7 ms
- **Min**: 1.4 ms
- **Max**: 3.5 ms
- **Rounds**: 475

#### Rdflib Export Realgrid

- **Mean**: 41.10 s
- **Min**: 39.47 s
- **Max**: 42.56 s
- **Rounds**: 5

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 4.48 s
- **Min**: 4.23 s
- **Max**: 4.86 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 178.9 μs
- **Min**: 134.8 μs
- **Max**: 542.1 μs
- **Rounds**: 1499

#### Rdflib Get Generators

- **Mean**: 144.6 μs
- **Min**: 123.3 μs
- **Max**: 1.3 ms
- **Rounds**: 2953

#### Rdflib Get Loads

- **Mean**: 421.3 μs
- **Min**: 330.2 μs
- **Max**: 1.5 ms
- **Rounds**: 1703

#### Rdflib Get Substations

- **Mean**: 167.3 μs
- **Min**: 122.0 μs
- **Max**: 1.2 ms
- **Rounds**: 2645

#### Rdflib Export Svedala

- **Mean**: 3.36 s
- **Min**: 3.23 s
- **Max**: 3.51 s
- **Rounds**: 5

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 505.2 ms
- **Min**: 452.4 ms
- **Max**: 562.1 ms
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 181.0 ms
- **Min**: 170.0 ms
- **Max**: 190.0 ms
- **Rounds**: 6

#### Triplets Get Generators

- **Mean**: 142.7 ms
- **Min**: 128.9 ms
- **Max**: 153.7 ms
- **Rounds**: 8

#### Triplets Get Loads

- **Mean**: 222.8 ms
- **Min**: 215.2 ms
- **Max**: 235.0 ms
- **Rounds**: 5

#### Triplets Get Substations

- **Mean**: 132.6 ms
- **Min**: 119.6 ms
- **Max**: 140.1 ms
- **Rounds**: 8

#### Triplets Export Realgrid

- **Mean**: 2.49 s
- **Min**: 2.34 s
- **Max**: 2.59 s
- **Rounds**: 5

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 21.8 ms
- **Min**: 16.4 ms
- **Max**: 28.9 ms
- **Rounds**: 15

#### Triplets Get Lines

- **Mean**: 21.3 ms
- **Min**: 15.0 ms
- **Max**: 30.8 ms
- **Rounds**: 37

#### Triplets Get Generators

- **Mean**: 21.8 ms
- **Min**: 15.9 ms
- **Max**: 30.9 ms
- **Rounds**: 59

#### Triplets Get Loads

- **Mean**: 35.4 ms
- **Min**: 27.5 ms
- **Max**: 48.9 ms
- **Rounds**: 29

#### Triplets Get Substations

- **Mean**: 20.2 ms
- **Min**: 14.2 ms
- **Max**: 34.7 ms
- **Rounds**: 41

#### Triplets Export Svedala

- **Mean**: 397.7 ms
- **Min**: 341.9 ms
- **Max**: 465.3 ms
- **Rounds**: 5

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 22.71 s
- **Min**: 18.13 s
- **Max**: 29.02 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 8.1 μs
- **Rounds**: 157432

#### Veragrid Get Generators

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 57.1 μs
- **Rounds**: 155473

#### Veragrid Get Loads

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 178.4 μs
- **Rounds**: 126503

#### Veragrid Get Substations

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 36.5 μs
- **Rounds**: 143823

#### Veragrid Export Realgrid

- **Mean**: 19.94 s
- **Min**: 18.61 s
- **Max**: 22.04 s
- **Rounds**: 5

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 1.76 s
- **Min**: 1.59 s
- **Max**: 1.92 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 61.7 μs
- **Rounds**: 122474

#### Veragrid Get Generators

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 63.4 μs
- **Rounds**: 170328

#### Veragrid Get Loads

- **Mean**: 0.3 μs
- **Min**: 0.3 μs
- **Max**: 11.7 μs
- **Rounds**: 110169

#### Veragrid Get Substations

- **Mean**: 0.3 μs
- **Min**: 0.2 μs
- **Max**: 22.4 μs
- **Rounds**: 88567

#### Veragrid Export Svedala

- **Mean**: 2.90 s
- **Min**: 2.48 s
- **Max**: 3.18 s
- **Rounds**: 5
