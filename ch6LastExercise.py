# creating 3 dictionaries of people w/ key-values being info about the person
lover = {
    'member': 'lover',
    'first_name': 'stephanie',
    'last_name': 'price',
    'age': 31,
    'city': 'chase city',
    'fav_color': 'green',
    'sex': 'female',
}
brother = {
    'member': 'brother',
    'first_name': 'michael',
    'last_name': 'yore',
    'age': 25,
    'city': 'chase city',
    'fav_color': 'black',
    'sex': 'male',
}
sister = {
    'member': 'sister',
    'first_name': 'michelle',
    'last_name': 'welch',
    'age': 45,
    'city': 'mt. airy',
    'fav_color': 'white',
    'sex': 'female',
}

# creating a list of family memebers
family = [lover, brother, sister]

# looping through the list of family members
# and then looping through the individual dictionaries
for role in family:
    if role['member'] == 'lover':
        print(
            f"The love of my life is {role['first_name'].title()} "
            f"{role['last_name'].title()}."
            )
    elif role['member'] == 'brother':
        print(
            f"My brother's name is {role['first_name'].title()} "
            f"{role['last_name'].title()}."
        )
    elif role['member'] == 'sister':
        print(
            f"My sister's name is {role['first_name'].title()} "
            f"{role['last_name'].title()}."
        )
    if role['sex'] == 'male':
        print(
            f"He is {role['age']} years old and lives in {role['city'].title()}. "
            f"His favorite color is {role['fav_color']}."
        )
    elif role['sex'] == 'female':
        print(
            f"She is {role['age']} years old and lives in {role['city'].title()}. "
            f"Her favorite color is {role['fav_color']}."
        )
print("\n")
# initializing dictionaries
tux = {
    'animal': 'cat',
    'name': 'tux',
    'owner': 'stephanie',
    'fave_toy': 'spider',
    'age': 8,
}
morgan = {
    'animal': 'dog',
    'name': 'morgan',
    'owner': 'john',
    'fave_toy': 'bunny',
    'age': 9,
}
bruce = {
    'animal': 'cat',
    'name': 'bruce',
    'owner': 'michael',
    'fave_toy': 'laser',
    'age': 4
}
meli = {
    'animal': 'cat',
    'name': 'meli',
    'owner': 'victor',
    'fave_toy': 'snake',
    'age': 1
}
coco = {
    'animal': 'cat',
    'name': 'coco',
    'owner': 'kathy',
    'fave_toy': 'couch',
    'age': 12,
}

# making a list if dictionaries
pets = [tux, morgan, bruce, meli, coco]

# looping through the list and using the dictionary keys and values
for animals in pets:
    if animals['owner'] == 'victor' or animals['owner'] == 'stephanie':
        print(
            f"This is our {animals['animal']} {animals['name'].title()}."
        )
    elif animals['owner'] == 'john' or animals['owner'] == 'kathy':
        print(
            f"This is my parents' {animals['animal']} {animals['name'].title()}."
        )
    elif animals['owner'] == 'michael':
        print(
            f"This is my brother's {animals['animal']} {animals['name'].title()}."
        )

# per deepseek, the below way is more concise and more easily maintainable 
# because it avoids excessive if-elif statements
# the relationship dictionary can be edited and once
# instead of complex if-elif statements
owner_relationships = {
    'victor': 'ours',
    'stephanie': 'ours',
    'michael': 'my brother\s',
    'john': 'my partents\'',
    'kathy': 'my parents\'',
}

for animals in pets:
    owner = animals['owner'] # creating local variable to use 
    relationship = owner_relationships.get(owner, 'owner unknown') # variable 
    # accesses the owner_relationships dictionary and matches the owner to the
    # relationship. uses the default if an animal owner doesn't exist in the 
    # raltionships dictionary.

    description = (
        f"This is {relationship} {animals['animal']} {animals['name'].title()}. "
        f"{animals['name'].title()} is {animals['age']} years old and loves "
        f"playing with their {animals['fave_toy']}."
    ) # creates a variable that can be easily printed.

    if animals['age'] >= 10: # adding to the description if an animal is 
        # older than 10.
        description += (
            f" {animals['name'].title()} is a wise and an "
            f"experienced {animals['animal']}!"
        )
    print(description)
print("\n")

# intializing a dictionary
fave_places = {
    'victor': ['italy', 'japan', 'united states'],
    'stephanie': ['italy', 'beach'],
    'john': ['chicago', 'new york', 'wyoming'],
}

# looping through the dictionary and using keys and values
for k, v in fave_places.items():
    name = k
    place = v
    print(
        f"Some of {name.title()}'s favorite places include: "
    )
    for item in place:
        print(
            f"\t{item.title()}"
        )
print("\n")

fave_nums = {
    'victor': [3, 7, 11, 24, 69, 420],
    'stephanie': [1, 2, 14, 28],
    'bill': [187, 45, 187, 47]
}

for name, num in fave_nums.items():
    print(
        f"{name.title()}'s favorite numbers are: "
    )
    for n in num: 
        print(
            f"\t{n}"
        )
print("\n")

cities = {
    'san_franciso': {
        'country': 'united states',
        'population': 805_000,
        'fact': 'has aweful public transit system',
    },
    'tokyo': {
        'country': 'japan',
        'population': 15_000_000,
        'fact': 'is the most populated city in the world',
    },
    'athens': {
        'country': 'greece',
        'population': 644_000,
        'fact': 'is the capital of greece',
    }
}

for city, city_info in cities.items():
    print(
        f"{city.title()} is in {city_info['country'].title()}. "
        f"It {city_info['fact']} and has a population of {city_info['population']}."
    )
print("\n")

