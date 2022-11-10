#Function without args
# def hellowold():
#     print("Python")
#     c=10+90
#     print(c)
#     print("Bye")
# hellowold()

#Function with args
# def sum(num1,num2):
#     result = num1+num2
#     return result
#
# a = sum(20,30)
# print(a)

#Function with default args
def sum(num1,num2,num3=0, num4=0):
    result = num1+num2+num3+num4
    return result

a = sum(20,30,70,80)
print(a)


#Example Program with even numbers using lists in Functions

def check_even_number(list1):

    even_number=[]
    odd_number=[]

    for x in list1:
        if x%2 ==0:
            even_number.append(x)
        else:
            pass
    return even_number
    # for x in list1:
    #     if x % 2 == 0:
    #         pass
    #     else:
    #         odd_number.append(x)
    #return odd_number
Result = check_even_number([1,2,3,4,5,6,7,8,9,10])
print(Result)