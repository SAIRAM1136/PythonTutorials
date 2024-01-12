import sys
sys.path.append("C:/Users/saira/PycharmProjects/SeleniumAutomate/PythonTraining/Day8/PackA")
sys.path.append("C:/Users/saira/PycharmProjects/SeleniumAutomate/PythonTraining/Day8/PackB")

# import Emp
# emp=Emp.Employee(102,'Scott',30000)
# emp.displayemp()
#
# import Stu
# stu=Stu.Student(103,'John','A')
# stu.displaystu()


from Emp import *
from Stu import *

emp= Employee(102,'Scott',30000)
emp.displayemp()

stu=Student(103,'John','A')
stu.displaystu()