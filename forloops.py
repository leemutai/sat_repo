fruits = ["Apple","Mango","Banana","Berry","Water Melon"]7
students = ["Brian","Sharon","Brenda","Victor","Mickey"]
for fruit in fruits:
    print(fruit)
print("======")
for  student in students:
    print(students)

# assign a student a fruit
#print("I have given {} an {}".format(students[0],fruits[0]) )

nu_students = len(students)

# for stu in students:
#   print("Ihave given {}".format(students[i]))

for i in range (nu_students):
    print("I have given {} a {}".format(students[i],fruits[i]))


# assign students their marks
marks = [45,67,89,76,89,100,54,68]
names = ["Joy","Paula","Rachael","Trizah","Moses","Brian","Bently","Wayne"]

# ssign students their respective marks in this formart:
# Joy : 45

no = len(names)
for i in range (no):
    print("{} : {}".format(names[i],marks[i]))
