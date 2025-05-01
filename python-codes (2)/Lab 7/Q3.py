#import copy

# we need employee Roll number, then his/her dept., then his/her salary
d1={}
depts={}
maxSal={}
minSal={}
    
a=int(input("Enter the number of employees you want to enter the data of: "))

for i in range(0, a):
    temp=str(input(f"Enter the roll nmber of the employee ({i+1}): "))
    temp2=str(input(f"Enter the department of the employee ({i+1}): "))
    temp3=str(input(f"Enter the salary of the employee ({i+1}): "))
    dtemp={f"{temp}": { "dept":f"{temp2}", "sal":f"{temp3}" }}
    d1.update(dtemp)

for j in d1:
    d=d1[j]
    dept={d["dept"]:d["dept"]}
    maxSalTemp={d["dept"]:0}
    minSalTemp={d["dept"]:0}
    maxSal.update(maxSalTemp)
    minSal.update(minSalTemp)
    depts.update(dept)
    
for k in d1:
    d=d1[k]
    for l in depts:
        if(d["dept"]==l):
            toCheck=copy.copy(d["sal"])
            byMaxCheck=maxSal[l]
            byMinCheck=minSal[l]
            if(int(toCheck)>int(byMaxCheck)):
                updateMax={l:d["sal"]}
                maxSal.update(updateMax)
            if(int(toCheck)<int(byMinCheck)):
                updateMin={l:d["sal"]}
                minSal.update(updateMin)

for m in depts:
    print(f"Here is maximum salary in {m} department: {maxSal[m]}")
    print(f"Here is minimum salary in {m} department: {minSal[m]}")
