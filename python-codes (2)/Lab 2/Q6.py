a=int(input("Enter your number: "))
print("Number =",a)
temp=a
b=1
i=10

while (temp%i==0):
    b+=1
    temp=temp/i
    i*=10

print("It is", b, "digit(s) number")
