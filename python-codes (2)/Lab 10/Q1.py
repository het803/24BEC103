file=open("test.csv", "w")
file.write("Hello\n")
file.write("World")
file.close()

file=open("test.csv", "r")
print(file.read())
file.close()
