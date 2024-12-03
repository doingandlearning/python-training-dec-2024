# Lab: Basic Arithmetic Operations

## Objective

Write a script that takes two numbers as input and outputs their sum, difference, product, and quotient.

## Instructions

1. Create a new Python script file.
2. Prompt the user to enter two numbers.
3. Calculate the sum, difference, product, and quotient of the two numbers.
4. Display the results to the user.

## Example

```python
# Example output
Enter the first number: 10
Enter the second number: 5

Sum: 15
Difference: 5
Product: 50
Quotient: 2.0
```

## Tips

- Use the `input()` function to get user input.
- Convert the input to integers or floats as needed.
- Handle division by zero appropriately.

## Extension: Using Command Line Arguments

### Objective

Modify the script to accept the two numbers as command line arguments instead of prompting the user for input.

### Instructions

1. Import the `sys` module to access command line arguments.
2. Retrieve the two numbers from `sys.argv`.
3. Calculate the sum, difference, product, and quotient of the two numbers.
4. Display the results to the user.

### Example

```python
# Example usage
$ python script.py 10 5

Sum: 15
Difference: 5
Product: 50
Quotient: 2.0
```

### Tips

- Use `sys.argv` to get the command line arguments.
- Convert the arguments to integers or floats as needed.
- Handle cases where the correct number of arguments is not provided.
- Handle division by zero appropriately.
