# Print all the alphabates in upper case and lower case

a=65

print("Alphabates in uppercase:")
for i in range(0, 26):
    print(chr(a+i))
else:
    a=97

print("Alphabates in lowercase:")
for i in range(0, 26):
    print(chr(a+i))
 
