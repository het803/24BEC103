# Count number of alphabates and number of digits in any given string

a=str(input("Enter your text: "))
char=0
num=0

for i in range(0, len(a)):
    if(ord(a[i])>=65 and ord(a[i])<=90):
        char+=1
    elif(ord(a[i])>=97 and ord(a[i])<=122):
        char+=1
    elif(ord(a[i])>=48 and ord(a[i])<=57):
        num+=1

print(f"Your string, which is: {a}; has {char} alphabates and {num} digits.")
