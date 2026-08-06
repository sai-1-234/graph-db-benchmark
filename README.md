# Graph Database Cloud Benchmark

## Objective

This project benchmarks **CognoDB Cloud** against managed graph database platforms using the same dataset, identical workloads, and reproducible benchmark scripts.

## Databases

- CognoDB Cloud
- Neo4j AuraDB
- Memgraph
- FalkorDB
- Apache AGE

## Dataset

Dataset: SNAP soc-Epinions1

Source:
https://snap.stanford.edu/data/soc-Epinions1.html

Nodes: 75,879

Relationships: 508,837

## Project Structure

```
benchmark/
datasets/
results/
docs/
```

## Benchmark Metrics

- Data Loading
- 1-Hop Traversal
- 2-Hop Traversal
- 3-Hop Traversal
- Point Lookup
- Indexed Lookup
- Aggregation
- Mixed Read/Write Workload

## Environment

Python 3.8

Neo4j Driver

python-dotenv

## Running

Install dependencies

```bash
pip install -r requirements.txt
```

Run benchmark

```bash
python benchmark/benchmark_runner.py
```

## Results

Results are stored inside the `results` folder.

## Notes

Passwords and connection URIs are stored in environment variables and are not committed to Git.