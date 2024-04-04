num1=input("Enther the first number: ")
num2=input("Enther the second number: ")

sign=input("Write the name of the operation:(+,-,*,/,%) ")

sum=int(num1)+int(num2)
sub=int(num1)-int(num2)
mul=int(num1)*int(num2)
div=int(num1)/int(num2)
mod=int(num1)%int(num2)

print("The Result is: ")
if sign=='+':
    print(sum)
elif sign=='-':
    print(sub)
elif sign=='*':
    print(mul)
elif sign=='/':
    print(div)
elif sign=='%':
    print(mod)
else:
    print("Invalid")