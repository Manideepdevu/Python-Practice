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

nameToFind = input("input the name to find the age")

for i,student in enumerate(studentList):
    if studentList[i]['name'] == nameToFind:
        print("age of the student",nameToFind,studentList[i]['age'])
        break