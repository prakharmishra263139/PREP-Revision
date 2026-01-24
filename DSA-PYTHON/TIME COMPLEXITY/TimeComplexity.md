## What is Time Complexity?

Time complexity is a way to analyze and compare the efficiency of different algorithms or code solutions. It gives us a standard to judge which code is better, regardless of the specific hardware running it. In interviews, code is often evaluated by its time complexity.

> **Note:**  
> Time complexity does **not** refer to the actual time taken by a machine to execute code.

### Why Doesn’t Time Complexity Measure Real Time?

The running time of a code can vary across different computers. For example:
- A low-end machine (e.g., an old Windows laptop) may run the same code slower than a high-end machine (e.g., the latest MacBook).
- Hardware differences and system loads mean "real" time is not a reliable measure to compare algorithms.

Therefore, we **should not** compare two codes or algorithms based on execution time alone, as it is dependent on the hardware.

---

### Definition
> **Time complexity** describes how the running time of an algorithm changes as the input size increases.

It focuses on the growth rate of operations with respect to input size, not the machine speed. In other words, time complexity measures the relationship between input size and the number of basic operations performed, giving us a machine-independent measurement.

Let’s understand this better with the following diagram:



## What is Space Complexity?
Space complexity is a measure of the amount of memory an algorithm or code requires while it runs. Similar to time complexity, it provides a way to evaluate algorithms independently of specific hardware, so we use Big O notation to describe space usage instead of measuring it in MB, GB, etc.

> **Note:**  
> Space complexity, like time complexity, is abstracted from the real memory used by a particular machine, focusing instead on how memory requirements grow with input size.

### Definition

Space complexity represents the total memory used by an algorithm, which includes both:
- **Auxiliary space:** Extra space or temporary variables used during computation (besides the space needed to store the inputs).
- **Input space:** Memory required to store the input data itself.

So,  
**Space Complexity = Auxiliary Space + Input Space**
