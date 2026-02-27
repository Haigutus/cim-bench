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
| cimgraph (Realgrid) | 9.49 s | 2274.9 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| cimgraph (Svedala) | 342.6 ms | 126.9 MB | 97 lines, 39 gen, 0 loads | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.29 s | 4012.8 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 433.8 ms | 1044.7 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| rdflib (Realgrid) | 14.87 s | 930.9 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| rdflib (Svedala) | 813.4 ms | 134.9 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.35 s | 593.9 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| triplets (Svedala) | 123.5 ms | 44.6 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| veragrid (Realgrid) | 10.95 s | 4949.7 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| veragrid (Svedala) | 752.8 ms | 666.3 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.1 μs | 2.6 ms | 264.6 μs | 239.2 μs | 43.8 μs | 64.6 ms | 5.9 ms | 0.1 μs | 0.0 μs |
| get_lines | 0.1 μs | 0.1 μs | 33.2 ms | 296.7 μs | 1.3 ms | 51.3 μs | 64.5 ms | 5.8 ms | 0.0 μs | 0.0 μs |
| get_loads | 0.2 μs | 0.2 μs | 18.8 ms | 189.1 μs | 1.1 ms | 124.4 μs | 193.8 ms | 16.4 ms | 0.1 μs | 0.1 μs |
| get_substations | 0.1 μs | 0.1 μs | 4.1 ms | 119.0 μs | 772.3 μs | 46.3 μs | 64.4 ms | 5.7 ms | 0.1 μs | 0.1 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 9.49 s
- **Min**: 8.83 s
- **Max**: 11.09 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 12.9 μs
- **Rounds**: 172087

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 2.2 μs
- **Rounds**: 95511

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.1 μs
- **Max**: 24.7 μs
- **Rounds**: 89759

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.2 μs
- **Rounds**: 95239

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 342.6 ms
- **Min**: 286.8 ms
- **Max**: 400.9 ms
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.4 μs
- **Rounds**: 98242

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.3 μs
- **Rounds**: 94707

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.1 μs
- **Max**: 5.3 μs
- **Rounds**: 135429

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.5 μs
- **Rounds**: 90736

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.29 s
- **Min**: 4.21 s
- **Max**: 4.42 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 33.2 ms
- **Min**: 32.1 ms
- **Max**: 36.7 ms
- **Rounds**: 29

#### Pypowsybl Get Generators

- **Mean**: 2.6 ms
- **Min**: 2.3 ms
- **Max**: 16.8 ms
- **Rounds**: 216

#### Pypowsybl Get Loads

- **Mean**: 18.8 ms
- **Min**: 17.5 ms
- **Max**: 21.2 ms
- **Rounds**: 48

#### Pypowsybl Get Substations

- **Mean**: 4.1 ms
- **Min**: 3.5 ms
- **Max**: 11.0 ms
- **Rounds**: 148

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 433.8 ms
- **Min**: 405.4 ms
- **Max**: 478.0 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 296.7 μs
- **Min**: 266.0 μs
- **Max**: 19.0 ms
- **Rounds**: 1130

#### Pypowsybl Get Generators

- **Mean**: 264.6 μs
- **Min**: 250.7 μs
- **Max**: 409.7 μs
- **Rounds**: 1843

#### Pypowsybl Get Loads

- **Mean**: 189.1 μs
- **Min**: 178.5 μs
- **Max**: 355.7 μs
- **Rounds**: 2383

#### Pypowsybl Get Substations

- **Mean**: 119.0 μs
- **Min**: 110.9 μs
- **Max**: 301.9 μs
- **Rounds**: 3586

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 14.87 s
- **Min**: 14.66 s
- **Max**: 15.05 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 1.3 ms
- **Min**: 1.2 ms
- **Max**: 2.1 ms
- **Rounds**: 388

#### Rdflib Get Generators

- **Mean**: 239.2 μs
- **Min**: 227.2 μs
- **Max**: 485.9 μs
- **Rounds**: 1785

#### Rdflib Get Loads

- **Mean**: 1.1 ms
- **Min**: 1.1 ms
- **Max**: 2.5 ms
- **Rounds**: 479

#### Rdflib Get Substations

- **Mean**: 772.3 μs
- **Min**: 726.8 μs
- **Max**: 1.8 ms
- **Rounds**: 797

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 813.4 ms
- **Min**: 810.9 ms
- **Max**: 817.5 ms
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 51.3 μs
- **Min**: 49.4 μs
- **Max**: 80.6 μs
- **Rounds**: 5832

#### Rdflib Get Generators

- **Mean**: 43.8 μs
- **Min**: 41.8 μs
- **Max**: 118.8 μs
- **Rounds**: 10006

#### Rdflib Get Loads

- **Mean**: 124.4 μs
- **Min**: 119.1 μs
- **Max**: 526.8 μs
- **Rounds**: 4870

#### Rdflib Get Substations

- **Mean**: 46.3 μs
- **Min**: 43.7 μs
- **Max**: 549.9 μs
- **Rounds**: 8821

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.35 s
- **Min**: 1.22 s
- **Max**: 1.43 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 64.5 ms
- **Min**: 63.7 ms
- **Max**: 65.3 ms
- **Rounds**: 9

#### Triplets Get Generators

- **Mean**: 64.6 ms
- **Min**: 64.0 ms
- **Max**: 65.3 ms
- **Rounds**: 16

#### Triplets Get Loads

- **Mean**: 193.8 ms
- **Min**: 193.0 ms
- **Max**: 195.6 ms
- **Rounds**: 6

#### Triplets Get Substations

- **Mean**: 64.4 ms
- **Min**: 63.2 ms
- **Max**: 65.7 ms
- **Rounds**: 16

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 123.5 ms
- **Min**: 107.1 ms
- **Max**: 139.3 ms
- **Rounds**: 10

#### Triplets Get Lines

- **Mean**: 5.8 ms
- **Min**: 5.1 ms
- **Max**: 7.2 ms
- **Rounds**: 78

#### Triplets Get Generators

- **Mean**: 5.9 ms
- **Min**: 5.1 ms
- **Max**: 8.4 ms
- **Rounds**: 163

#### Triplets Get Loads

- **Mean**: 16.4 ms
- **Min**: 14.9 ms
- **Max**: 22.4 ms
- **Rounds**: 50

#### Triplets Get Substations

- **Mean**: 5.7 ms
- **Min**: 4.9 ms
- **Max**: 9.7 ms
- **Rounds**: 158

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 10.95 s
- **Min**: 7.71 s
- **Max**: 15.33 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.5 μs
- **Rounds**: 122911

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 96815

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.7 μs
- **Rounds**: 57495

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 192344

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 752.8 ms
- **Min**: 504.7 ms
- **Max**: 1.38 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.4 μs
- **Rounds**: 199602

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.4 μs
- **Rounds**: 102052

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 24.3 μs
- **Rounds**: 170912

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.4 μs
- **Rounds**: 199204
