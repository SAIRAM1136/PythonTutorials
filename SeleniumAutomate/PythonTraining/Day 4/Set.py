x={1,2,3,4,5}
print(x)

x={"java","python","javascript","c"}
print(x)

#Accessing items from Set
x={"java","python","javascript","c"}
for i in x:
    print(i)

#Value exists in set or not
x={"java","python","javascript","c"}
print("python" in x)

#Add new items in a set : add()-Single item & update()-mutliple items
x={"java","python","javascript","c"}
x.add("ruby")
print(x)

x.update(["c#", "nodesjs", "selenium"])
print(x)

#Find length of a set
x={'selenium', 'ruby', 'c#', 'python', 'nodesjs', 'c', 'javascript', 'java'}
print(len(x))

#to remove a item
x.remove("selenium")
print(x)

#to clear all items from the set
x.clear()
print(x)

#joining 2 sets using union ()
set1 ={'a','b','c'}
set2 ={1,2,3}
set3= set1.union(set2)
print(set3)