thislist = ["Apple","Grapes","Mangoes","Pineaple","Banana","Cherry"]
print(thislist)
# printing grapes
print(thislist[1])
print(thislist[3])
print(thislist[5])

# negative indexing
print(thislist[-1])
print(thislist[-6])
#slicing items in a list
print(thislist[1:4])
print(thislist[-1:-4])

print("===========")
# accessing list items using for loop
for fruit in thislist:
    print(fruit)
# printing the number of items in a list
no_items = len(thislist)
print("The number of fruits in the list:",no_items)

print("============")
# getting the number of items using the len
for i  in range (no_items):
    if i %2 == 1:
         print("Item at position {} is {}".format(i,thislist[i]))