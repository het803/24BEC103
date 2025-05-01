import random

mylist=[]
for i in range(0, 30):
    mylist.append(random.randint(-20, 20))

mypositiveList=[]
mynegativeList=[]

for i in range(0, 30):
    if(mylist[i]<0):
        mynegativeList.append(mylist[i])
    else:
        mypositiveList.append(mylist[i])

print(f"Here is your whole list: {mylist}")
print(f"Here is your positive list: {mypositiveList}")
print(f"Here is your negative list: {mynegativeList}")
