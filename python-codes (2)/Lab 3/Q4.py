def removeSubstring(x, y):
    return x.replace(y, '')

a = str(input("Enter a string: "))
b = str(input("Enter a substring to remove: "))
res = removeSubstring(a, b)
print(res) 