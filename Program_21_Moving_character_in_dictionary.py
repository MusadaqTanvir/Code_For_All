#First of all create the dictionary 
Alien = {}
#Assign values to the Alien
Alien['color'] = 'Yellow'
Alien['point'] = 10
Alien['x_coordinate'] = 0
Alien['y_coordinate'] = 25 
Alien['speed'] = 'medium'
print("The Original Character\n", Alien)
x_increment = 0
#Now Move the Alien in the game on the screen along x-axis
if Alien['speed'] == 'slow':
    x_increment = x_increment + 1
elif Alien['speed'] == 'medium':
    x_increment = x_increment+ 2
else:
    x_increment = x_increment + 3
Alien['x_coordinate'] = x_increment
print(Alien)

#Now if we want to remove the a key from the dictionary
del Alien['color']
print(Alien)
#removing the point again
del Alien['point']
print(Alien)

