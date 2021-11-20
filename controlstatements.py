a = 33
b = 200
if a>b:
    print("A is greater than b")
else:
    print("B is greater than a")

# grading system
marks = 45

if marks >= 70:
    print("Student grade: A")
elif marks >= 60:
    print("Student grade: B")

elif marks >= 50:
    print("Student grade: C")

elif marks >= 40:
    print("Student grade: D")
else:
    print("Student grade: F")

#Calculating bmi
#weight = int(input("Enter weight in kgs "))
#height = float(input("Enter your height in M "))
#bmi = weight/(height*height)
#print("OUR BMI IS:",bmi)


# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater
#if bmi >=30:
    #print("You are abese")
#elif bmi >25 and bmi<=29.9:
    #print("You are over weight")
#elif bmi >=18.5 and bmi<=24.9:
    #print("You have normal weight")
#else:
    #print("You are underweight")

#calculating odd or even
Number = int(input("Enter Number to test:"))
if Number%2 == 0:
    print("{} is Even".format(Number))
else:
    print("{} is odd".format(Number))

