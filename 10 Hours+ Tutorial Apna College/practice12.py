#WAP to find the sum of first n numbers. (using while)

n = int(input("Enter n: "))
sum=0

i=1
while (i<=n):
    sum = sum + i
    print(i, "Iteration",  sum)
    i=i+1
    
print("Total", sum)