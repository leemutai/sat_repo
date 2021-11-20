# request for number of students
nu_students = int(input("How many students do you want to find average for?:"))
marks = []
for i in range (nu_students):
    studentmark = float(input("Please enter marks for student {}:".format(i+1)))
    marks .append (studentmark)

nu_students = len(marks)
sum = 0
for i in range (nu_students):
    sum+=marks[i]
    print(marks[i])
average = sum/nu_students
print("average",average)

