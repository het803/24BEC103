d={}
a=str(input("Enter your string: "))
l=list(a)

for i in l:
    temp={i:0}
    d.update(temp)

for i in d:
    for j in l:
        if(i==j):
            value=int(d[i])+1
            d1={i:value}
            d.update(d1)

print(d)
