tuple1=(1,"Python",90.01, True,1,1,1,'Qa')
# print(tuple1)
# print(tuple1[1])
# print(tuple1[-2])
# print(tuple1[::-1])
# print(tuple1.count(1))
# print(tuple1.index('Qa'))

# #Slicing
# print(tuple1[1:6])
#
# #Tuples  are immutable , we cannot update/modify the values, where as Lists are Mutable we can modify
#
# print(type(tuple1))

#we can convert Tuple into Lists and sets

L1 = list(tuple1)
S1 = set(tuple1)
print(type(L1))
print(type(S1))
print(L1)
print(S1)

