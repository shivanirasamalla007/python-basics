# example :
# coordinates = ("x", "y")
# my_tuple = (10,20,30)
# print(my_tuple)
# print(type(my_tuple))

# creating a tuple :
# Empty tuple 
# Et = ()
# # tuple with numbers : 
# N = (1,2,3,4,5,6)
# # tuple with mixed datatypes 
# M = (24,3,14,"A","C",True, "False")
# # tuple with single element :
# a = 10 # Int
# print(type(a))
# b = [10] #List
# print(type(b))
# c = (10,) # Tuple
# print(type(c))
# my_tuple = (10,20,30)
# print(my_tuple)
# print(type(my_tuple))

# Accessing Elements :
# Tuple uses index values to access an element :
# a = (10,20,30,40)
#1    0  1  2  3
#-1  -4 -3 -2 -1 
# print(a[0]) #10
# print(a[1]) # 20
# print(a[2]) #30
# print(a[3]) #40
# print(a[-1]) #40
# print(a[-2]) #30
# print(a[-3]) #20
# print(a[-4]) #10 
# a = (10,20,30,40)
# #1    0  1  2  3
# #-1  -4 -3 -2  -1
# print(a[1:3]) # 20 30
# print(a[:2]) # 10 20
# print(a[-3:-1])  # 20 30 

# changing the value :
# A[1]=50 
# print(A) #TypeError : 'tuple' object does not support item assignment 
# # append():
# A.append(50)
# print(A)

# sorting and reversing :