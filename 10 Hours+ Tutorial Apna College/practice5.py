#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = [1, 3, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")