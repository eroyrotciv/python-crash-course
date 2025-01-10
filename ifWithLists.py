"""
# simple for loop to go through pizza toppings
requested_toppings = ['mushrooms', 'peppers', 'sausage', 'onions']
for topping in requested_toppings:
    print(f"Adding {topping}.")
print("\nYour pizza is done!")

# for loop and if statement to check for unavailable topping
for topping in requested_toppings:
    if topping == 'peppers':
        print(f"Sorry, {topping} is currently unavailable.")
    else:
        print(f"Adding {topping}.")
"""
"""
# checking to see if a list is empty prior to conditionals
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("Finished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")
"""
# using multiple lists and checking for list values
available_toppings = ['mushrooms', 'olives', 'peppers', 'pepperoni',
                      'sausage', 'onions', 'chicken', 'beef']

requested_toppings = ['onions', 'french fries', 'chicken', 'mushrooms']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we can't put {topping} on this pizza.")
print("Finished making your pizza.")

