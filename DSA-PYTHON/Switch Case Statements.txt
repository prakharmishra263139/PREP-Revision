Switch Case Statements

- If-else statements are like the Swiss Army knife of decision-making:
    - Offer flexibility and can handle a wide range of conditions and branching logic.
    - Useful when you need to evaluate complex conditions.
    - Ideal when conditions aren't based on simple equality checks.
    - Preferred for scenarios where conditions are not easily enumerable, or you need to execute different code blocks based on various conditions.

- Switch statements shine when:
    - You have a single variable to compare against multiple distinct values.
    - They help make code concise, cleaner, and more structured.
    - Best for simplifying situations with multiple exact matches.

In practice, if-else statements and switch statements often complement each other—use if-else for complex, varied conditions, and switch for clear, enumerable cases.


Example

day = int(input("Enter a number (1-7): "))

# Match-case (Python 3.10+ feature) to act like a switch
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        # Default case if no match
        print("Invalid")

