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


## PySpark map and reduce — Explained

### map (Transformation)
- The `map` function applies a given function to each element in a distributed dataset (such as an RDD or a DataFrame column).
- In Spark and Databricks, `map` enables parallel data processing by applying the function independently to data on different nodes of the cluster.
- Example in context: If you have a dataset of numbers and want to square each number, you use `map` to do this in parallel.
- `map` is a *transformation*, meaning it returns a new dataset (RDD or DataFrame) and does not immediately compute results. Execution is lazy and only happens when an action is called.
- Typical use-cases: Cleaning data, transforming values, extracting fields.

---

### reduce (Action)
- The `reduce` function combines elements of the dataset using a binary function to produce a single result.
- In Spark and Databricks, this aggregation first happens locally on each partition, then the results are further reduced across the cluster.
- Example in context: Summing a distributed dataset of numbers to get the total.
- `reduce` is an *action*, which triggers actual computation and cluster execution; it brings the final result back to the driver program.
- The function used in `reduce` must be commutative and associative for correct distributed processing.
- Typical use-cases: Calculating sums, products, maximum/minimum values.

---

### Summary Notes
- `map` is for element-wise transformation and is lazy (does not trigger computation).
- `reduce` aggregates all data into a single result and triggers computation.
- These patterns (along with related methods such as `flatMap` and `reduceByKey`) are fundamental for distributed processing in Spark and Databricks.
- Spark optimizes these operations to efficiently process very large datasets across many machines.
- Real-world use: Classic word count problem, data cleaning, and aggregation in big data pipelines.


### How Distributed Computing Works in Spark

Distributed computing is the process of splitting a large computaional task into smaller subtasks and executing them in parallel across multiple machines that work
together as a single system.

- **Driver Program:**  
  The driver is the main process (your Python or Scala script) that defines Spark transformations and actions. It plans overall job execution and coordinates work.

- **Cluster Overview:**  
  In distributed computing, computation is spread across multiple machines (nodes) working together as a *cluster*. In Spark, the cluster consists of:
  - **Driver node:** Runs the driver program.
  - **Worker nodes:** Execute tasks and store partitions of data.

- **Workers and Executors:**  
  Each worker node runs *executor* processes. Executors perform the actual data processing tasks. The driver sends tasks to executors and collects results.

- **Tasks and Jobs:**  
  - When an action is called, Spark splits the work into *jobs*, *stages*, and *tasks*.
  - A **task** is a unit of work on a data partition (e.g., mapping over part of the dataset).  
  - Each executor executes many tasks in parallel.

- **Resource Management:**  
  A cluster manager (like YARN, Kubernetes, or Spark’s standalone mode) handles allocation of resources and management of worker nodes.

- **How it all fits together:**  
    1. Driver sends jobs and tasks to the cluster.
    2. Cluster manager assigns tasks to workers.
    3. Workers (executors) process data in parallel and return results to the driver.
    4. Driver assembles final output.

- **Benefits:**  
  This distributed model enables Spark to handle massive datasets and compute-intensive workloads efficiently by dividing the workload over multiple computers.


  ## Why Spark Came Into Existence — What Spark Solves That Hadoop Can't

  Apache Spark was created to address the major limitations of Hadoop MapReduce, which was the dominant big data processing framework before Spark.

  - **Hadoop MapReduce:**
      - Processes data in batch mode using disk for intermediate data between each map and reduce step.
      - Each step reads from and writes to disk, making it inefficient for workflows requiring multiple steps (like iterative machine learning or graph algorithms).
      - Programming model is low-level and cumbersome for complex data flows.

  - **Problems Spark Solves:**
      - **Speed:** Spark performs in-memory computation, avoiding repeated disk I/O. This makes it up to 100x faster for certain workloads, especially iterative algorithms (e.g., ML, graph processing).
      - **Ease of Use:** Spark provides higher-level APIs (DataFrames, SQL, etc.) for easier, more concise code compared to writing raw MapReduce jobs.
      - **Versatility:** Supports not only batch processing but also interactive queries, streaming, machine learning, and graph analytics in a single framework.
      - **Reusability & Pipelines:** Allows chaining multiple transformations and actions efficiently, supporting complex pipelines with less overhead.
      - **Active Ecosystem:** Integrates with a wide range of data sources and third-party tools.

  **Summary:**  
  Spark was created to overcome Hadoop MapReduce's inefficiencies for repeated and advanced analytics, to speed up big data computations, and to provide a unified, developer-friendly platform for diverse big data workloads.


  ## Databricks vs. Spark — What's the Difference?

  **Apache Spark** is an open-source distributed computing engine for large-scale data processing. It provides the underlying framework and APIs for building batch, streaming, machine learning, and analytics applications — but *you* manage the cluster setup, infrastructure, and deployment (whether on-premises, in the cloud, or on your laptop).

  **Databricks** is a commercial platform built on top of Apache Spark. It offers a cloud-based environment (on AWS, Azure, or GCP) with managed Spark clusters, collaborative notebooks, and integrated tools for data engineering, data science, machine learning, and analytics. Databricks handles cluster management, scaling, security, and optimizations automatically, letting you focus on development instead of infrastructure.|

  **In Short:**  
  - Use **Apache Spark** when you want complete control, open-source flexibility, or need to run Spark on your own infrastructure.
  - Use **Databricks** when you want a managed, scalable, collaborative analytics platform with productivity and enterprise features built in (popular for teams working in the cloud).

