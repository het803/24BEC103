import random

mylist=[]
for i in range(0, 20):
    mylist.append(random.randint(0, 10))

print(f"Here is your list: {mylist}")

a=int(input("Which number's occurrences you want: "))
numOccu=[]
for i in range(0, 20):
    if(mylist[i]==a):
        numOccu.append(i)
print(f"Here is where your number came: {numOccu}")
