# list 1 of 1 to 6
ls1=[1,2,3,4,5,6]

# list 2 of 6 to 1
ls2=[6,5,4,3,2,1]

# adding corrresponding elemnts and getting the list
result=list(map(lambda a,b:a+b, ls1, ls2))

print(f"Here is list 1: {ls1}\nHere is list 2: {ls2}\nHere is addition of both lists' corresponding elements: {result}")
