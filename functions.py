def sumtwonumbers(a,b):

    c = a+b
    print("Result is :",c)
#function call
sumtwonumbers(7,8)
sumtwonumbers(17,20)
sumtwonumbers(10000000000,2456376583888)
sumtwonumbers(56.387602,564784)
sumtwonumbers(0.00000245,-26575748)
print("=============================")

# write a function called multiplythreenos,
# that multiply any given numbers and returns the result
# call the function atlest 7 times


def multiplythreenumbers(a,b,c):
    d = a*b*c
    print("Result is :",d)
#function call
multiplythreenumbers(5,4,6)
multiplythreenumbers(789,342,876 )
multiplythreenumbers( 12,34,76)
multiplythreenumbers(13,89,90)
multiplythreenumbers(32,45,67)
multiplythreenumbers(10,14,78)
multiplythreenumbers(12,87,67)

# creat  a function call is  getvolumeofcylinder that accepts radius and height
# use this function to find the volume of the following
# r - 14, h-100
# r - 44, h-0
# r - 28, h-05
# r - 30, h-9

def getvolumeofcylinder (r,h):
    pie = 3.142
    volume = pie * pow(r,2)*h
    print("Result is :",volume)
getvolumeofcylinder(14,100)
getvolumeofcylinder(44,0)
getvolumeofcylinder(28,5)
getvolumeofcylinder(30,9)

# stair case example
print("==============")
for i in range (10):
 print(i*"x")

 for i in range (15):
    print(*i,"x")

