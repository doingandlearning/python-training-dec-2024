### Lab: Handling Errors in Division

In this lab, you will write a Python script that prompts users for two numbers and divides the first by the second. Your task is to handle potential errors gracefully, ensuring the program does not crash and provides meaningful feedback to the user.

#### Instructions:

1. Prompt the user to input two numbers.
2. Attempt to divide the first number by the second.
3. Handle the following potential errors:
   - **Non-numeric input**: Inform the user if the input is not a number.
   - **Division by zero**: Inform the user that division by zero is not allowed.
4. Ensure the program continues to run and allows the user to try again after an error.

#### Example Output:

```
Enter the first number: 10
Enter the second number: 0
Error: Division by zero is not allowed. Please try again.

Enter the first number: 10
Enter the second number: a
Error: Non-numeric input. Please enter valid numbers.

Enter the first number: 10
Enter the second number: 2
Result: 5.0
```

#### Tips:

- Use `try` and `except` blocks to handle exceptions.
- Consider using a loop to allow the user to retry after an error.

Good luck, and happy coding!
