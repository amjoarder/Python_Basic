#write a recursive function to print all elements in a list. Hint: use list & index as parameters


def print_(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_(list, idx+1)

fruits = ["Mango", "Banana", "Guava"]

print(fruits)