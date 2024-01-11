# # if, if else, elif

# #print a person is eligible to vote or not
#eligibility criteria age>=18

age = int(input('Enter your age: '))
if age >= 18:
    print("Eligible for Vote")
else:
    print("Not Eligible for Vote")

print("********************************************************")

# #Find a number is even or odd
num = int(input('Enter the number: '))
if num%2==0:
    print("Given number is even")
else:
    print("Given number is odd")

print("********************************************************")

#terinary operator
num = int(input('Enter the number: '))
print("Even Number") if num%2==0 else print("odd number")

print("********************************************************")

# #Multiple conditions using elif
# #Program to display day based on given number

Dayno = int(input('Enter the Number : '))
if Dayno==0:
    print("Sunday")
elif Dayno==1:
    print("Monday")
elif Dayno==2:
    print("Tuesday")
elif Dayno==3:
    print("Wednesday")
elif Dayno==4:
    print("Thursday")
elif Dayno==5:
    print("Friday")
elif Dayno==6:
    print("Saturday")
elif Dayno==7:
    print("Sunday")
else:
    print("Invalid")

print("********************************************************")

#Write a Program to check given number is positive or negative
x = int(input('Enter the number : '))
if x>0:
    print("The number is Positive")
else:
    print("The number is Negative")

print("********************************************************")

#Write a Program to check Largest of 2 numbers

m = int(input('Enter the number : '))
if m>50:
    print("The number is Largest")
else:
    print("The number is Smallest")

print("********************************************************")

#Print week number if user provided weekname

Dayname = input('Enter the weekname : ')
if Dayname=='sunday':
    print(0)
elif Dayname=='Monday':
    print(1)
elif Dayname=="Tuesday":
    print(2)
elif Dayname=="wednesday":
    print(3)
elif Dayname=="Thursday":
    print(4)
elif Dayname=="Friday":
    print(5)
elif Dayname=="Saturday":
    print(6)
elif Dayname=="Sunday":
    print(7)
else:
    print("Invalid weekname")

#Write a Program to assign grades to a students as per Marks

studentMarks = int(input("Enter Marks : "))
if studentMarks >90:
    print("A Grade Student")
elif studentMarks >80:
    print("B Grade")
elif studentMarks >50:
    print("C Grade")
else:
    print("Student is Failed")









