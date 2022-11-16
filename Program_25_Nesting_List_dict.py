#we will do nesting in this program
aliens = []
for alien_no in range(20):
    new_alien = {'color':'green', 'point':5,}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
# We are changing the colors of first three aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'Yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
for alien in aliens[:5]:
    print(alien)