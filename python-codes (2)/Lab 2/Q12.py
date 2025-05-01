import math

x=int(input("Enter the x coordinate of the center of the circle = "))
y=int(input("Enter the y coordinate of the center of the circle = "))
r=int(input("Enter the radius of the circle = "))

print("Coordinates: (", x, ",", y, ")")
print("Radius = ", r)

x1=int(input("Enter the x coordinate of a point to check = "))
y1=int(input("Enter the y coordinate of a point to check = "))

d=math.sqrt(math.pow(x1-x, 2) - math.pow(y1-y, 2))

if(d<r):
    print("Point is inside the circle")
elif(d==r):
    print("Point is on the circle")
else:
    print("Point is outside the circle")
