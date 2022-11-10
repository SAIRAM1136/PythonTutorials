#Single Level Inheritance

class Base:
    name="Mukesh"
    def baseMethod(self):
        print("I am in BaseClass")

#Child class inherting Base class
class Child(Base):
    company = "Automation"
    def childMethod(self):
        print("I am in ChildClass")

#Object of ChildClass

c=Child()
c.childMethod()
c.baseMethod()
print(c.name)
print(c.company)