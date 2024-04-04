#take n input and show odd or even using a function

def odd_even(n):
    if (n%2 == 0):
        print("Even")
    else:
        print("Odd")
    

n = int(input("Enter a Number:"))
odd_even(n)