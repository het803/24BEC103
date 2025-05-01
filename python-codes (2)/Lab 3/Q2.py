def upperkar(x):
    result = ''
    for char in x:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def lowerkar(x):
    result = ''
    for char in x:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def togglekar(x):
    result = ''
    for char in x:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

a = str(input("Enter a string: "))
print("Here is your string: ", a)
print(f"Here is Upper case: {upperkar(a)}")
print(f"Here is Lower case: {lowerkar(a)}")
print(f"Here is Toggle case: {togglekar(a)}")