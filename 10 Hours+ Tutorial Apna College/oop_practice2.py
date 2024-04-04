#Create Account class with 2 attributes - balance & account no.

class Account:
    def __init__(self, balance, accNo):
        self.balance= balance
        self.accNo=accNo

print(Account)

acc1 = Account(1000, 101)
print(acc1.balance, acc1.accNo)