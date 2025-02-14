# looping through all key-value pairs 

# new dictionary for user_0
user_0 = {
    'username': 'vyore',
    'first_name': 'victor',
    'last_name': 'yore',
}

# using a for loop to loop through a dictionary
for key, value in user_0.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value.title()}")

fave_game = {
    'victor': 'lies of p',
    'michael': 'elden ring',
    'stephanie': 'sims',
    'tyler': 'baulders gate 3',
    'aaron': 'apex',
    'chad': 'call of duty',
}

for name, game in fave_game.items():
    print(f"{name.title()}'s favorite video game is {game.title()}.")

# looping through all the keys in a dictionary using the .keys() method
for name in fave_game.keys():
    print(name.title())

# just looping through a dictionary is equivalent to looping through the keys
# the 2 statements below output exactly the same values
for name in fave_game:
    print(name.title())
for name in fave_game.keys():
    print(name.title())

fam = ['michael', 'stephanie', 'tyler', 'aaron']

for name in fave_game:
    if name in fam:
        print(f"What up fam, wanna play {fave_game[name].title()}?")
    elif name not in fam:
        print(f"What up {name.title()}? Wanna play some {fave_game[name].title()}?")
""" stoping the input portion of this snippet to test faster
# using .keys() method to see if a key exists
# list(dict) is equivalent to dict.keys()
if 'josh' not in fave_game.keys():
    fave_game['josh'] = input("Josh, what's your favorite game?")
if 'josh' in fave_game:
    print(f"Josh's favorite game is {fave_game['josh'].title()}.")
"""
# verifying there is no differences in the output from the 3 different statements
for key in fave_game:
    print(key)
for key in fave_game.keys():
    print(key)

# looping through a dictionary keys in a particular order
for name in sorted(fave_game):
    print(f"{name.title()}, do you want to play some {fave_game[name].title()}?")

# working w/ only the values in a dictionary using the .values() method
print(
    "\nGame values listed in the dictionary printed in alphabetical order:"
)
for value in sorted(fave_game.values()):
    print(value.title())

# printing dictionary in reversed order by passing optional reverse=True
print(
    "\nGame values listed in the dictionary printed in reverse alphabetical order:"
)
for value in sorted(fave_game.values(), reverse=True):
    print(value.title())

state_reside = {
    'victor': 'virginia',
    'stephanie': 'virginia',
    'michael': 'virginia',
    'michelle': 'north carolina',
    'aaron': 'florida',
    'josh': 'florida',
    'kim': 'new jersey',
}

# using the set() function to only list unique values in reverse alphabetical order
# .values() has to be specified, otherwise the keys are iterated through
print("\nI have family living in the following states: ")
for state in set(sorted(state_reside.values(), reverse=True)):
    print(state.title())

# using both the key and the value and using lambda to sort by the value 
# looping through a dictionary
print("\n")
for name, state in sorted(state_reside.items(), key=lambda x: x[1], reverse=True):
    print(f"{name.title()} lives in {state.title()}.")

# using lambda and both the key and the value in a loop to sort by the key
print("\n")
for name, state in sorted(state_reside.items(), key=lambda x: x[0], reverse=False):
    print(f"{name.title()} lives in {state.title()}.")

"""
# a set can be created similar to a dictionary, except there is not a key:.
# in a set, the values are just separated by a comma
set_fruits = {
    'apple', 'apple', 'pear', 'orange', 'banana', 'grape', 'banana', 'orange',
    'apple', 'tomato', 'dragonfruit',
}
print(sorted(set_fruits))

set_colors = {
    'orange', 'green', 'red', 'blue', 'purple', 'black', 'white', 'pink', 
}
# finds values that are in both sets colors and fruits
print("Values that are in both sets colors and fruits\n", set_colors & set_fruits)
# values in colors, but not in fruits
print("Values in colors, but not in fruits\n", set_colors - set_fruits)
# values that are in fruits, but not colors
print("Values that are in fruits, but not colors\n", set_fruits - set_colors)
# values in both colors or fruits
print("Values in both colors or fruits\n", set_colors | set_fruits)
# values that are in colors or fruits, but not in both
print("Values that are in colors or fruits, but not in both\n", set_colors ^ set_fruits)
"""