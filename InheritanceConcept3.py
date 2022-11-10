#Multiple Inheritance

class classA():

    def methodA(self):
        print("Welcome to CLass A")

    def Welcome(self):
        print("Welcome to Python World A")

class classB:

    def methodB(self):
        print("Welcome to Class B")

    def Welcome(self):
        print("Welcome to Python World B")


class classC(classA, classB):

    def methodC(self):
        print("Welcome to Class C")

obj1 = classC()

obj1.Welcome()

