#WAP to find the factorial of first n numbers. (using for)

n = int(input("Enter n: "))

fact=1

for i in range(1, n+1):
    fact=fact*i
print("Factorial of", n, "is", fact)