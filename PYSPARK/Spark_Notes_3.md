### Lazy Evaluation and Actions in Spark

- **Lazy Evaluation**:  
  - In Spark, transformations (like `map`, `filter`) are not executed immediately.
  - Spark builds a plan of these operations and waits until it is necessary to compute the result.
  - Computation happens *only* when an action is called.
  - This makes Spark efficient, as it can optimize the way it runs jobs.

- **Example of Lazy Evaluation**:
  - If you write a transformation like filtering data, Spark doesn't do anything right away.
  - The actual filtering happens only when you ask Spark for an output (like counting or collecting the data).

- **Actions**:  
  - Actions are operations that trigger the computation in Spark and return results.
  - When an action is called, Spark runs all the transformations needed to produce the output.
  - Some common actions are:  
    - `collect()`: Gets all data as a list.
    - `count()`: Returns the number of items.
    - `first()`: Returns the first element.
    - `show()`: Displays the data (for DataFrames).

- **Example of Actions**:
  - After you’ve defined transformations, running an action like `collect()` or `count()` will make Spark process the data and show you the result.

*In summary: In Spark, transformations are lazy and only processed when you run an action. Actions produce results and trigger computation.*

