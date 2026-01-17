While Loops in Programming

- Loops are used to repeat a block of code multiple times based on a given condition.
- The **while** loop is a type of loop that continues running as long as its condition remains true.
- **How a while loop works:**
    - **1. Evaluate condition:**           The loop checks its test expression (condition) before each iteration.
    - **2. Execute code if true:**         If the condition is true, the code inside the loop runs.
    - **3. Re-evaluate after each run:**   The loop checks the condition again after completing the loop body.
    - **4. Repeat or exit:**               If the condition is still true, repeat the loop. If false, exit.

- If the condition is false from the start, the loop body doesn't execute at all.
- The while loop's execution entirely depends on its test condition being true.


- While loops can be best illustrated with the practical example of finding the factorial of a number.
    - The factorial of a number `n` is the product of all positive integers from 1 to `n`.
    - To compute this using a while loop:
        - Initialize a factorial variable to 1.
        - Repeatedly multiply it by `n` while decrementing `n` until `n` becomes 0.
        - This process ensures the factorial is calculated correctly.

- While loops are particularly useful when you need a block of code to execute only as long as a condition is true.
    - The loop terminates as soon as the condition becomes false.
    - This is vital for tasks like validating user input or processing data until a specific condition is met.
    - By checking the condition at the beginning of the loop, you control whether the loop body executes at all.
    
> **Example:** Calculating factorial using a while loop in Python  
> ```python
> # Initialize number
> n = 5
> factorial = 1
>
> # Loop to calculate factorial using while
> while n > 0:
>     factorial *= n
>     n -= 1
>
> print(f"Factorial of 5 is: {factorial}")
> ```
//
// The above code snippet demonstrates how to use a while loop
// to calculate the factorial of 5. Each step is visible in the code box,
// making it easy to read in a README or Markdown file.
//
