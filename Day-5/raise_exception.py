def withdraw(balance,amount):
    if(amount<=0):
        raise ValueError("Invalid amount")
    if(amount>balance):
        raise ValueError("Insufficeint funds")
    return balance-amount

try:
    print(withdraw(5000,3000))
except ValueError as e:
    print(e)