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

