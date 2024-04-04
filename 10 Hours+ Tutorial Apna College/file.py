f = open("file1.txt","r")

'''
data = f.read()
print(data)
#ekbar read hoye gele r read hobe na.
'''

data1 = f.readline()
print(data1)

print(type(data1))

f.close()



