class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"{amount} is debited,bal is {self.getbal()}")
        else:
            print("insufficient funds")
    def credit(self,amount):
        self.balance+=amount
        print(f"{amount} is credited,bal is {self.getbal()}")
    def getbal(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self,interest):
        self.interest=interest
        super().__init__(1000,"acc123")
    def interestrate(self):
        intrest1=self.balance*(self.interest/100)
        self.balance+=intrest1
        print(self.getbal())
acc1=SavingsAccount(5)
acc1.credit(500)
acc1.interestrate()
OUTPUT:
500 is credited,bal is 1500
1575.0
