vehicledict = {
    "name":"BMW",
    "model":"x6",
    "year":"2014",
    "color":"silver",
    "price":12345678.5678,
    "issold":False
}
print(vehicledict)
# getting the model
print(vehicledict["model"])
print(vehicledict["issold"])

print("==============")
#printing key names in a dictionary
for keyname in vehicledict:
    print(keyname)



# printing values in a dictionary
print("=============")
for value in vehicledict.values():
    print(value)

# printing the values together
for keynames,values in vehicledict.items():
    print(keynames,values)
