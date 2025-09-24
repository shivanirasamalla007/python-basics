
# searching and checking 
# a = [1, 2, 3, 4, 5]-*+
# if 4 in a :
#     print("yes item is present")

# b = [1 , 2, 3, 4, 5]
# if 6 not in b :
#     print("yes item is not present ")
# index method
# a =[1, 2, 3, 4, 5]
# print(a.index(4)) #3
# count method
# # a= [1,1,2,2,3,3,4,4,5,5,6,6,7,7,7,7,7,7,8,8,9,9]
# # print(a.count(7))
# frnds = ["shiney", "rishi", "shivani"]
# frnd2 = frnds.copy()
# print(frnd2)
# frnd2.append("satyam")
# print(input("enter the multiple values : ")).split() # 10 20 30 40 50
# a = list(map(int,input("enter the multiple values : ").split())) # 10 20 30 40 50 
# print(a)
# using index with for loop :
# names = ["shivani", "naveena", "sravya"]
# a = len(names)
# for i in range (0,1):
# print("names", i, names[1])
# list1 = ["hardik pandiya","virat kohli","bhumra","siraj"]
# list2 = ["vdk","ram pothineni","vijay thalapathi","nani"]
# # for i in range (0,2):
# print(list1[0],list2[1])
# list1 = []
# n =int(input("enter the number of list values :"))
# for i in range (0,n):
#     a = input("enter the list values :")
#     list1.append(a)
#     print(list1)
    
# give the input values to the lists from 0 to 10 :
# list1 = []
# n = int(input("enter the number of list values :"))
# for i in range (n):
#       a = input("enter the values :")
#       print(list1)

# sum of list items = 10 20 30 40 50 without using sum().
# list1 = [ 10,20,30,40,50]
# sum = 0 #100
# for i in list1 : # 10 20 30 40 50 
#     sum = sum + i # 150 
#     print(sum)
# convert ["p","y","t","h","o","n"] to python
# list1 = ["y","t","h","o","n"]
# word = "p"
# for i in list1 : # y t h o n 
#     word = word + i 
#     print(word)
# find the maximum and minimum number without using max() and min() :
# list1 = [ 7,12,1,6,20,10,25,15]
# list1.sort()
# print(list1)
# print("maximum of list :", list1[7])
# print("minimum of list:", list1[0])
# searching for an element in list :
# names = ["shivani","naveena","sravya","suma"]
# searching_names = input("Enter the name to be found :")#shivani # naveena
# found = False 
# for i in names  :
    
#     if searching_names == i :
#         found = True 
# if found :
#     print("yes")
# else:
#     print("no")
# numbers = [ 1,2,3,4,5,6,7,8,9,10]
# o = 5
# e = 5
# even_count = 0 #2
# odd_count = 0  #1
# for i in range (len(numbers)) :
#     if numbers [i] %2 == 0:
#         even_count += 1
#     else :
#         odd_count += 1 
# print("number of even numbers are :", even_count)
# print("number of odd numbers are :", odd_count)
# list1 = [1,2,3,4,-1,-3,-4]
# #p = 4
# #n = 3
# for i in range (1,5):
#     print(i)
    
# numbers = [1,2,3,4,5,6,7,-1,-2,-3,-4]
# positive_list = []
# for i in range (len(numbers)) :
#     if numbers[i] > 0 :
#         positive_list.append(numbers[i])
# print(positive_list)
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# m = int(input("enter the number to be multipied: "))
# After_multiplication = []
# for i in numbers :
#     After_multiplication.append(i*m)
# print(After_multiplication)
        
    

