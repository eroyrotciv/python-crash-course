restaurant_orders = {
    'subway': 'tuna',
    'mcdonalds': 'quarter pounder',
    'chinese': 'teryaki chicken',
    'mexican': 'acp',
    'italian': 'steak and cheese',
}
# using both the keys and values out of a dictionary
for k, v in restaurant_orders.items():
    print(f"I get {v.title()} from {k.title()}.")

# using just the key from a dictionay
print("\nI sometimes get food from the following restaurants: ")
for k in restaurant_orders:
    print(k.title())

# using just the value from a dictionary
print("\nIf I go out to eat, I usually get one of the following items: ")
for v in restaurant_orders.values():
    print(v.title())

fave_languages = {
    'victor': 'swift',
    'stephanie': 'swift',
    'michael': 'ruby',
    'tyler': 'python',
    'mom': 'c+',
    'dad': 'kobal',
}

unpolled_people = ['josh', 'aaron', 'jordan', 'tyler', 'mike', 'kathy', 'oksana']

# iterating through a dictionary and matching to values in a list
print("\n")
for name in unpolled_people:
    if name in fave_languages.keys():
        print(
            f"{name.title()}, looks like we already have your response. "
            f"Your favorite programming language is {fave_languages[name].title()}."
        )
    elif name not in fave_languages.keys():
        print(
            f"{name.title()}, do you have a favorite programming language?"
        )

# iterating throuhg a dictionary and matching values NOT in a list
print("\n")
for name in fave_languages:
    if name not in unpolled_people:
        print(
            f"{name.title()}, thank you for pre-emptively responding to the poll. "
            f"Your favorite programming language is {fave_languages[name].title()}."
        )
    elif name in unpolled_people:
        print(
            f"{name.title()}, looks like we missed your answers the first time "
            f"around. "
            f"Your favorite programming language is {fave_languages[name].title()}."
        )
    else:
        print(
            f"{fave_languages.keys().title()}, your language is lsjfljfadl."
        )

# trying to capture all names in the dictionary and the list
# per DeepSeek, create a set of processed names
processed_names = set()

for name, language in fave_languages.items():
    if name not in processed_names:
        print(
            f"{name.title()}'s favorite language is {language.title()}."
        )
        processed_names.add(name)

for name in unpolled_people:
    if name not in processed_names:
        print(
            f"{name.title()} has not provided a favorite language yet."
        )
        processed_names.add(name)
