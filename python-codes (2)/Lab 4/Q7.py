def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

def ncr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def npr(n, r):
    return fact(n) // fact(n - r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"nCr({n}, {r}) = {ncr(n, r)}")
print(f"nPr({n}, {r}) = {npr(n, r)}")