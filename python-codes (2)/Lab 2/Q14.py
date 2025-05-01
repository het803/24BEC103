def pass_or_fail(s1,s2,s3):
    if s1<=39 or s2 <= 39 or s3 <= 39:
        return "Fail"
    return "Pass"
def assign_grade(grade):
    if grade <= 100 and grade>=80:
        return 'O'
    elif grade>= 79:
        return 'A+'
    elif grade >= 69: 
        return 'A'
    elif grade >= 59 and grade >= 55:
        return 'B+'
    elif grade >= 54 and grade >= 50:
        return 'B'
    elif grade >= 49 and grade >= 45:
        return 'C' 
    elif grade >= 44 and grade >= 40:
        return 'P'
    elif grade >= 39 and grade >= 0:
        return 'F'  

s1 = int(input("Enter subject 1 marks: "))
s2 = int(input("Enter subject 2 marks: "))
s3 = int(input("Enter subject 3 marks: "))

total = s1+s2+s3
avg = total/3
s1G = assign_grade(s1)
s2G = assign_grade(s2)
s3G = assign_grade(s2)

print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Result: {pass_or_fail(s1,s2,s3)}")
print(f"Subject 1 : Grade: {s1G}")
print(f"Subject 2 : Grade: {s2G}")
print(f"Subject 3 : Grade: {s3G}")