class Student:
    university = "University"
#parameterized constructor
    def __init__(self, name):
        #print(self)
        self.name = name
        print("adding")

s1 = Student("A M Joarder")
#print(s1)
print(s1.university, s1.name)
