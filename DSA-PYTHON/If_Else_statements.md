Python is flexible: you can assign an integer to a variable, and later assign a string to the same variable without errors. However, this flexibility means you must be more cautious with type-related logic.

If-Else Statements

Conditional statements are a key concept in programming, allowing decisions based on conditions. These let your code execute different blocks depending on whether specific conditions are met.

The `if-else` Statement

The `if` statement executes a block of code if a condition is true. The `else` statement is optional and lets you specify code to run if the `if` condition is false.

Flow of control:

- If the condition in the `if` statement is true, the code inside the if block executes.
- If the condition is false, the code inside the else block (if present) executes.


# Ask the user for their age
age = int(input("Enter your age: "))  # Input is a string, so convert to integer

# Check if the entered age is greater than or equal to 18
if age >= 18:
    # If true, print that the user is an adult
    print("You are an adult.")
else:
    # Otherwise, print that the user is not an adult
    print("You are not an adult.")
