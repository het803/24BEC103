a=int(input("Enter your first angle of a triangle (a): "))
b=int(input("Enter your second angle of a triangle (b): "))
c=int(input("Enter your thrid angle of a triangle (c): "))
print("a =",a)
print("b =",b)
print("c =",c)

if(a+b+c==180):
    print("Angles are of a valid traingle")
else:
    print("Angles are not of a valid traingle")
