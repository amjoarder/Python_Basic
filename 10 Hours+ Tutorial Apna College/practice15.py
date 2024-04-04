# WAF to print the elements of a list in a single line. ( list is the parameter)

a = [1,2,3,4,5,6]

def element(list):
    for items in list:
        print(items, end=" ")

element(a)