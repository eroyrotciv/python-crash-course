# creating an empty dictionary and then using inputs to store information 
# about a person
persons = {}
persons['first_name'] = input("What is your first name? ")
persons['last_name'] = input("What is your last name? ")
persons['age'] = input("How old are you? ")
persons['city'] = input("In what city do you currently live? ")

# printing a personalized message to that individual using the information 
# they provided
print(f"Hello {persons['first_name'].title()}, pleasure to meet you. "
      f"How are you enjoying {persons['city'].title()}?")

# storing peoples favorite numbers in dictionary
fave_num = {
    'victor': 24,
    'stephanie': 28,
    'michael': 6,
    'kathy': 17,
    'john': 8,
}

# .items() method presents dictionary key-value pairs as (key, value) in a list
# ex: dict_items([(key1, value1), (key2, value2), ...])
print(fave_num.items())

# using a for loop to iterate through the key-values in a dictionary and print
# out a customized message
for name, number in fave_num.items():
    print(f"{name.title()}'s favorite number is {number}.")

for key, value in persons.items():
    print(f"{key.title()}: {value.title()}")
