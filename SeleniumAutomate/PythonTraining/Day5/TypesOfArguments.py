def fun(i,j):
    print(i,j)
fun(10,20)  #Positional arguments
fun(j=25,i=85)   #keyword arguments

#Example 2: default values assigned to positinal arguments
def fun(i,j=20):
    print(i,j)
fun(10)

#Example 3: Keyword arguments
def func(name, greetmessage):
    print(greetmessage+" "+name)
func("John","Good Morning")

#Example 4 : Combine Positinal & keyword argms
def my_func(a,b,c):
    print(a,b,c)
my_func(10,20,30) #positional
my_func(a=10, b=20,c=30) #keyword
my_func(10,20,c=30) #Combination
#my_func(10,b=20,30) #positional arguments must be appear before keyword argument

#Example 5:
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(10,20))
print(type(largest(10,20)))



