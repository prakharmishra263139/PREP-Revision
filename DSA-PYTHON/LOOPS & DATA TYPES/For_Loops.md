What is a For Loop and Why is it Used?

A for loop is a control structure in programming that allows you to execute a specific block of code repeatedly. It's especially useful when you want to perform the same task multiple times without duplicating your code. Let's break down the essential components of a for loop:

- Initialization:        You declare and initialize a variable that serves as a counter. This step only happens once at the beginning.
- Condition:             You specify a condition that determines when the loop should stop executing.
- Increment/Decrement:   You define how the counter variable changes after each iteration.

// Note:
// The following example shows a nested for loop in Java.
// The outer loop runs 3 times (i = 0 to 2), and for each i,
// the inner loop also runs 3 times (j = 0 to 2).
// This results in a 3x3 grid of outputs, showing every possible combination of i and j.

//
// public class Main {
//     public static void main(String[] args) {
//         for (int i = 0; i < 3; i++) {
//             for (int j = 0; j < 3; j++) {
//                 System.out.println("i = " + i + ", j = " + j);
//             }
//         }
//     }
// }
//
