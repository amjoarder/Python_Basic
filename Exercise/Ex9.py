# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads

'''
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
countHead = 0
countTail = 0
for i in result:
    if(i == "heads"):
        countHead+=1
    if(i == "tails"):
        countTail+=1
print(f'Head:{countHead}, Tail:{countTail}')'''



# 2. Print square of all numbers between 1 to 10 except even numbers
'''
for i in range(0,11):
    if(i%2 != 0):
        print(i**2)
'''



# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
'''
print("\nExercise 3\n")
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')

'''
# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message
'''
for i in range(1,6):
    print("Are you tired?")
    a = input("y or n? ")
    if(a == "y"):
        print("You didn't finish the race")
        break
    else:
        print("Continue")
        continue
        i=i+1
print("You've completed", i, "km")

'''



# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)