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
| cimgraph (Realgrid) | 11.52 s | 2274.2 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| cimgraph (Svedala) | 394.8 ms | 126.9 MB | 97 lines, 39 gen, 0 loads, 56 subs | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.87 s | 1706.3 MB | 7561 lines, 1347 gen, 6687 loads, 4791 subs | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 489.4 ms | 898.9 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| rdflib (Realgrid) | 17.61 s | 930.9 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| rdflib (Svedala) | 961.2 ms | 135.2 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.55 s | 594.4 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| triplets (Svedala) | 138.1 ms | 44.2 MB | 97 lines, 39 gen, 73 loads, 57 subs | Dataset: 7.3 MB |
| veragrid (Realgrid) | 12.20 s | 4785.7 MB | 7561 lines, 1347 gen, 6687 loads, 4875 subs | Dataset: 86.5 MB |
| veragrid (Svedala) | 840.0 ms | 656.9 MB | 97 lines, 39 gen, 73 loads, 56 subs | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|
| get_generators | 0.1 μs | 0.1 μs | 3.9 ms | 328.9 μs | 276.4 μs | 53.0 μs | 64.8 ms | 6.5 ms | 0.1 μs | 0.1 μs |
| get_lines | 0.1 μs | 0.1 μs | 40.5 ms | 345.0 μs | 1.4 ms | 62.4 μs | 67.3 ms | 6.1 ms | 0.0 μs | 0.1 μs |
| get_loads | 0.2 μs | 0.2 μs | 23.1 ms | 225.4 μs | 1.5 ms | 148.8 μs | 196.8 ms | 17.6 ms | 0.2 μs | 0.1 μs |
| get_substations | 0.1 μs | 0.1 μs | 6.5 ms | 146.2 μs | 896.9 μs | 54.9 μs | 66.5 ms | 5.7 ms | 0.1 μs | 0.1 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 11.52 s
- **Min**: 10.93 s
- **Max**: 12.84 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 8.5 μs
- **Rounds**: 198413

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 7.1 μs
- **Rounds**: 192345

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 13.6 μs
- **Rounds**: 100919

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.6 μs
- **Rounds**: 80103

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 394.8 ms
- **Min**: 340.1 ms
- **Max**: 442.4 ms
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.4 μs
- **Rounds**: 82830

#### Cimgraph Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 7.2 μs
- **Rounds**: 199641

#### Cimgraph Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.2 μs
- **Max**: 8.5 μs
- **Rounds**: 95330

#### Cimgraph Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.4 μs
- **Rounds**: 83522

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.87 s
- **Min**: 4.82 s
- **Max**: 4.99 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 40.5 ms
- **Min**: 36.0 ms
- **Max**: 51.0 ms
- **Rounds**: 27

#### Pypowsybl Get Generators

- **Mean**: 3.9 ms
- **Min**: 2.9 ms
- **Max**: 7.4 ms
- **Rounds**: 145

#### Pypowsybl Get Loads

- **Mean**: 23.1 ms
- **Min**: 20.4 ms
- **Max**: 37.0 ms
- **Rounds**: 44

#### Pypowsybl Get Substations

- **Mean**: 6.5 ms
- **Min**: 5.3 ms
- **Max**: 10.2 ms
- **Rounds**: 103

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 489.4 ms
- **Min**: 468.2 ms
- **Max**: 516.0 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 345.0 μs
- **Min**: 319.8 μs
- **Max**: 1.3 ms
- **Rounds**: 1106

#### Pypowsybl Get Generators

- **Mean**: 328.9 μs
- **Min**: 291.2 μs
- **Max**: 23.4 ms
- **Rounds**: 1313

#### Pypowsybl Get Loads

- **Mean**: 225.4 μs
- **Min**: 206.0 μs
- **Max**: 1.2 ms
- **Rounds**: 1737

#### Pypowsybl Get Substations

- **Mean**: 146.2 μs
- **Min**: 129.7 μs
- **Max**: 1.0 ms
- **Rounds**: 2668

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 17.61 s
- **Min**: 17.47 s
- **Max**: 17.82 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 1.4 ms
- **Min**: 1.3 ms
- **Max**: 2.5 ms
- **Rounds**: 328

#### Rdflib Get Generators

- **Mean**: 276.4 μs
- **Min**: 264.1 μs
- **Max**: 417.4 μs
- **Rounds**: 1392

#### Rdflib Get Loads

- **Mean**: 1.5 ms
- **Min**: 1.2 ms
- **Max**: 5.2 ms
- **Rounds**: 243

#### Rdflib Get Substations

- **Mean**: 896.9 μs
- **Min**: 838.5 μs
- **Max**: 2.3 ms
- **Rounds**: 536

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 961.2 ms
- **Min**: 941.7 ms
- **Max**: 991.7 ms
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 62.4 μs
- **Min**: 58.3 μs
- **Max**: 168.0 μs
- **Rounds**: 4068

#### Rdflib Get Generators

- **Mean**: 53.0 μs
- **Min**: 49.0 μs
- **Max**: 1.0 ms
- **Rounds**: 8084

#### Rdflib Get Loads

- **Mean**: 148.8 μs
- **Min**: 140.7 μs
- **Max**: 369.9 μs
- **Rounds**: 3921

#### Rdflib Get Substations

- **Mean**: 54.9 μs
- **Min**: 52.1 μs
- **Max**: 169.5 μs
- **Rounds**: 7516

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.55 s
- **Min**: 1.40 s
- **Max**: 1.68 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 67.3 ms
- **Min**: 64.9 ms
- **Max**: 69.7 ms
- **Rounds**: 8

#### Triplets Get Generators

- **Mean**: 64.8 ms
- **Min**: 63.5 ms
- **Max**: 66.0 ms
- **Rounds**: 16

#### Triplets Get Loads

- **Mean**: 196.8 ms
- **Min**: 196.1 ms
- **Max**: 198.3 ms
- **Rounds**: 6

#### Triplets Get Substations

- **Mean**: 66.5 ms
- **Min**: 65.2 ms
- **Max**: 67.9 ms
- **Rounds**: 15

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 138.1 ms
- **Min**: 127.7 ms
- **Max**: 144.6 ms
- **Rounds**: 9

#### Triplets Get Lines

- **Mean**: 6.1 ms
- **Min**: 5.3 ms
- **Max**: 8.0 ms
- **Rounds**: 71

#### Triplets Get Generators

- **Mean**: 6.5 ms
- **Min**: 5.6 ms
- **Max**: 8.3 ms
- **Rounds**: 152

#### Triplets Get Loads

- **Mean**: 17.6 ms
- **Min**: 15.9 ms
- **Max**: 21.9 ms
- **Rounds**: 38

#### Triplets Get Substations

- **Mean**: 5.7 ms
- **Min**: 5.0 ms
- **Max**: 7.9 ms
- **Rounds**: 169

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 12.20 s
- **Min**: 8.74 s
- **Max**: 16.83 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 102051

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.5 μs
- **Rounds**: 48499

#### Veragrid Get Loads

- **Mean**: 0.2 μs
- **Min**: 0.1 μs
- **Max**: 8.6 μs
- **Rounds**: 159694

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 45.9 μs
- **Rounds**: 182117

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 840.0 ms
- **Min**: 571.1 ms
- **Max**: 1.53 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.1 μs
- **Min**: 0.0 μs
- **Max**: 1.1 μs
- **Rounds**: 196118

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.4 μs
- **Rounds**: 84876

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 10.0 μs
- **Rounds**: 164420

#### Veragrid Get Substations

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 1.0 μs
- **Rounds**: 84732
