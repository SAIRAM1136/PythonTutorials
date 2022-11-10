class classA():

    def methodA(self):
        print("Hello")

class classB(classA):

#Method Overriding
    def methodA(self):
        print("Hello")

obj = classB()
obj.methodA()
