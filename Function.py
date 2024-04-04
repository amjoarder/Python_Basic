#Built-in Function
# int() str() float() min() range() max()

#Module Function
import math
print(dir(math))
from math import sqrt
print(sqrt(4))


import random
print(dir(random))

import string
print(dir(string))

#User Defined

def sum(a, b):
    print(a + b)
sum(1, 2)




def sum(a, b=4):
    print(a + b)
sum(1,5)