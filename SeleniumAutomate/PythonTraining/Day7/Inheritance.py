#Single Inheritance
#Example 1
# class A:
#     def m1(self):
#         print("This is M1 Method from Class A")
# class B(A):
#     def m2(self):
#         print("This is M2 Method from Class B")
#
# obj=B()
# obj.m1()
# obj.m2()

#Example 2
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a+self.b)
# obj=B()
# obj.m1()
# obj.m2()

#MULTI_LEVEL INHERITANCE
# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()

#HiERARCHY INHERITANCE
# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# obj=B()
# obj.m2()
# obj.m1()
#
# obj1=C()
# obj1.m1()
# obj1.m3()

#MULTIPLE INHERITANCE
# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x+self.y)
# class B:
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# obj1=C()
# obj1.m1()
# obj1.m2()
# obj1.m3()

#METHOD OVERRIDING : Same method name using in Parent class and child class
# class A:
#     def m1(self):
#         print("This is Method of m1 from class A")
# class B(A):
#     def m1(self):
#         print("This is Method of m1 from class B")
#         super().m1()                            #Calling parent class method through Child class using super keyword
#
# obj= B()
# obj.m1()

#Example 7:
# class A:
#     a,b=10,20
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)           #Local Variables
#         print(self.i+self.j) #Class Variables
#         print(self.a+self.b) #Class Variables
#
# obj=B()
# obj.m(5,3)

#Overriding Variables
# class Parent:
#     name="Scott"
# class Child(Parent):
#     name="John"       #Overriding the variable value
#
# obj=Child()
# print(obj.name)

#Overriding Methods
# class Bank:
#     def rateOfIntrest(self):
#         return 0
# class X(Bank):
#     def rateOfIntrest(self):
#         return 10
# class Y(Bank):
#     def rateOfIntrest(self):
#         return 12
#
# obj=X()
# print(obj.rateOfIntrest())
#
# obj=Y()
# print(obj.rateOfIntrest())

#METHOD OVERLOADING (POLYMORPHISM) 1:
# class Human:
#     def sayHello(self,name=None):
#         if name is not None:
#             print("Hello " + name)
#         else:
#             print("Hello")
#
# h=Human()
# h.sayHello()
# h.sayHello("Smith")

#METHOD OVERLOADING (POLYMORPHISM) 2:
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
c=Calculation()
c.add()
c.add(10,20)
c.add(100,200,300)



















































