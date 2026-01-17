## Arrays
- An array is a linear data structure that stores elements, allowing efficient operations and random access using index values.
- Elements in an array are of the same type (homogeneous) and are stored in contiguous (adjacent) memory locations.
- Arrays organize related data together, making it easy to find and operate on any element due to predictable memory placement.
- Because the computer knows where each element is in memory, accessing one or more elements is very fast.

Let’s Visualize arrays..!
To understand how the array works, Visualize your computer’s memory as a continuous block or grid. Each piece of block or grid contains information/data that is stored in it.

Why are arrays 0-indexed?
- Indexing from 0 simplifies memory computation: the index directly represents the offset from the start of the array.
- This avoids having to subtract 1 (as in n-1) for each element’s address calculation.
- For an array of length n, valid indexes run from 0 up to n-1.
- Most programming languages use 0-based indexing for this reason, making it standard and built-in to their design.


Defining an Array:
- An array is defined to hold elements all of the same data type.
    - Example: If you create an array of integers, every element in that array must be an integer.
- Arrays can be used to store different types of values: integers, strings, boolean values, characters, or objects.
    - However, once the type is set for an array, every element must match that type.
    - Mixing types in the same array is not allowed.
- Arrays cannot mix heterogeneous data; all elements must contain the same kind of data.

Creating an array:
    - Assign it to a variable (name of the array).
    - Define the type of elements it will store (integer, string, boolean).
    - Define its size (the maximum number of elements it will store).

Syntax:      Data_type   array_name   [Array_size];
Example:     int myArray[8];
    int      => Data type
    myArray  => Name of array
    [8]      => Size of array
When you define the size of the array, all of that space in memory is "reserved".


Summary of Arrays:
- Memory is allocated instantly: As soon as the array is created, space in memory is reserved and the array is empty until values are assigned.
- Elements are stored contiguously: All elements are placed in adjacent locations, enabling very efficient direct access (O(1) time complexity) using index values.
- Fixed size and type: The array’s size and the type of its elements are established at creation. Arrays only store elements of the same (homogeneous) data type.
- Inserting elements: Inserting at the end of the array is simple and takes constant time O(1). Inserting at the start or in the middle is possible, but it requires shifting elements and is more complex.
- Removing elements: Removing from a specific index can be done in constant time O(1), but removing from the start or middle also may require shifting elements.
