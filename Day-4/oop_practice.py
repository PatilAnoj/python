#bank_account

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        if(amount<=0):
            raise ValueError("Amount must be positive")
        self.balance=self.balance+amount
        return self.balance
    
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Amount must be positive")
        if(amount>self.balance):
            raise ValueError("insufficient funds ") 
        
        self.balance=self.balance-amount
        return self.balance
pnb=BankAccount(1234,5000)
print(pnb.deposit(2000))
print(pnb.withdraw(800))


#product class
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def apply_discount(self,percent):
        if percent<0 or percent>100:
            raise ValueError("invalid discount percentage")
        
        discount_amount= self.price*(percent/100)
        self.price-=discount_amount
        return self.price
        
