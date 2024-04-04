#Random Password Generator
import random
import string
#s = string.ascii_letters()
#randC = random.choice()

pass_len = 12

charValues = string.ascii_letters + string.digits + string.punctuation


password = ""

for i in range(pass_len):
    password+= random.choice(charValues)

print(password)


#we can do this using list comprehension
'''
pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

res = [random.choice(charValues) for i in range(pass_len)]
print(res)
'''

