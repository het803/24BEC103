a=int(input("Enter your first number (a): "))
b=int(input("Enter your second number (b): "))
c=int(input("Enter your third number (c): "))
print("a =",a)
print("b =",b)
print("c =",c)

if(a>b and a>c):
    print(a, "is the largest number")
elif(b>a and b>c):
    print(b, "is the largest number")
else:
    print(c, "is the largest number")

if(a<b and a<c):
    print(a, "is the smallest number")
elif(b<a and b<c):
    print(b, "is the smallest number")
else:
    print(c, "is the smallest number")
