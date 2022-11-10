emp = {"Qa":"Smith","Dev":"John","Devops":"William"}
# # print(emp)
# # # print(emp["Dev"])
# # # print(emp["Qa"])
# # print(emp.get("Dev"))

#List in Dict
# emp = {"Qa":["Smith","Rahul","David"],"Dev":"John","Devops":"William"}
# print(emp)
# print(emp["Qa"][2])

#Dict inside Dict
# emp ={"Qa":"Smith", "Dev":{"frontend":"John","backend":"william"}}
# print(emp["Qa"])
# print(emp["Dev"].get("frontend"))
# print(emp["Dev"]["frontend"])

#Add element into dict
emp["Manager"]="Jack"
print(emp)

# print(len(emp))
#
# print(emp.keys())
# print(emp.values())
# print(emp.items())

#delete 1 particular Key value pair
# del emp["Qa"]
# print(emp)

#Dict using Keyvalue pair

emp=dict(Qa = "Kane", Dev = "john", Devops = "william" )
print(emp)

#Dict using Tuple as List
emp=dict([(1,"Java"), (2,"Python"), (3, "JS")])
print(emp)