#Example : create a class
# class Myclass:
#     def myFunc(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mc1=Myclass() #Create an Object
#
# mc1.myFunc()
# mc1.display("Smith")

#Example 2:
# class myClass:
#     def m1(self):
#         print("This is Instance method")
#     @staticmethod # Annotation
#     def m2(self, number):
#         print(self,number)
#
# mc=myClass() #Object creation
# mc.m1()
# myClass.m2(50,100)

#Example 3: creation of class variable and Access
# class Myclass:
#     a,b=10,20            #Class Variables
#     def add(self):
#         print(self.a+self.b)
#     def multiply(self):
#         print(self.a*self.b)
# mc=Myclass()
# mc.add()
# mc.multiply()

#Example 4 : Creation of global, local, class variable and access
# i,j = 15,20                         #Global variables
# class Myclass:
#     a,b = 10,20                     #class Variables
#     def add(self,x,y):              #Local Variables (x,y)
#         print(x+y)
#         print(i+j)
#         print(self.a+self.b)
# mc=Myclass()
# mc.add(1,2)

#Example 5 : same variable names
# a,b = 15,20
# class Myclass:
#     a,b = 10,20
#     def add(self,a,b):
#         print(a+b)                            #Local
#         print(self.a+self.b)                  #Class
#         print(globals()['a']+globals()['b'])  #global
#
# mc=Myclass()
# mc.add(1,2)

#Example 6: 1 class multiple object

# class Myclass:
#     def display(self,name):
#         print("Hello")
#         print(name)
#
# obj1=Myclass()
# obj1.display("John")
#
# obj2=Myclass()
# obj1.display("Smith")

#Example 7: Constructor exampple
#
# class Myclass:
#     def __init__(self):
#         print("This is Constructor")
#     def m1(self):
#         print("This is Method")
#     def m2(self,x,y):
#         return(x+y)
#
# mc=Myclass() #invoke constructor automatically
# mc.m1()      # Method we need to call explicitly by using method
# print(mc.m2(10,20))

# class myclass:
#     name ='john'
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# mc=myclass('David')

#***********************************Example*********************************
class Emp:

    def __init__(self, eid, ename,sal):
        self.eid = eid
        self.ename = ename            #converting class variables into local variables
        self.sal = sal
    def display(self) -> object:
        print(self.eid, self.ename, self.sal)

e1=Emp(1024,'John',20000)
e1.display()

e2=Emp(1025,'Smith',30000)
e2.display()















