#w = write. meaning overwrites the previous text
f = open("file1.txt","w")
f.write("I want to learn PYTHON")


#a = append. meaning add something
f = open("file1.txt", "a")
f.write("\n2nd line")
f.close()


with open("file1.txt", "a") as f:
    data = f.read()

