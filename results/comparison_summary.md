# Benchmark Comparison Report

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Performance Comparison

### Load Performance

| Library | Load Time (mean) | Memory (MB) | Elements | Notes |
|---------|------------------|-------------|----------|-------|
| cimgraph (Realgrid) | 14.69 s | 1832.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimgraph (Svedala) | 514.3 ms | 94.7 MB | 97 lines, 39 gen, 0 loads, 56 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.88 s | 1266.1 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 498.3 ms | 895.1 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 17.23 s | 854.3 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 952.9 ms | 110.1 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.60 s | 515.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 136.9 ms | 60.6 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 18.26 s | 2690.4 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 1.61 s | 612.2 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.1 μs | 3.3 ms | 408.9 μs | 285.6 μs | 49.4 μs | 19.4 ms | 2.1 ms | 0.0 μs | 0.0 μs |
| get_lines | 0.1 μs | 0.1 μs | 39.3 ms | 409.9 μs | 1.7 ms | 58.6 μs | 19.9 ms | 2.1 ms | 0.0 μs | 0.0 μs |
| get_loads | 0.2 μs | 0.2 μs | 20.7 ms | 294.5 μs | 1.4 ms | 140.3 μs | 55.2 ms | 6.3 ms | 0.1 μs | 0.1 μs |
| get_substations | 0.1 μs | 0.1 μs | 5.7 ms | 215.8 μs | 928.3 μs | 52.0 μs | 19.0 ms | 2.1 ms | 0.0 μs | 0.0 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 14.69 s
- **Min**: 12.57 s
- **Max**: 16.96 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.0 μs
- **Rounds**: 73497

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.7 μs
- **Rounds**: 74600

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 9.9 μs
- **Rounds**: 94429

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.3 μs
- **Rounds**: 87245

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 514.3 ms
- **Min**: 453.3 ms
- **Max**: 552.8 ms
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.7 μs
- **Rounds**: 84589

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 7.5 μs
- **Rounds**: 170039

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.1 μs
- **Max**: 8.5 μs
- **Rounds**: 81613

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 3.5 μs
- **Rounds**: 87093

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.88 s
- **Min**: 4.81 s
- **Max**: 4.98 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 39.3 ms
- **Min**: 35.8 ms
- **Max**: 56.6 ms
- **Rounds**: 27

#### Pypowsybl Get Generators

- **Mean**: 3.3 ms
- **Min**: 2.8 ms
- **Max**: 9.1 ms
- **Rounds**: 199

#### Pypowsybl Get Loads

- **Mean**: 20.7 ms
- **Min**: 18.7 ms
- **Max**: 33.3 ms
- **Rounds**: 47

#### Pypowsybl Get Substations

- **Mean**: 5.7 ms
- **Min**: 4.5 ms
- **Max**: 15.8 ms
- **Rounds**: 137

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 498.3 ms
- **Min**: 472.2 ms
- **Max**: 520.3 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 409.9 μs
- **Min**: 383.2 μs
- **Max**: 746.7 μs
- **Rounds**: 769

#### Pypowsybl Get Generators

- **Mean**: 408.9 μs
- **Min**: 361.5 μs
- **Max**: 3.0 ms
- **Rounds**: 1201

#### Pypowsybl Get Loads

- **Mean**: 294.5 μs
- **Min**: 263.9 μs
- **Max**: 1.7 ms
- **Rounds**: 1560

#### Pypowsybl Get Substations

- **Mean**: 215.8 μs
- **Min**: 185.6 μs
- **Max**: 912.4 μs
- **Rounds**: 2637

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 17.23 s
- **Min**: 16.80 s
- **Max**: 17.82 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 1.7 ms
- **Min**: 1.3 ms
- **Max**: 8.4 ms
- **Rounds**: 210

#### Rdflib Get Generators

- **Mean**: 285.6 μs
- **Min**: 264.1 μs
- **Max**: 555.2 μs
- **Rounds**: 1349

#### Rdflib Get Loads

- **Mean**: 1.4 ms
- **Min**: 1.2 ms
- **Max**: 2.2 ms
- **Rounds**: 339

#### Rdflib Get Substations

- **Mean**: 928.3 μs
- **Min**: 836.2 μs
- **Max**: 3.5 ms
- **Rounds**: 631

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 952.9 ms
- **Min**: 898.6 ms
- **Max**: 1.02 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 58.6 μs
- **Min**: 55.7 μs
- **Max**: 328.5 μs
- **Rounds**: 4007

#### Rdflib Get Generators

- **Mean**: 49.4 μs
- **Min**: 46.7 μs
- **Max**: 375.7 μs
- **Rounds**: 8729

#### Rdflib Get Loads

- **Mean**: 140.3 μs
- **Min**: 133.9 μs
- **Max**: 737.3 μs
- **Rounds**: 3950

#### Rdflib Get Substations

- **Mean**: 52.0 μs
- **Min**: 49.5 μs
- **Max**: 176.4 μs
- **Rounds**: 7781

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.60 s
- **Min**: 1.58 s
- **Max**: 1.62 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 19.9 ms
- **Min**: 16.3 ms
- **Max**: 24.4 ms
- **Rounds**: 54

#### Triplets Get Generators

- **Mean**: 19.4 ms
- **Min**: 16.0 ms
- **Max**: 26.2 ms
- **Rounds**: 47

#### Triplets Get Loads

- **Mean**: 55.2 ms
- **Min**: 52.9 ms
- **Max**: 56.5 ms
- **Rounds**: 21

#### Triplets Get Substations

- **Mean**: 19.0 ms
- **Min**: 15.0 ms
- **Max**: 28.8 ms
- **Rounds**: 54

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 136.9 ms
- **Min**: 131.4 ms
- **Max**: 159.7 ms
- **Rounds**: 8

#### Triplets Get Lines

- **Mean**: 2.1 ms
- **Min**: 1.9 ms
- **Max**: 5.1 ms
- **Rounds**: 350

#### Triplets Get Generators

- **Mean**: 2.1 ms
- **Min**: 1.9 ms
- **Max**: 3.6 ms
- **Rounds**: 431

#### Triplets Get Loads

- **Mean**: 6.3 ms
- **Min**: 5.6 ms
- **Max**: 10.8 ms
- **Rounds**: 160

#### Triplets Get Substations

- **Mean**: 2.1 ms
- **Min**: 1.9 ms
- **Max**: 3.4 ms
- **Rounds**: 455

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 18.26 s
- **Min**: 16.53 s
- **Max**: 20.35 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.5 μs
- **Rounds**: 99612

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 100624

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 20.8 μs
- **Rounds**: 148965

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 99811

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 1.61 s
- **Min**: 1.25 s
- **Max**: 1.88 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.4 μs
- **Rounds**: 196502

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.3 μs
- **Rounds**: 118695

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 9.4 μs
- **Rounds**: 161760

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.3 μs
- **Rounds**: 116050
