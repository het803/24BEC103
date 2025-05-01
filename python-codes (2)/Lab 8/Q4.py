s = {"Aayushi", "arnav", "Aryan", "aashi", "Bhavya", "babubhai", "Beeingan", "bahubali"}
a = set()
b = set()

for i in s:
    if i.startswith("A") or i.startswith("a"):
        a.add(i)
    elif i.startswith("B") or i.startswith("b"):
        b.add(i)

print(f"All the names = {s}")
print(f"Names that starts with A or a = {a}")
print(f"Names that starts with B or b = {b}")