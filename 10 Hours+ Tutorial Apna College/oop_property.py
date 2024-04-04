class Student:
    def __init__(self, coa, net, cpp):
        self.coa = coa
        self.net = net
        self.cpp = cpp

    @property
    def percentage(self):
        return str((self.coa+self.net+self.cpp)/3)+"%"
        
s1 = Student(98,97,96)
print(s1.percentage)
#mark change. percentage changed automatically
s1.coa = 89
print(s1.percentage)
