#create a user's information dictionary
users = {
    'username':'musadaqtanver',
    'first':'Musadaq',
    'last':'Tanvir',
}
for key, value in users.items():
    print(key,"\t",value)
    
print("<<<<<<<<<<<<<<<<<<<--------------------------------------------->>>>>>>>>>")
#This type of looping provides both keys and values at a time respectively to first and second variable. 
students = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
}

for name, languages in students.items():
    print(f"{name.title()}'s favourite Language is {languages.title()}")


print("<<<<<<<<<<<<<<<<<<<--------------------------------------------->>>>>>>>>>")
#Now we will just loop through the keys of dictionaries not values 
for name in students.keys(): # Same as if we write default for loop
    print(name) 
    
print("<<<<<<<<<<<<<<<<<<<--------------------------------------------->>>>>>>>>>")
# Lets apply some conditions via loop to dictionary
friends = ['jen', 'sarah']
for name in students:
    print(name)
    if name in friends:
        print(f"{name} Glad to know you like {students[name].title()}")    

print("<<<<<<<<<<<<<<<<<<<--------------------------------------------->>>>>>>>>>")
# Looping through the sorted list of keys returned to for loop of dictionary

for name in sorted(students.keys()):
    print(name)

print("<<<<<<<<<<<<<<<<<<<--------------------------------------------->>>>>>>>>>")
#If we want just values from the dictionary
for values in students.values():
    print(values)

print("<<<<<<<<<<<<<<<<<<<--------------------------------------------->>>>>>>>>>")
#if we want to know the values without repeatation we can use set method
for value in set(students.values()):
    print(value)