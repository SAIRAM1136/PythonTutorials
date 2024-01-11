#How to create a List
my_list=[1,2,3,4,5,6,7,8,9]
my_list1=['one','two','three','four']
my_list2=[1,'two','three',5,4]
my_list3=[]

print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)

#Accessing Items from the list
my_list4=['Java', 'Python', 'Ruby', 'c']
print(my_list4[2])

#Range of Indexes
my_list5=['one','two','three','java','python','ruby','c']
print(my_list5[2:5])


#How to change the item Value
x=['Java','c','c#']
x[2] = 'python'
print(x)

#read the values from list using for loop
my_list5=['one','two','three','java','python','ruby','c']
for i in my_list5:
    print(i)

#Check if the item is present in the list or not ** Important**
my_list5=['one','two','three','java','python','ruby','c']
if "python" in my_list5:
    print("Item is existing in the list")
else:
    print("Item is not")

#Find length of the list
my_list5=['one','two','three','java','python','ruby','c']
print(len(my_list5))

#add a new item in the list by using append or insert

#append : Append function will add new value in end of the list
my_list5=['one','two','three']
my_list5.append("python")
print(my_list5)

#insert : insert function will add new value in middle of the list by using index
my_list5=['one','two']
my_list5.insert(1,"python")
print(my_list5)

#how to remove a item from the list
my_list5 =['one','two','three','java','python','ruby','c']
my_list5.remove('ruby')
print(my_list5)

#How to remove item from list using index
#pop
my_list5 =['one','two','three','java','python','ruby','c']
my_list5.pop(2)
print(my_list5)

#del
my_list5 =['one','two','three','java','python','ruby','c']
del my_list5[0]
print(my_list5)

#clear
my_list5 =['one','two','three']
my_list5.clear()
print(my_list5)

#Copy one list to other
my_list5 =['one','two','three']
mylist6=list(my_list5)
print(mylist6)
print(my_list5)

#or
my_list5 =['one','two','three']
mylist6=my_list5.copy()
print(mylist6)

#Adding 2 lists
a=['a','b','c']
b=[1,2,3]
c=a+b
print(c)

#using loop statement
a=['a','b','c']
b=[1,2,3]

for i in b:
    a.append(i)
print(a)

#extend
a=['a','b','c']
b=[1,2,3]
a.extend(b)
print(a)













