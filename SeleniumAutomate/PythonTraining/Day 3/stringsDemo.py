#these are different ways to create a String variable
s="welcome"
s=str('welcome')

#variable with no string / empty strings
name = str()

#****** MUTABLE & IMMUTABLE ********

#Mutable means cannot change the value of the variable
#Immutable means can change the value of the variable

str1="welcome"
print(id(str1)) #1857977236096
print(str1)

str1=str1+"Python"
print(id(str1)) #2657336353328
print(str1)


#How to use + & * with string
str1="Welcome"
print(str1+''+'Python')
print(str1*2)

#slicing : []
s='Welcome Python'
print(s[2:7])
print(s[:8])
print(s[5:])

#giving negative it will be removed the characters from the last
print(s[2:-5])

#ord() and chr()
#ord : ASCII number of the given character
print(ord('S'))

#chr() : ASCII Character of the given number.
print(chr(83))


#Max,min and len functions in the string
n='Sai'
print(max(n))
print(min(n))
print(len(n))

#in notin returns always true or false
x = "Python"
print("thon" in x)
print("sai" not in x)


#Reverse String
#method 1
str1 = "WelcomePython"
rev_str1 = ''
for i in str1:
    rev_str1=i+rev_str1
print(rev_str1)

#Method2
str2='SaiRamBeecharaju'
rev_str2=str2[::-1]
print(rev_str2)


