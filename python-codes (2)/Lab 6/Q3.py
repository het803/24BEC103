tp=(13, 2, 2025)

print(f"Here is a default date tuple: {tp}")
print("Now enter your date:")

a=int(input("Enter the day: "))
b=int(input("Enter the month: "))
c=int(input("Enter the year: "))

tp1=(a, b, c)

print(f"Here is your complete date's tuple: {tp1}")

yeardiff=tp[3]-tp1[3]
daydiff=tp[3]-tp1[3]
monthdiff=tp[3]-tp1[3]
