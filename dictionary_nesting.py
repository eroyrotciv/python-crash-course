import random

alien_0 = {'color': 'yellow', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'green', 'points': 15}

# creating a list of dictionaries
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# create an empty list to store aliens
game_aliens = []

# create 30 new random aliens
for alien_number in range(15):
    new_alien = random.choice(aliens)
    game_aliens.append(new_alien)

# show the first 5 aliens
print("\n")
for alien in game_aliens:
    print(alien)
print(f"Total number of aliens: {len(game_aliens)}!")

for alien in game_aliens:
    if alien['color'] == 'green':
        alien['speed'] = 'fast'
    elif alien['color'] == 'red':
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['speed'] = 'slow'

print("\n")
for alien in game_aliens:
    print(alien)

# a list in a dictionary
# store information about a pizza
pizza = {
    'crust': 'thin',
    'topping': ['mushrooms', 'onions', 'peppers']
}

print(
    f"You ordered a {pizza['crust']}-crust pizza, "
    "with the following toppings:"
)
for topping in pizza['topping']:
    print(f"{topping.title()}")

# storing a list of languages in a dictionary value
fave_languages = {
    'victor': ['swift', 'python'],
    'stephanie': ['swift', 'python', 'english'],
    'michael': ['ruby', 'michalien'],
    'tyler': ['python'],
    'mom': ['c+', 'go'],
    'dad': ['kobal', 'basic'],
}

for name, languages in fave_languages.items():
    print(f"{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")

