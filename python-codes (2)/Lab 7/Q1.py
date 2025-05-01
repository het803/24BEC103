dict1={1:1, 2:2, 3:3}
dict2={4:4, 5:5, 6:6}
dict3={7:7, 8:8, 9:9}

def concDict(d1, d2, d3):
    dict4={}
    dict4.update(d1)
    dict4.update(d2)
    dict4.update(d3)
    #dict4={**d1, **d2, **d3}
    print(f"Here is your complete 4th dict. after cont.: {dict4}")

print(f"Here is dict. 1: {dict1}")
print(f"Here is dict. 2: {dict2}")
print(f"Here is dict. 3: {dict3}")

concDict(dict1, dict2, dict3)
