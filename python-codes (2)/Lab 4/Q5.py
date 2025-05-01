def triplets(n):
    triplets = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= n:
                triplets.append((a, b, int(c)))
    return triplets

n = 30
b = triplets(n)
for triplet in b:
    print(triplet)