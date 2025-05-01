# To print the table of a number

a=int(input("Enter the number you want to print the table of: "))
b=int(input("Till how much you want to print the table (ex., 10): "))
c=0

print("Here is your table:")

while (c<=b):
    print(a, "x", c, "=", a*c)
    c+=1
