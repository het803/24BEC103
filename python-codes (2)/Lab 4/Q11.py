import math

def sin(xDeg):

    xRad = xDeg * (math.pi / 180)

    sinx = math.sin(xRad)
    return sinx

xDeg = float(input("Enter degrees: "))
result = sin(xDeg)
print(f"sin({xDeg} degrees) = {result}")