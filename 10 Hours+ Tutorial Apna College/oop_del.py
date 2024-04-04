class Student:
    def __init__(self, name):
        self.name = name

s1=Student("John")

del s1
print(s1.name)

