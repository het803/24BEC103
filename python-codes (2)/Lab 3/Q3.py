def substringcheker(x, y):
    if y in x:
        return True
    elif x in y:
        return True
    else:
        return False

str1 = str(input("Enter a string: "))
str2 = str(input("Enter another string: "))
print(substringcheker(str1, str2)) 