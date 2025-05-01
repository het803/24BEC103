x = set()
for i in range(5):
    name = input("Enter a name: ")
    x.add(name)

name = input("Enter the name to edit: ")
x.discard(name)
name = input("Enter the new name: ")
x.add(name)

print(x)

for i in range(2):
    name = input("Enter the name to delete: ")
    x.discard(name)

print(x)