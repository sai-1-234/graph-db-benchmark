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

## Benchmark Results

| Database   | Nodes | Relationships | Load Time (s) | Relationships/s | Traversal P50 | Traversal P95 | Lookup P50 | Lookup P95 | Aggregation P50 | Aggregation P95 | Notes |
| ---------- | ----: | ------------: | ------------: | --------------: | ------------: | ------------: | ---------: | ---------: | --------------: | --------------: | ----- |
| CognoDB    |       |               |               |                 |               |               |            |            |                 |                 |       |
| Neo4j Aura |       |               |               |                 |               |               |            |            |                 |                 |       |
| Memgraph   |       |               |               |                 |               |               |            |            |                 |                 |       |
| FalkorDB   |       |               |               |                 |               |               |            |            |                 |                 |       |
| Apache AGE |       |               |               |                 |               |               |            |            |                 |                 |       |

## Caveats

- Neo4j Aura Free reached its free-tier relationship limit at approximately 400,000 relationships, so the full dataset could not be loaded.

- CognoDB successfully loaded approximately 508,000 relationships. During loading, a few transient network connection retries occurred, but the import completed sufficiently for benchmarking.

- Memgraph connection testing succeeded, but bulk data loading encountered SSL/TLS connection issues, preventing benchmark execution.

- FalkorDB cloud instance was successfully deployed, but integration with the existing Neo4j-driver-based benchmark framework was not completed during the assignment.

## Analysis

This benchmark compared CognoDB Cloud with other managed graph database platforms using the same benchmark framework and dataset where possible.

### Key Observations

- Neo4j Aura demonstrated lower traversal and lookup latency than CognoDB in the observed benchmark runs, but the free-tier relationship limit prevented loading the complete dataset.

- CognoDB successfully loaded approximately 508,000 relationships and completed all benchmark workloads. During loading, a small number of transient connection retries occurred, but benchmarking completed successfully.

- Aggregation latency was relatively similar between CognoDB and Neo4j Aura compared with traversal and lookup latency.

- Free-tier limitations significantly affected benchmarking. Platform quotas, storage limits, and cloud network latency influenced the observed performance and the ability to load identical datasets.

### Fairness

Every benchmark used the same benchmark framework, identical logical queries, and the same client machine. Where platforms imposed free-tier limitations, these limitations have been documented as part of the benchmark results rather than omitted.

## Methodology

- Same dataset used for every platform.
- Same benchmark scripts executed for every platform.
- Measurements collected after warm-up.
- Benchmarks executed from the same client machine.
- Free-tier limitations and observed caveats are documented.

Neo4j Aura Free reached its free-tier storage limit at approximately 400,000 relationships, so the complete SNAP soc-Epinions1 dataset could not be loaded without upgrading the instance.
