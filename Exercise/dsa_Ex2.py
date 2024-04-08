'''# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",exp[1]-exp[0]) # 150

# 2. Find out your total expense in first quarter (first three months) of the year
print("Expense for first quarter:",exp[0]+exp[1]+exp[2]) # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exp) # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June:",exp) # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]'''






'''
You have a list of your favorite marvel super heros.
1. Length of the list
#print(len(heros))

2. Add 'black panther' at the end of this list

#heros.append("black panther")
#print(heros)

3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'

heros=['spider man','thor','hulk','iron man','captain america']
heros.append("black panther")
heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)


4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).

heros=['spider man','thor','hulk','iron man','captain america']
heros.append("black panther")
heros.remove("thor")
heros.remove("hulk")
heros.append("doctor strange")
print(heros)



   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros=['spider man','thor','hulk','iron man','captain america']
heros.append("black panther")
heros.remove("thor")
heros.remove("hulk")
heros.append("doctor strange")
hero = heros.sort()
print(hero)
'''




#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

maxNum = int(input("Maximum Number: "))

for i in range(maxNum):
    if(i%2 != 0):
        print(i)


'''
max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)
'''