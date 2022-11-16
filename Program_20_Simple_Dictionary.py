#creating the dictionary
Characters = {'color':'green', 'point':5}
print(Characters['color'],"\n", Characters['point'])

#Taking out the points value from the dictionary and printing it..
user_points = Characters['point']
print(f"You earned just {user_points}")

#Now we are going to add key value pairs into the dictionary dynammically..
Characters['x_coordinates'] = 0
Characters['y_coordinates'] = 25
print(Characters)

#This Whole process can be started from early empty dictionary as following..

character = {}
character['color'] = 'Red'
character['point'] = 10
print(character)

