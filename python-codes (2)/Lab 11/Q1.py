while True:
    try:
        num = int(input("Enter an integer: "))
        break                       # exit loop if conversion succeeds
    except ValueError:
        print("Error: please enter a valid integer.\n")

print(f"You entered {num}.")
