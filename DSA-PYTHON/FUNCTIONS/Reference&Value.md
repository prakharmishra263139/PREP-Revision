## Functions: Pass by Value vs. Pass by Reference

Before we dive into code, let's use a simple analogy:

> **Imagine you're helping a friend edit their resume:**
>
> - **Option 1:** You take a *photocopy* of their resume and edit that. - pass by value 
>   - The friend's original resume stays unchanged.
>
> - **Option 2:** You take the *original* resume and make edits. -  pass by reference
>   - The friend's resume is directly changed.

This is very similar to how programming languages *pass data to functions:*  
- Sometimes they pass a **copy** of the data (called *pass by value*), so the original isn't changed.
- Sometimes they pass a **reference to the original data** (called *pass by reference*), so changes affect the original.

Knowing which method your language uses is important for understanding how data changes inside functions.


### What is Pass by Value?

When a variable is passed by value, a copy of the variable is made. The function works on that copy, and the original variable remains unchanged.
Imagine passing your Xeroxed mark sheet to a company. If they stamp or mark it, your original remains untouched. That’s pass-by-value.

**Key Characteristics:**
- The function receives a separate copy.
- Changes inside the function don’t affect the original variable.
- Safe, but potentially less efficient for large objects.

### What is Pass by Reference?

When a variable is passed by reference, the function receives the actual variable (not a copy). Any changes made inside the function will reflect on the original.
Imagine you give your friend your actual debit card to withdraw money. Any changes made (like balance deduction) affect your real bank account. That’s pass-by-reference.

**Key Characteristics:**
- The function receives the original memory address.
- Changes inside the function affect the original.
- Useful when you want to update multiple variables or return multiple values.



### Pass by Value vs. Reference in Python

Python uses a model sometimes called **"pass by object reference"** or **"pass by assignment."** This means:

- When you pass a variable to a function, you're passing a reference to the object, not the actual object.
- If the object is **immutable** (like `int`, `float`, `str`, `tuple`), it **behaves like pass by value**: changes inside the function do **not** affect the original.
- If the object is **mutable** (like `list`, `dict`, `set`), it **behaves like pass by reference**: changes inside the function **do** affect the original object.

#### Example 1: Immutable Type (int acts like pass by value)

```python
def modify(a):
    a = a + 10    # This creates a new int object inside the function

x = 5
modify(x)
print(x)  # Output: 5  (x is unchanged)
```

- `int` objects cannot be changed; inside the function, `a` just points to a new integer, but `x` outside remains `5`.

#### Example 2: Mutable Type (list acts like pass by reference)

```python
def modify(lst):
    lst.append(10)  # This modifies the original list object

nums = [5]
modify(nums)
print(nums)  # Output: [5, 10]
```

- The `modify` function appends to the list, and you see the change outside the function, because both `lst` and `nums` refer to the same list object in memory.

> **Note:**  
> Python's model is not *true* pass-by-value or pass-by-reference, but understanding the mutability of your data types will help you avoid surprises!


