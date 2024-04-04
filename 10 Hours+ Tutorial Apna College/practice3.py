#WAP to find the greatest of 3 numbers entered by the user

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))

if(a>b and a>c):
    print(a, " is the largest number")
elif(b>a and b>c):
    print(b, "is the largest number")
elif(c>a and c>b):
    print(c, "is the largest number")