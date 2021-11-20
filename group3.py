students = ["alice","mike","virginia"]
for student in  reversed(students):
    print(list(reversed(students)))
    break

cupdated = []
no = len(students)
for i in range(no):
    current = no-i-1
    cupdated.append(students[current])
print(cupdated)