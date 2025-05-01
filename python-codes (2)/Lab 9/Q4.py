ls=["madam", "Python", "malayalam", 12321]

palindroms=list(filter(lambda n:str(n)[::-1]==str(n), ls))

print(f"Here is original list: {ls}\nHere is list of Palindroms: {palindroms}")
