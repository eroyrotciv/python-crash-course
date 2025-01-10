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
