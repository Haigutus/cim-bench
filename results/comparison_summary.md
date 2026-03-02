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
| cimgraph (Realgrid) | 17.94 s | 2857.8 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimgraph (Svedala) | 1.34 s | 249.3 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.51 s | 4754.8 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 447.2 ms | 1157.2 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 19.13 s | 1095.7 MB | 7561 lines, 2694 gen, 13374 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 1.62 s | 228.4 MB | 97 lines, 78 gen, 146 loads, 57 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.41 s | 515.6 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 116.9 ms | 58.5 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 19.88 s | 1890.3 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 1.42 s | 551.9 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.1 μs | 3.4 ms | 329.8 μs | 416.8 μs | 50.0 μs | 45.9 ms | 5.3 ms | 0.0 μs | 0.0 μs |
| get_lines | 0.1 μs | 0.1 μs | 38.6 ms | 343.3 μs | 1.1 ms | 53.2 μs | 58.3 ms | 5.6 ms | 0.0 μs | 0.0 μs |
| get_loads | 0.2 μs | 0.2 μs | 19.3 ms | 233.0 μs | 2.0 ms | 135.5 μs | 64.9 ms | 6.5 ms | 0.1 μs | 0.1 μs |
| get_substations | 0.1 μs | 0.1 μs | 4.6 ms | 185.2 μs | 748.8 μs | 47.7 μs | 42.6 ms | 4.7 ms | 0.0 μs | 0.0 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 17.94 s
- **Min**: 15.08 s
- **Max**: 20.13 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 9.0 μs
- **Rounds**: 142187

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 17.5 μs
- **Rounds**: 196850

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 27.3 μs
- **Rounds**: 194969

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.5 μs
- **Rounds**: 77979

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 1.34 s
- **Min**: 1.21 s
- **Max**: 1.58 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.4 μs
- **Rounds**: 87627

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.5 μs
- **Rounds**: 85529

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 20.1 μs
- **Rounds**: 156691

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.6 μs
- **Rounds**: 83383

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.51 s
- **Min**: 4.44 s
- **Max**: 4.62 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 38.6 ms
- **Min**: 33.7 ms
- **Max**: 54.5 ms
- **Rounds**: 26

#### Pypowsybl Get Generators

- **Mean**: 3.4 ms
- **Min**: 2.6 ms
- **Max**: 9.5 ms
- **Rounds**: 103

#### Pypowsybl Get Loads

- **Mean**: 19.3 ms
- **Min**: 17.4 ms
- **Max**: 22.9 ms
- **Rounds**: 46

#### Pypowsybl Get Substations

- **Mean**: 4.6 ms
- **Min**: 3.7 ms
- **Max**: 20.2 ms
- **Rounds**: 138

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 447.2 ms
- **Min**: 426.0 ms
- **Max**: 466.2 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 343.3 μs
- **Min**: 318.7 μs
- **Max**: 3.1 ms
- **Rounds**: 1065

#### Pypowsybl Get Generators

- **Mean**: 329.8 μs
- **Min**: 302.5 μs
- **Max**: 628.9 μs
- **Rounds**: 1603

#### Pypowsybl Get Loads

- **Mean**: 233.0 μs
- **Min**: 214.7 μs
- **Max**: 464.3 μs
- **Rounds**: 2101

#### Pypowsybl Get Substations

- **Mean**: 185.2 μs
- **Min**: 144.5 μs
- **Max**: 23.9 ms
- **Rounds**: 2786

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 19.13 s
- **Min**: 18.71 s
- **Max**: 19.64 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 1.1 ms
- **Min**: 1.1 ms
- **Max**: 2.6 ms
- **Rounds**: 412

#### Rdflib Get Generators

- **Mean**: 416.8 μs
- **Min**: 404.1 μs
- **Max**: 597.7 μs
- **Rounds**: 921

#### Rdflib Get Loads

- **Mean**: 2.0 ms
- **Min**: 1.9 ms
- **Max**: 3.1 ms
- **Rounds**: 294

#### Rdflib Get Substations

- **Mean**: 748.8 μs
- **Min**: 683.8 μs
- **Max**: 1.8 ms
- **Rounds**: 891

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 1.62 s
- **Min**: 1.60 s
- **Max**: 1.66 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 53.2 μs
- **Min**: 49.3 μs
- **Max**: 242.3 μs
- **Rounds**: 6066

#### Rdflib Get Generators

- **Mean**: 50.0 μs
- **Min**: 47.8 μs
- **Max**: 104.5 μs
- **Rounds**: 8431

#### Rdflib Get Loads

- **Mean**: 135.5 μs
- **Min**: 124.6 μs
- **Max**: 403.0 μs
- **Rounds**: 4440

#### Rdflib Get Substations

- **Mean**: 47.7 μs
- **Min**: 44.8 μs
- **Max**: 132.9 μs
- **Rounds**: 9351

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.41 s
- **Min**: 1.41 s
- **Max**: 1.42 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 58.3 ms
- **Min**: 54.9 ms
- **Max**: 65.9 ms
- **Rounds**: 16

#### Triplets Get Generators

- **Mean**: 45.9 ms
- **Min**: 42.6 ms
- **Max**: 54.9 ms
- **Rounds**: 22

#### Triplets Get Loads

- **Mean**: 64.9 ms
- **Min**: 62.1 ms
- **Max**: 69.8 ms
- **Rounds**: 16

#### Triplets Get Substations

- **Mean**: 42.6 ms
- **Min**: 37.4 ms
- **Max**: 49.1 ms
- **Rounds**: 23

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 116.9 ms
- **Min**: 111.4 ms
- **Max**: 136.6 ms
- **Rounds**: 9

#### Triplets Get Lines

- **Mean**: 5.6 ms
- **Min**: 4.9 ms
- **Max**: 7.0 ms
- **Rounds**: 146

#### Triplets Get Generators

- **Mean**: 5.3 ms
- **Min**: 5.0 ms
- **Max**: 7.5 ms
- **Rounds**: 184

#### Triplets Get Loads

- **Mean**: 6.5 ms
- **Min**: 5.9 ms
- **Max**: 8.7 ms
- **Rounds**: 134

#### Triplets Get Substations

- **Mean**: 4.7 ms
- **Min**: 4.5 ms
- **Max**: 5.6 ms
- **Rounds**: 154

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 19.88 s
- **Min**: 17.87 s
- **Max**: 21.99 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.2 μs
- **Rounds**: 113033

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.2 μs
- **Rounds**: 114456

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 35.0 μs
- **Rounds**: 168607

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.9 μs
- **Rounds**: 196080

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 1.42 s
- **Min**: 1.10 s
- **Max**: 1.66 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.4 μs
- **Rounds**: 196853

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.3 μs
- **Rounds**: 198021

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 6.0 μs
- **Rounds**: 198807

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.2 μs
- **Rounds**: 67715
