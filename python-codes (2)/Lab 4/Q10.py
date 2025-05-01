def fbseq(n):
    fbser = []
    a, b = 0, 1
    for _ in range(n):
        fbser.append(a)
        a, b = b, a + b
    return fbser

n = int (input("Enter the number of terms: "))
print(fbseq(n))