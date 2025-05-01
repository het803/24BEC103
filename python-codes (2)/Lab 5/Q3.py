import random

mylist=[]
for i in range(0, 50):
    mylist.append(random.randint(0, 30))

print(f"Here is your list before modifications: {mylist}")
# modifiedList=removeDuplicate(list)
print(f"Here is your list after modifications: {list(set(mylist))}")
