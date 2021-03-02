studentList =[]
totalNoOfStuds = int(input("Enter total number of students"))
index = 0
iterate = range(index,totalNoOfStuds)

for current in enumerate(iterate):
    student ={}
    student['name'] = input("Enter Student Name :")
    student['age'] = input("Enter Age :")
    studentList.append(student)

print(studentList)