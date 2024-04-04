#Create methods for debit, credit & printing the balance
class Account:
    def __init__(self, balance, accNo):
        self.balance= balance
        self.accNo=accNo
    
    def debit(self, amount):
        self.balance -= amount
        print(amount, "Debited")
        print("Total Balance", self.get_bal())
    
    def credit(self, amount):
        self.balance +=amount
        print(amount,"Credited")
        print("Total Balance", self.get_bal())
    
    def get_bal(self):
        return self.balance
    
acc1 = Account(91000,12345)
acc1.debit(90000)
acc1.credit(5000)
acc1.credit(1000)