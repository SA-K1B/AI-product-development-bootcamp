# Calculator Script

This script allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## Functionality
The main function, `calculate(num1, num2, operator)`, takes three parameters:
- `num1`: The first number
- `num2`: The second number
- `operator`: The operation to perform (+, -, *, /)

The function returns:
- The result of the operation if valid
- An error message for division by zero or invalid operators

## Usage
To run the script, execute it in a Python environment. You will be prompted to enter two numbers and the operator.

## Example
```
Enter the first number: 10
Enter the second number: 5
Enter the operator (+, -, *, /): +
15.0
```
If an invalid operator is entered:
```
Enter the first number: 10
Enter the second number: 5
Enter the operator (+, -, *, /): x
Error: Invalid operator
```
If division by zero is attempted:
```
Enter the first number: 10
Enter the second number: 0
Enter the operator (/): /
Error: Division by zero
```

## Error Handling
The script checks for division by zero and invalid operators, returning appropriate error messages.
