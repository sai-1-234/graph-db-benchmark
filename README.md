# Graph Database Benchmark

## Objective

This project benchmarks multiple graph databases using the same public dataset and identical workloads.

The benchmark measures:

- Data loading performance
- Traversal performance
- Lookup performance
- Aggregation performance
- Mixed workload performance

## Databases

- CognoDB Cloud
- Neo4j AuraDB
- Memgraph
- FalkorDB
- Apache AGE

## Dataset

Dataset:

SNAP - soc-Epinions1

Source:

https://snap.stanford.edu/data/soc-Epinions1.html

Statistics

- Nodes: 75,879
- Relationships: 508,837

## Project Structure

```
benchmark/
configs/
datasets/
docs/
results/
```

## Benchmarks

### Load Benchmark

Measures:

- Import time
- Relationships/sec

### Traversal

Measures:

- 1-hop traversal

### Lookup

Measures:

- Point lookup

### Aggregation

Measures:

- Count operations

### Workload

Measures:

- Concurrent read workload

## Environment

Python 3.8+

Neo4j Python Driver

python-dotenv

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python benchmark/benchmark_runner.py
```

## Results

Benchmark results are stored in the `results/` folder.

## Security

Database credentials are **not committed** to Git.

Use `.env.example` as a template.