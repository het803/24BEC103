d1={}

a=str(input("Do you wish to enter the values in the dict.? (yes/no): "))

if(a=="yes"):
    b=int(input("Enter the number of values you want to enter: "))
    c=str(input("Do you want to enter strings (str) or integers (int): "))
    for i in range(0, b):
        if(c=="int"):
            temp=int(input(f"Enter {i+1} value: "))
            dtemp={i:temp}
        else:
            temp=str(input(f"Enter {i+1} value: "))
            dtemp={i:f"{temp}"}
        d1.update(dtemp)

if(len(d1)==0):
    print("It is empty!")
else:
    print(f"It is not empty! And has a length of {len(d1)}, where dict.: {d1}")
