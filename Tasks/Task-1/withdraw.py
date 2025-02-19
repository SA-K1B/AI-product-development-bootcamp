#function for withdrawing
def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient funds"
    return balance - amount

# take input for balance and amount 
balance = int(input("Enter balance: "))
amount = int(input("Enter amount: "))
new_balance = withdraw(balance, amount)
#check if returned statement is integer or string
# if integer, print the new balance
# if string, print the insufficient funds message

if type(new_balance) == int:
    print(f"New balance: {new_balance}")
else:
    print(new_balance)
