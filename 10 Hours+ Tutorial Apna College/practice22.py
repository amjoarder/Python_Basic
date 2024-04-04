#WAF that replace all occurrences of “java” with “python” in above file
with open("practice_file.txt", "r") as f:
    data = f.read()

new_data = data.replace("JAVA", "Python")
print(new_data)


with open("practice_file.txt", "w") as f:
    f.write(new_data)


