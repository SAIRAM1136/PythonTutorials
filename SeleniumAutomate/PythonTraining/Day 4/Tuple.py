x=('John','Smith','jack')
print(x)
print(type(x))

#to access tuple items
x=('John','Smith','jack')
print(x[0])

#range of tuple
x=('John','Smith','jack','harry','max','warn')
print(x[2:5])

#Changing Tuple values : it cannot possible to change but there is work around
# firstly, tuple is conevrted into list , change values and again convert to tuple
x=('John','Smith','jack')
a=list(x) #converted to list

a[2]="warner" #added value
print(a)

x=tuple(a) #converted to tuple
print(x)

#Print all tuple items using loop
x=('John','Smith','jack','harry','max','warn')
for i in x:
    print(i)

#Check item is present in the tuple or not
x=('John','Smith','jack','harry','max','warn')
if 'harry' in x:
    print('Present')
else:
    print('Not present')


