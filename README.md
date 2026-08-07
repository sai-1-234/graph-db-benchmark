# Graph Database Benchmark

## Objective

This project benchmarks **CognoDB Cloud** against multiple graph database platforms using the same public dataset, identical logical workloads, and a common benchmark framework.

The objective is to provide a **fair, reproducible, and transparent comparison** of graph database performance under free-tier resource constraints.

---

# Databases Evaluated

| Database | Status |
|----------|--------|
| CognoDB Cloud | ✅ Benchmarked |
| Neo4j AuraDB Free | ✅ Benchmarked |
| Memgraph Cloud | ✅ Benchmarked |
| FalkorDB Cloud | ⚠️ Instance deployed, benchmark integration not completed |
| Apache AGE | ❌ Not benchmarked |

---

# Dataset

**Dataset Name**

SNAP - soc-Epinions1 Social Network

**Source**

https://snap.stanford.edu/data/soc-Epinions1.html

### Dataset Statistics

- Nodes: **75,879**
- Relationships: **508,837**

The same dataset was used for every database whenever platform limits allowed.

---

# Project Structure

```
graph-db-benchmark/
│
├── benchmark/
│   ├── aggregation.py
│   ├── benchmark_runner.py
│   ├── connect.py
│   ├── data_loader.py
│   ├── db.py
│   ├── lookup.py
│   ├── traversal.py
│   ├── workload.py
│   └── utils.py
│
├── datasets/
│
├── results/
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# Platform Configuration

The benchmark attempts to compare databases using comparable free-tier cloud resources.

| Database | Deployment | Resource Tier |
|-----------|------------|---------------|
| CognoDB Cloud | Free Tier | Provider default free tier |
| Neo4j AuraDB | Free Tier | Provider default free tier |
| Memgraph Cloud | Free Trial | Provider default trial tier |
| FalkorDB Cloud | Free Tier | Provider default free tier |

Free-tier limitations are documented where they affected benchmarking.

---

# Benchmark Methodology

Every benchmark follows the same methodology.

- Same dataset
- Same logical queries
- Same benchmark framework
- Same client machine
- Same benchmark scripts
- Warm-up before measurements
- 100 benchmark iterations for read workloads
- Reported **P50** and **P95** latency
- Mixed workload executed with **10 concurrent workers**
- Honest reporting of free-tier limitations and failed runs

---

# Benchmarks

## Data Loading

Measures:

- Total load time
- Relationships/sec

---

## Traversal Benchmark

Measures

- 1-Hop Traversal
- 2-Hop Traversal
- 3-Hop Traversal

Reports

- P50 latency
- P95 latency

---

## Lookup Benchmark

Measures

- Point lookup

Reports

- P50 latency
- P95 latency

---

## Aggregation Benchmark

Measures

- Count aggregation

Reports

- P50 latency
- P95 latency

---

## Mixed Workload

Measures

- Concurrent mixed read/write workload

Configuration

- 10 concurrent workers
- 100 operations
- Reports sustained throughput (queries/sec)

---

# Benchmark Results

| Database | Relationships | 1-Hop P50 (ms) | 1-Hop P95 (ms) | Lookup P50 (ms) | Lookup P95 (ms) | Aggregation P50 (ms) | Aggregation P95 (ms) | Mixed Workload |
|-----------|--------------:|---------------:|---------------:|----------------:|----------------:|---------------------:|---------------------:|----------------|
| CognoDB | 508000 | 1075.030 | 1618.784 | 902.682 | 1409.763 | 319.959 | 421.918 | Completed |
| Neo4j AuraDB | 400000 | 413.829 | 701.202 | 413.939 | 718.284 | 279.022 | 331.508 | Completed |
| Memgraph | 508837 | 504.614 | 1077.575 | 479.467 | 1020.467 | 298.543 | 401.395 | Completed |
| FalkorDB | — | — | — | — | — | — | — | Not Completed |
| Apache AGE | — | — | — | — | — | — | — | Not Tested |

---

# Reproducing the Benchmark

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment

Create the appropriate environment file.

Example

```
.env
.env.neo4j
.env.memgraph
```

Credentials are **not included** in this repository.

---

## Load dataset

```bash
python benchmark/data_loader.py
```

---

## Execute benchmark

```bash
python benchmark/benchmark_runner.py
```

Benchmark results are automatically written to the **results/** directory.

---

# Security

No credentials are committed to this repository.

Environment variables are loaded from local `.env` files.

Use `.env.example` as a template.

---

# Caveats

- Neo4j Aura Free reached the provider's free-tier relationship limit at approximately **400,000 relationships**, preventing import of the complete dataset.

- CognoDB successfully loaded approximately **508,000 relationships**. During loading, a small number of transient network retries occurred but benchmarking completed successfully.

- Memgraph successfully loaded the complete dataset after resolving transaction compatibility by using explicit transactions instead of managed write transactions.

- FalkorDB Cloud instance was successfully deployed and connectivity was investigated. Full benchmark integration was not completed because the existing benchmark framework was built around the Neo4j Bolt driver while FalkorDB Cloud requires a different client integration.

- Free-tier cloud services occasionally exhibited network latency and throttling which may influence observed benchmark results.

---

# Analysis

This benchmark compared multiple graph database platforms using identical datasets and equivalent benchmark workloads wherever possible.

## Observations

- Neo4j AuraDB produced the lowest observed lookup and traversal latency but could not load the complete dataset because of free-tier limits.

- CognoDB successfully loaded the complete benchmark dataset and executed every benchmark workload using the common benchmark framework.

- Memgraph successfully loaded the complete dataset after adapting the loader to use explicit transactions and produced competitive lookup and aggregation performance.

- Aggregation latency across databases was more consistent than traversal latency.

- Deep (3-hop) traversals produced noticeably higher latency than shallow traversals across all tested platforms.

## Fairness

Every benchmark used:

- the same dataset
- the same benchmark framework
- identical logical queries
- the same client machine

Where cloud providers imposed free-tier limitations, these limitations are documented rather than omitted.

The objective of this benchmark is **not** to determine a universal "best" graph database, but to provide a fair, reproducible comparison using identical datasets, workloads, and benchmark methodology under comparable free-tier resource constraints.

---

# Technologies Used

- Python 3.8+
- Neo4j Python Driver
- python-dotenv
- concurrent.futures
- CSV
- Cypher

---

# Repository

The repository contains:

- Automated benchmark framework
- Data loading scripts
- Benchmark runners
- Result collection
- Reproducible instructions
- Benchmark analysis

All benchmark code was developed to allow future extension with additional graph database platforms.