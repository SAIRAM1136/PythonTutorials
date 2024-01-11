a={101:'x',102:'y',103:'z'}
print(a)

#access items from dict
mydic={"brand":"Hyndai","model":"verna","year":2022}
print(mydic["model"])

#using get()
print(mydic.get("year"))

print(mydic)
#Change values in a dict
mydic["year"]=2023
print(mydic)

#read all keys and values using loop
for i in mydic:
    print(i) # it prints only keys from dict
for i in mydic:
    print(mydic[i]) #it prints only values from dict
        #or
for i in mydic.values():
    print(i)

#print keys along with values
for x,y in mydic.items():
    print(x,y)

#To check key is exists or not
if "brand" in mydic:
    print("exists")
else:
    print("not exists")

#Find number of items in dict
print(len(mydic))

#Adding items in dict
mydic["color"]="white"
print(mydic)

#remove item from dict
# mydic.pop("color")
# print(mydic)
        #or
del mydic["color"]
print(mydic)



