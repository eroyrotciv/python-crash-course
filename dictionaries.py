"""
# defining a dictionary
alien0 = {'color': 'green', 'points': 5}

# adding to a dictionary
alien0['x_position'] = 0
alien0['y_position'] = 25

print(alien0)

# defining an empty dictionary then adding 
alien1 = {}
alien1['color'] = 'red'
alien1['points'] = 10
alien1['x_position'] = 10
alien1['y_position'] = 30
print(alien1)

# modifying values in a dictionary
print(f"The alien is {alien0['color']}.")
alien0['color'] = 'yellow'
print(f"The alien is now {alien0['color']}.")

alien2 = {'x_position': 0, 'y_position': 0, 'speed': 'medium'}
print(f"The original position: {alien2['x_position']}")

# move the alien to the right.
# determine how far to move the alien based on its speed
if alien2['speed'] == 'slow':
    x_increment = 1
elif alien2['speed'] == 'medium':
    x_increment = 2
else:
    # alien must be fast
    x_increment = 3

# new position is old position plus the increment dependent on speed
alien2['x_position'] = alien2['x_position'] + x_increment

print(f"New position: {alien2['x_position']}")

# removing key-value pairs form a dictionary
del alien2['speed']
print(alien2)

# using a dictionary of similar objects
fav_country = {
    'victor' : 'japan',
    'stephanie' : 'greece',
    'tyler' : 'korea',
    'michael' : 'mexico',
}
country = fav_country['victor']
print(f"Victor's favorite country is {country}.")

# if you try to access a key that doesn't exist, you'll get an error
# instead you can use the get() method 
# get(argument 1 is a key, (optional) argument 2 is the default value returned  
    # if the requested key doesn't exist)
speed = alien0.get('speed', 'This alien doesn\'t have a speed')
print(speed)

# if a key exist though, get() will return the value
x_position = alien1.get('x_position', 'This alien doesn\'nt have an x position')
print(x_position)

# if the optional 2nd get() argument is omitted, a value of None is returned
speed = alien2.get('speed')
print(speed)
"""
# creating a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# calling a value from a dictionary via the key
add_points = alien_0['points']
print(f"You just earned {add_points} points.")

# adding new key-value pairs to an existing dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# creating a new dictionary
fav_food = {'vegetable': 'peas', 'fruit': 'apple', 'berry': 'blueberry', 
            'meat': 'chicken', 'drink': 'water'}
print(fav_food)

# adding new key-value pairs to dictionary
fav_food['dessert'] = 'yellow cake'
print(fav_food)

# creating an empty dictionary and then adding new key-value pairs to it
victor = {}
victor['age'] = 31
victor['height'] = 71
victor['sex'] = 'hell yeah'
print(victor)

# modifying a value in a dictionary is similar to adding new values, except
# you specify an existing key
victor['sex'] = 'male'
print(victor['sex'])

alien_1 = {'x_position' : 0, 'y_position': 25, 'speed': 'medium'}
print(f"The original x-position is {alien_1['x_position']}.")

# Move the alien to the right
# Determines how far to move the alien based on the speed
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # Alien must be fast
    x_increment = 3

# calculate new x_position based on speed. Old position plus increment
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"The new x-position is {alien_1['x_position']} because the alien moves"
      f" at a {alien_1['speed']} pace.")

# varifying that a variable created in an if clause is a global variable
print(x_increment)

print(f"The original x-position is {alien_1['x_position']}.")

alien_1['speed'] = 'fast'
# Move the alien to the right
# Determines how far to move the alien based on the speed
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # Alien must be fast
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"The aliens newest position is {alien_1['x_position']}.")

# removing key-value pairs using del statement
print(alien_0)
del alien_0['points']
print(alien_0)

# using a dictionary to store one kind of information about different objects
fav_games = {
    'victor': 'apex',
    'michael': 'elden ring',
    'tyler': 'bg3',
    'stephanie': 'sims',
}

game = fav_games['michael'].title()
print(f"Michael's favorite game is {game}.")

# if you try to access a key-value pair that doesn't exist, you'll get an error
#print(fav_games['mom']) # key 'mom' doesn't exist, KeyError: 'mom' is present

# using get() to access values, an optional value can be passed to output 
# a default if the key requested doens't exist
game = fav_games.get('mom', 'Fave game doesn\'t exist!')
print(game)
game = fav_games.get('tyler', 'Fave game doesn\'t exist.')
print(game)

# if optional argument isn't passed, get() returns special value None
game = fav_games.get('dad')
print(game)

