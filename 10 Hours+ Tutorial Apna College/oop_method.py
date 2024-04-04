class Student:
    university = "University"

    def __init__(self, name):
        
        self.name = name
        print("adding")
#method
    def hello(self):
        print("This is a method")

s1 = Student("A M Joarder")
s1.hello()
print(s1.name)

