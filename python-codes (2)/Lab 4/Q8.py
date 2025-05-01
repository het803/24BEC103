# To compute the factorial of a number

a=int(input("Enter number you want the factorial of: "))
b=1

for i in range(1, a+1):
    b*=i

print("Factorial of", a, "is =", b)
