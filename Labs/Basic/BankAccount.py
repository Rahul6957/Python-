class BankAccount:
    def __init__(self,accountHolder="RAHUL",balance=0):
        self.accountHolder=accountHolder
        self.balance=balance

    def deposit( self, amount):
     a=2
     self.balance =self.balance + amount
     return amount

    def withdraw (self,amount):

        self.balance= self.balance - amount
        return amount

    def check_balance(self):
       return self.balance


ob=BankAccount()























































       
s1 = BankAccount()
p=s1.deposit(200)
print(f"Deposit {p}")
pr=s1.withdraw(100)
print(f"withdraw {pr}")
pri=s1.check_balance()
print(f"Balance {pri}")