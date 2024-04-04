marks=[100,98,95,100,97]

marks.append(99)
print(marks)

marks.insert(0,99)
print(marks)

print(99 in marks)

print(len(marks))


i=0
while i<len(marks):
    print(marks[i])
    i=i+1

marks.clear() #clears list