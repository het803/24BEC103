import random

ls=[]

for i in range(0, 10):
    temp=random.randint(-15, 15)
    ls.append(temp)

squares=list(map(lambda n:n**2, ls))
print(f"Here is the original list: {ls}\nHere is the list of its' squares: {squares}")
