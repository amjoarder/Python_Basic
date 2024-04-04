import random 
randNum = random.randint(1,100)


while True:
    n = input("Enter a number from 1 to 100 or Press Q to Quit: ")
    if(n == "Q"):
        break
    n = int(input("Enter a number from 1 to 100 or Press Q to Quit: "))
    if(n == randNum):
        print("You are Correct!")
        break
    elif(n<randNum):
            print("The number is less than the guessed number. Guess Again")
    else:
            print("The number is greater than the guessed number. Guess Again",)

print("Random Number was",randNum)




