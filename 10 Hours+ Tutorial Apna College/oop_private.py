class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #private
#private method
    def __hello(): 
        print("aaaa")

acc1 = Account("12543", "@%$^&")

print(acc1.acc_no)
print(acc1.__acc_pass) #it'll get error. can not access private out of it's class

