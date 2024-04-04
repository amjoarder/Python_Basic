'''
#Print from 100 to 1

i=100
while i>=1:
    print(i)
    i=i-1
'''


'''

#Multiplication Table
n = int(input("Enter a number: "))

i = 1
while i<=10:
    print(n,"*",i, "=", n*i)
    i=i+1

'''


"""
i = 1
while i<=5:
    print("[", i*i, "]" )
    i=i+1
"""



"""
hero = ["batman", "superman", "spiderman"]
i=0
while i<len(hero):
    print(hero[i])
    i=i+1
"""


hero = ["batman", "superman", "spiderman"]
x="superman"
i=0
while i<len(hero):
    if (hero[i] == x):
        print("Found at ", i)
    i=i+1
