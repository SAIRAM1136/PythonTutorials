# lang = input("Please enter Programming Language : ")
# #Elif Condition
# #lang = "Python"
# if lang == "Selenium":
#     print("Lang is Matched")
# elif lang == "Java":
#     print("Lang is Matched")
# elif lang == "Python":
#     print("Lang Found")
# else:
#     print("Not Found")

#Nested If
salary = input("Please Enter the Salary : ")
#Typecasting : Converting datatype
sal = int(salary)
if sal>40000:
    print("Eligible for car loan")
    if sal>80000:
        print("Eligible for Home Loan")
        if sal>100000:
            print("Eligible for all kind of Loans")
else:
    print("Not Eligible for any Kind of Loans")




