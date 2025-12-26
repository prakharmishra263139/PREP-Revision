# Apache Spark — Notes

## Overview
- Open-source engine for distributed data processing and ML.  
    Example: compute daily user metrics from TBs of web logs across a cluster.

## Implementations
- Spark (Scala/Java) — native engine (example: production ETL job).  
- PySpark — Python API (example: data scientist prototyping in Jupyter).  
- sparklyr — R interface (example: analyst using dplyr-style queries on cluster).

## Key Concepts & Features
- In-memory computation & caching — speeds iterative jobs.  
    Example: repeated passes when training recommendation models.
- Distributed processing & parallel execution — split work across nodes.  
    Example: parsing millions of log files in parallel.
- Fault tolerance via RDD lineage — recompute lost partitions after failures.  
    Example: worker dies during ETL but results are recovered automatically.
- Immutable data structures — deterministic transformations and retries.  
    Example: reproducible preprocessing of clickstream data.
- Lazy evaluation (DAG) — transformations build a plan; actions trigger execution.  
    Example: chain filter/map and run count to execute once.
- DataFrame optimizations & SQL (Catalyst) — query planning and pushdowns.  
    Example: filter predicate pushed to Parquet read for faster scans.

## Advantages
- High performance (in-memory + parallelism). Example: faster model training on large datasets.  
- Scalability across clusters. Example: scale from single node to hundreds of nodes for TBs of data.  
- Unified platform for batch, streaming, interactive, and ML. Example: one pipeline for ETL + real-time scoring.  
- Ease of use via high-level APIs. Example: SQL/DataFrame queries instead of low-level map-reduce.  
- Strong ecosystem and connectors. Example: read/write to S3, HDFS, Kafka, databases.

## Languages & APIs
- Scala — primary/native API (example: core Spark job development).  
- Java — enterprise integrations (example: embed Spark in Java services).  
- Python (PySpark) — popular with data scientists (example: Jupyter data exploration).  
- R (sparklyr) — R-friendly data analysis (example: dplyr-style distributed transforms).

## PySpark — Summary
- Python API for Spark (DataFrames, SQL, MLlib, Streaming).  
    Example: use PySpark to process logs and train a distributed model in one workflow.

### PySpark — Key Features (one-line + example)
- DataFrames & SQL — SQL-like analytics on big data. Example: aggregating metrics from Parquet logs.  
- MLlib integration — scalable ML algorithms. Example: distributed logistic regression training.  
- Streaming/Structured Streaming — real-time stream processing. Example: compute rolling metrics from Kafka.  
- Python ecosystem integration — use pandas/NumPy where appropriate. Example: sample preprocessing with pandas, scale with Spark.  
- Fault tolerance & lazy evaluation — resilient and efficient pipelines. Example: ETL job recovers from worker failure and executes only when action requested.

### PySpark — Advantages (short)
- Scalability (example: nightly processing of TBs).  
- Performance (example: in-memory iterative ML).  
- Ease of use (example: Pythonic DataFrame API in Jupyter).  
- Fault tolerance (example: automatic recompute on node failure).  
- Unified platform & community support (example: many connectors and active docs/tutorials).
