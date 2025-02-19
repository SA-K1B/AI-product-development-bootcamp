# Withdraw Script

This script allows users to withdraw an amount from their balance, checking for sufficient funds before processing the transaction.

## Functionality
The main function, `withdraw(balance, amount)`, takes two parameters:
- `balance`: The current balance of the user
- `amount`: The amount the user wishes to withdraw

The function returns:
- The new balance if the withdrawal is successful
- A message "Insufficient funds" if the withdrawal amount exceeds the balance

## Usage
To run the script, execute it in a Python environment. You will be prompted to enter your current balance and the amount you wish to withdraw.

## Example
```
Enter balance: 100
Enter amount: 50
New balance: 50
```
If the withdrawal amount exceeds the balance:
```
Enter balance: 100
Enter amount: 150
Insufficient funds
```

## Error Handling
The script checks if the withdrawal amount is greater than the balance and returns an appropriate message if funds are insufficient.
