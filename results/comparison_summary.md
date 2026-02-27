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
| cimgraph (Realgrid) | 12.46 s | 1478.5 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| cimgraph (Svedala) | 449.7 ms | 92.3 MB | 97 lines, 39 gen, 0 loads | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.62 s | 3340.1 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 460.0 ms | 921.9 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| rdflib (Realgrid) | 15.25 s | 806.2 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| rdflib (Svedala) | 856.4 ms | 100.7 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.48 s | 513.6 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| triplets (Svedala) | 130.2 ms | 61.6 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| veragrid (Realgrid) | 17.06 s | 2689.8 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| veragrid (Svedala) | 1.43 s | 603.5 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.0 μs | 4.2 ms | 367.9 μs | 275.6 μs | 45.8 μs | 14.5 ms | 1.8 ms | 0.0 μs | 0.0 μs |
| get_lines | 0.1 μs | 0.0 μs | 45.1 ms | 350.8 μs | 1.5 ms | 53.4 μs | 15.4 ms | 1.9 ms | 0.0 μs | 0.0 μs |
| get_loads | 0.2 μs | 0.2 μs | 24.4 ms | 238.5 μs | 1.2 ms | 129.8 μs | 44.1 ms | 5.6 ms | 0.1 μs | 0.1 μs |
| get_substations | 0.1 μs | 0.1 μs | 5.9 ms | 167.6 μs | 867.1 μs | 47.5 μs | 14.4 ms | 1.8 ms | 0.0 μs | 0.0 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 12.46 s
- **Min**: 11.50 s
- **Max**: 13.29 s
- **Rounds**: 3

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 4.7 μs
- **Rounds**: 162549

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 88402

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.1 μs
- **Max**: 27.0 μs
- **Rounds**: 152370

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.5 μs
- **Rounds**: 95329

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 449.7 ms
- **Min**: 408.9 ms
- **Max**: 485.9 ms
- **Rounds**: 3

#### Cimgraph Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.9 μs
- **Rounds**: 191939

#### Cimgraph Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.2 μs
- **Rounds**: 103972

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.1 μs
- **Max**: 5.6 μs
- **Rounds**: 137287

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 0.3 μs
- **Rounds**: 104516

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.62 s
- **Min**: 4.56 s
- **Max**: 4.72 s
- **Rounds**: 3

#### Pypowsybl Get Lines

- **Mean**: 45.1 ms
- **Min**: 37.1 ms
- **Max**: 58.0 ms
- **Rounds**: 24

#### Pypowsybl Get Generators

- **Mean**: 4.2 ms
- **Min**: 2.7 ms
- **Max**: 8.1 ms
- **Rounds**: 143

#### Pypowsybl Get Loads

- **Mean**: 24.4 ms
- **Min**: 18.2 ms
- **Max**: 83.2 ms
- **Rounds**: 37

#### Pypowsybl Get Substations

- **Mean**: 5.9 ms
- **Min**: 3.9 ms
- **Max**: 12.2 ms
- **Rounds**: 123

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 460.0 ms
- **Min**: 444.0 ms
- **Max**: 482.3 ms
- **Rounds**: 3

#### Pypowsybl Get Lines

- **Mean**: 350.8 μs
- **Min**: 310.8 μs
- **Max**: 2.2 ms
- **Rounds**: 1020

#### Pypowsybl Get Generators

- **Mean**: 367.9 μs
- **Min**: 300.4 μs
- **Max**: 3.4 ms
- **Rounds**: 1581

#### Pypowsybl Get Loads

- **Mean**: 238.5 μs
- **Min**: 211.6 μs
- **Max**: 1.2 ms
- **Rounds**: 2102

#### Pypowsybl Get Substations

- **Mean**: 167.6 μs
- **Min**: 153.4 μs
- **Max**: 598.8 μs
- **Rounds**: 2742

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 15.25 s
- **Min**: 14.85 s
- **Max**: 15.80 s
- **Rounds**: 3

#### Rdflib Get Lines

- **Mean**: 1.5 ms
- **Min**: 1.2 ms
- **Max**: 4.2 ms
- **Rounds**: 330

#### Rdflib Get Generators

- **Mean**: 275.6 μs
- **Min**: 241.6 μs
- **Max**: 1.6 ms
- **Rounds**: 1761

#### Rdflib Get Loads

- **Mean**: 1.2 ms
- **Min**: 1.1 ms
- **Max**: 2.2 ms
- **Rounds**: 403

#### Rdflib Get Substations

- **Mean**: 867.1 μs
- **Min**: 718.4 μs
- **Max**: 2.8 ms
- **Rounds**: 784

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 856.4 ms
- **Min**: 841.1 ms
- **Max**: 872.8 ms
- **Rounds**: 3

#### Rdflib Get Lines

- **Mean**: 53.4 μs
- **Min**: 50.9 μs
- **Max**: 184.4 μs
- **Rounds**: 3695

#### Rdflib Get Generators

- **Mean**: 45.8 μs
- **Min**: 40.8 μs
- **Max**: 173.6 μs
- **Rounds**: 9122

#### Rdflib Get Loads

- **Mean**: 129.8 μs
- **Min**: 120.6 μs
- **Max**: 387.3 μs
- **Rounds**: 4619

#### Rdflib Get Substations

- **Mean**: 47.5 μs
- **Min**: 42.4 μs
- **Max**: 146.2 μs
- **Rounds**: 8624

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.48 s
- **Min**: 1.48 s
- **Max**: 1.49 s
- **Rounds**: 3

#### Triplets Get Lines

- **Mean**: 15.4 ms
- **Min**: 14.1 ms
- **Max**: 19.5 ms
- **Rounds**: 64

#### Triplets Get Generators

- **Mean**: 14.5 ms
- **Min**: 13.5 ms
- **Max**: 16.5 ms
- **Rounds**: 72

#### Triplets Get Loads

- **Mean**: 44.1 ms
- **Min**: 42.3 ms
- **Max**: 47.1 ms
- **Rounds**: 23

#### Triplets Get Substations

- **Mean**: 14.4 ms
- **Min**: 13.9 ms
- **Max**: 17.5 ms
- **Rounds**: 71

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 130.2 ms
- **Min**: 124.3 ms
- **Max**: 150.8 ms
- **Rounds**: 8

#### Triplets Get Lines

- **Mean**: 1.9 ms
- **Min**: 1.6 ms
- **Max**: 4.6 ms
- **Rounds**: 345

#### Triplets Get Generators

- **Mean**: 1.8 ms
- **Min**: 1.7 ms
- **Max**: 3.5 ms
- **Rounds**: 486

#### Triplets Get Loads

- **Mean**: 5.6 ms
- **Min**: 4.8 ms
- **Max**: 8.9 ms
- **Rounds**: 173

#### Triplets Get Substations

- **Mean**: 1.8 ms
- **Min**: 1.7 ms
- **Max**: 3.6 ms
- **Rounds**: 514

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 17.06 s
- **Min**: 16.02 s
- **Max**: 17.77 s
- **Rounds**: 3

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.2 μs
- **Rounds**: 101021

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.3 μs
- **Rounds**: 101647

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.4 μs
- **Rounds**: 59447

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 3.6 μs
- **Rounds**: 103757

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 1.43 s
- **Min**: 1.15 s
- **Max**: 1.70 s
- **Rounds**: 3

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 1.0 μs
- **Rounds**: 198021

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 91989

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 7.3 μs
- **Rounds**: 156446

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.3 μs
- **Rounds**: 126823
