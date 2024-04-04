#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value



dict={}
print(type(dict))

sub1 = input("Enter 1st Subject: ")
marks1 = input("Marks of 1st Subject: ")
dict.update({sub1:marks1})
print(dict)

sub2 = input("Enter 2nd Subject: ")
marks2 = input("Marks of 2nd Subject: ")
dict.update({sub2:marks2})
print(dict)

sub3 = input("Enter 3rd Subject: ")
marks3 = input("Marks of 3rd Subject: ")
dict.update({sub3:marks3})
print(dict)