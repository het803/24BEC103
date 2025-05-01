a=int(input("Enter length of the rectangle: "))
b=int(input("Enter breadth of the rectangle: "))
print("Length =",a)
print("Breadth =",b)

area=a*b
perimeter=2*(a+b)

print("Area =", area)
print("Perimeter =", perimeter)

if(area>perimeter):
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than area")
