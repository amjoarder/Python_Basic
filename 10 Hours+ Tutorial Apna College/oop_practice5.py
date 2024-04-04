class Employee:
    def __init__(self,role, department,salary):
        self.role=role
        self.department =department
        self.salary=salary

    def ShowDetail(self):
        print(self.role)  
        print(self.department) 
        print(self.salary)
    
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Tech", "500000$")


e1 = Employee("Engineer", "IT Dept.", "100000$/month")
e1.ShowDetail()

E1 = Engineer("AMJ", "25")
E1.ShowDetail()