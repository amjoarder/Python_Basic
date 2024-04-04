#Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks


    def avg(self):
        sum = 0
        for value in self.marks:
            sum=sum+value
            
        print("Hi", self.name, "Your Score is", sum/3)

s1=Student("Ajmain", [99,99,100])
s1.avg()