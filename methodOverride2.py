#To Avoid Method Overriding

class classA():

    def methodA(self):
        print("Hello from Class A")

class classB(classA):
    def methodB(self):
        super().methodA()
        print("Hello from Class B")

obj = classB()
obj.methodA()
obj.methodB()

