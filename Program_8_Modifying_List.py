# We will Modify the List...
items = ['Dell','HP','Nokia','Vivo','Realme','Samsung','Google Pixel']
#Orignal list
print("Simple orignal list\n", items)
# We will Modify the first element of the list and adding another on the position of first element
items[0]='Lenovo'
print("Modified list by index method\n", items)
#Adding element to the list on the last index
items.append('Infinix')
#printing the modified list recently...
print("Modified list by append method\n", items)
#Adding value into the list on the desired location using insert() method
items.insert(0, 'Redme')
#printing the list...
print("Modified list by the insert method\n", items)

#Removing the values from the list using the del statement
#The Del statement is used when we know the location of an element that is going to be removed...
#For example we want to remove the Redme that is on the 0 index 
del items[0]
#printing the list..
print("Modified list using del statement\n", items)
#Removing element from the list using the pop() method..
poped_value = items.pop()
print("The Poped value" , poped_value)
print("Updated list after pop method\n", items)
#Removing the value by its index using pop() method..
items.pop(0)
print("After Removing first method\n", items)
#Removing the value from the list directly..
items.remove('Samsung')
print("After Removing Samsung directly\n", items)