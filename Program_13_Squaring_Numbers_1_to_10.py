#creating list of numbers
#This Program simmple done  
My_List = list(range(1,10))
Squared_List = []
for i in range(1, 10):
    i = i**2
    Squared_List.append(i)
print(Squared_List)
#This Program using list comprehensions
My_List = list(range(1,10))
print(My_List)
Squared_List = [i**2 for i in My_List]
print(Squared_List)

#More List comprehension using
My_List = [i**2 for i in range(1, 10)]
print(My_List)