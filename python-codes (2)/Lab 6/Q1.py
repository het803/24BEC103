def tup(lis):
    boys = 0
    girls = 0

    for name in lis:
        if isinstance(name, tuple):
            boys += 1
        else:
            girls += 1

    return boys, girls

names = [("Maharshi",), "Krishan", ("Soham",), "Shivam", ("Yagna",), "Darshil"] 
boys, girls = tup(names)
print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")
