def vowelskitne(x):
    vowels = "AaEeIiOoUu"
    count = 0
    for char in x:
        if char in vowels:
            count += 1
    return count

a = str(input("Enter a string: "))
b = vowelskitne(a)
print(f"The number of vowels in the string is: {b}")