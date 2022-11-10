class Person:

    def welcome(self):
        print("Hello Python")

    def Hello(self):
        print("Hello World")

    def sum(self, num1, num2):
        print(num1+num2)


p=Person()

p.Hello()
p.welcome()
p.sum(23,24)


#OBJECT WITH PROPERTIES
p.name="python"
p.version=3.9

print(p.name)