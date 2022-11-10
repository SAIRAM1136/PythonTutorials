#Multilevel Inheritance

class classA():

    def methodA(self):
        print("Welcome to CLass A")

    def Welcome(self):
        print("Welcome to Python World A")

class classB(classA):

    def methodB(self):
        print("Welcome to Class B")

    def Welcome(self):
        print("Welcome to Python World B")


class classC(classB):

    def methodC(self):
        print("Welcome to Class C")

    def Welcome(self):
        print("Welcome to Python World C")

obj1=classC()
obj1.methodC()
obj1.methodB()
obj1.methodA()
obj1.Welcome()

