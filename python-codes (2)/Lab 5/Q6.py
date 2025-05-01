def fc(f):
    return (f - 32) * 5.0/9.0

def lis(flist):
    return [fc(temp) for temp in flist]


flist = [29, 47, 57, 59, 10]
c = lis(flist)
print(c)
