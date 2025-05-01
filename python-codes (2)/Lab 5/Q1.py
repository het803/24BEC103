import random

def flatten(args):
    flattenList=[]
    for i in args:
        if isinstance(i, list):
            flattenList.extend(flatten(i))
        else:
            flattenList.append(i)
    return flattenList

a=str(input("Do you want to enter the integers yourself? (yes/no): "))

if(a.lower() =="yes"):
    temp=int(input("How many odd integers: "))
    odd=[]
    for i in range(0, temp):
        oddTemp=int(input(f"Enter {i} element for list of odd integer: "))
        odd.append(oddTemp)
    temp=int(input("How many even integers: "))
    even=[]
    for i in range(0, temp):
        evenTemp=int(input(f"Enter {i} element for list of odd integer: "))
        even.append(evenTemp)
else:
    odd=[]
    for i in range(0, 5):
        oddTemp=random.randint(0, 999999)
        odd.append(oddTemp)
    even=[]
    for i in range(0, 4):
        evenTemp=random.randint(0, 999999)
        even.append(evenTemp)

b=str(input("Do want to choose which element from the odd list to replace (yes/no): "))

if(b.lower()=="yes"):
    temp=int(input("Which index: "))
    odd[temp]=even
else:
    odd[2]=even

print(odd)
flattenList=flatten(odd)
print(f"Here is you flatten list: {flattenList}")
sortList=flattenList.sort()
print(f"Here is your sorted list: {sortList}")
