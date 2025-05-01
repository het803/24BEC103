studs = []
total = int(input("Enter the number of students: "))
for _ in range(total):
	student = tuple(input("Enter roll no, name, age: ").split())
	studs.append(student)

rolls = [student[0] for student in studs]
names = [student[1] for student in studs]
ages = [student[2] for student in studs]

print("Roll Numbers:", rolls)
print("Names:", names)
print("Ages:", ages)