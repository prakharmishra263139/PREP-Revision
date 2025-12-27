# Apache Spark — Notes

## Overview
- **Open-source engine** for distributed data processing and ML.  
  _Example:_ Compute daily user metrics from TBs of web logs across a cluster.

## Implementations
- **Spark (Scala/Java):** Native engine  
  _Example:_ Production ETL job.
- **PySpark:** Python API  
  _Example:_ Data scientist prototyping in Jupyter.
- **sparklyr:** R interface  
  _Example:_ Analyst using dplyr-style queries on a cluster.

## Key Concepts & Features
- **In-memory computation & caching:** Speeds iterative jobs.  
  _Example:_ Repeated passes when training recommendation models.
- **Distributed processing & parallel execution:** Splits work across nodes.  
  _Example:_ Parsing millions of log files in parallel.
- **Fault tolerance via RDD lineage:** Recomputes lost partitions after failures.  
  _Example:_ Worker dies during ETL but results are recovered automatically.
- **Immutable data structures:** Ensures deterministic transformations and retries.  
  _Example:_ Reproducible preprocessing of clickstream data.
- **Lazy evaluation (DAG):** Builds a plan; actions trigger execution.  
  _Example:_ Chain filter/map and run count to execute only once.
- **DataFrame optimizations & SQL (Catalyst):** Advanced query planning and predicate pushdowns.  
  _Example:_ Filter predicate is pushed to Parquet read for faster scans.

## Advantages
- **High performance** (in-memory + parallelism).  
  _Example:_ Faster model training on large datasets.
- **Scalability across clusters.**  
  _Example:_ Scale from single node to hundreds of nodes processing TBs of data.
- **Unified platform** for batch, streaming, interactive, and ML.  
  _Example:_ One pipeline for ETL and real-time scoring.
- **Ease of use via high-level APIs.**  
  _Example:_ SQL/DataFrame queries instead of low-level map-reduce.
- **Strong ecosystem and connectors.**  
  _Example:_ Read/write to S3, HDFS, Kafka, databases.

## Languages & APIs
- **Scala:** Primary/native API  
  _Example:_ Core Spark job development.
- **Java:** Enterprise integrations  
  _Example:_ Embed Spark in Java services.
- **Python (PySpark):** Popular with data scientists  
  _Example:_ Jupyter data exploration.
- **R (sparklyr):** R-friendly data analysis  
  _Example:_ dplyr-style distributed transforms.

## PySpark — Summary
- **Python API for Spark** (DataFrames, SQL, MLlib, Streaming).  
  _Example:_ Use PySpark to process logs and train a distributed model in one workflow.

### PySpark — Key Features (with Examples)
- **DataFrames & SQL:** SQL-like analytics on big data.  
  _Example:_ Aggregating metrics from Parquet logs.
- **MLlib integration:** Scalable machine learning algorithms.  
  _Example:_ Distributed logistic regression training.
- **Streaming/Structured Streaming:** Real-time processing of data streams.  
  _Example:_ Compute rolling metrics from Kafka.
- **Python ecosystem integration:** Use pandas/NumPy where appropriate.  
  _Example:_ Preprocessing with pandas, scaling out with Spark.
- **Fault tolerance & lazy evaluation:** Resilient, efficient pipelines.  
  _Example:_ ETL job recovers from worker failure and is only executed when action requested.

### PySpark — Advantages (Brief)
- **Scalability**  
  _Example:_ Nightly processing of TBs of data.
- **Performance**  
  _Example:_ In-memory iterative machine learning.
- **Ease of use**  
  _Example:_ Pythonic DataFrame API in Jupyter.
- **Fault tolerance**  
  _Example:_ Automatic recompute on node failure.
- **Unified platform & strong community support**  
  _Example:_ Many connectors and active documentation/tutorials.

---

## PySpark map and reduce — Explained

### map (Transformation)
- The `map` function applies a given function to each element in a distributed dataset (e.g., an RDD or DataFrame column).
- Enables parallel data processing across different nodes of the cluster.
- _Example:_ Use `map` to square every number in a dataset, performing the computation in parallel.
- `map` is a **transformation**: it returns a new dataset (RDD or DataFrame), and execution is lazy (it only happens when an action is called).
- _Typical use-cases:_ Cleaning data, transforming values, extracting fields.

### reduce (Action)
- The `reduce` function combines elements of a dataset using a binary function to produce a single result.
- Aggregation is performed locally on each partition, then results are combined across the cluster.
- _Example:_ Summing a distributed dataset of numbers to get the total.
- `reduce` is an **action**: it triggers actual computation and brings the final result back to the driver program.
- The function must be commutative and associative for correct distributed execution.
- _Typical use-cases:_ Sums, products, maximum/minimum calculation.

---

### Hadoop Problems that Spark Solved

- **Slow processing:**  
  Hadoop MapReduce writes intermediate results to disk, which makes it slow.  
  _Spark solves this with in-memory computation for much faster processing._

- **Difficult iterative/interactive jobs:**  
  Hadoop is inefficient for iterative ML algorithms or interactive analytics.  
  _Spark supports efficient iterative processing and interactive querying._

- **Complex programming:**  
  Hadoop requires lots of complex, boilerplate code.  
  _Spark offers easy APIs in Python, Scala, and SQL._

- **No real-time capability:**  
  Hadoop is batch-only. No real-time or streaming processing.  
  _Spark provides real-time and streaming processing with Structured Streaming._

- **Limited analytics tools:**  
  Hadoop MapReduce is not optimized for SQL or advanced analytics.  
  _Spark comes with built-in SQL, DataFrames, MLlib, and Graph analytics capabilities._

---

### Summary Notes

- `map`: For element-wise transformations; lazy (does not trigger computation).
- `reduce`: Aggregates data to a single result; **triggers** Spark computation.
- These, along with functions like `flatMap` and `reduceByKey`, are core for distributed processing in Spark/Databricks.
- Spark optimizes these operations for efficient processing across large datasets and clusters.
- _Real-world examples:_ Word count, data cleaning, data aggregation in big data pipelines.

---

## How Distributed Computing Works in Spark

_Distributed computing_ splits a large computational task into smaller subtasks and runs them in parallel across multiple machines working as a single system.

- **Driver Program:**  
  Main process (your Python or Scala script); defines Spark transformations and actions, plans job execution, and coordinates work.

- **Cluster Overview:**  
  Computation is spread across multiple machines (“nodes”) working together as a cluster:  
    - **Driver node:** Runs the driver program.  
    - **Worker nodes:** Execute tasks and store data partitions.

- **Workers and Executors:**  
  Each worker node runs one or more **executor** processes; executors carry out the actual data processing. The driver sends tasks to executors and collects their results.

- **Tasks & Jobs:**  
    - When an action is called, Spark splits work into jobs, stages, and tasks.
    - A **task** operates on a data partition (e.g., mapping over part of the data).
    - Each executor runs many tasks in parallel.

- **Resource Management:**  
  Cluster manager (YARN, Kubernetes, or Spark’s standalone mode) handles resource allocation and worker node management.

- **Execution flow:**  
    1. Driver sends jobs and tasks to the cluster.
    2. Cluster manager assigns tasks to workers.
    3. Workers (executors) process data in parallel, returning results to the driver.
    4. Driver assembles final output.

- **Benefits:**  
  This distributed model lets Spark efficiently handle large datasets and compute-intensive workloads by dividing work over many computers.

---

## Why Spark Came Into Existence — What Spark Solves That Hadoop Can't

Apache Spark was built to overcome Hadoop MapReduce’s major limitations, which was once the dominant big data processing framework.

- **Hadoop MapReduce:**  
    - Works in batch mode, writing intermediate data to disk between each map and reduce step.
    - Each step reads and writes to disk, making it inefficient for workflows needing multiple steps (like iterative ML or graph processing).
    - Programming model is low-level and complex for multi-step jobs.

- **Spark Solves These Problems:**  
    - **Speed:** In-memory computation avoids repeated disk I/O. Up to 100x faster for some workloads, especially for ML and graph applications.
    - **Ease of Use:** Higher-level APIs (DataFrames, SQL) make code easier and shorter vs. raw MapReduce.
    - **Versatility:** Unified support for batch, interactive queries, streaming, machine learning, and graph analytics.
    - **Reusability & Pipelines:** Chaining transformations/actions enables efficient complex data pipelines.
    - **Active Ecosystem:** Connects to many data sources and integrates with third-party tools.

**Summary:**  
Spark was created to provide speed, developer-friendliness, and a unified approach for big data analytics, overcoming MapReduce’s inefficiency in repeated/advanced analytics.

---

## Databricks vs. Spark — What's the Difference?

- **Apache Spark:**  
  Open-source distributed computing engine for large-scale data processing. You manage the cluster setup, infrastructure, and deployment (on-premises, cloud, or your laptop).
- **Databricks:**  
  Commercial platform built on top of Spark. Provides a managed cloud environment (AWS, Azure, GCP), managed Spark clusters, collaborative notebooks, and integrated tooling for engineering, data science, and machine learning. Handles cluster management, scaling, security, and optimizations — you focus on development.

**In Short:**  
- Use **Apache Spark** if you want complete control, open-source flexibility, or need Spark on your own infrastructure.
- Use **Databricks** for a managed, scalable, collaborative analytics platform, with productivity and enterprise features (great for teams in the cloud).

