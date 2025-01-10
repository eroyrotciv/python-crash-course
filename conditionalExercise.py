# predicting if evaluation will be True/False
user = 'active'
print("If user == 'active', the result should be 'True'.")
print(user == 'active')

age = 31
print("\nIf age >= 21, the result will be 'True'.")
print(age >= 21)

birthMonth = 'April'
print("\nIf birthMonth.lower() != 'april', the result will be 'False'.")
print(birthMonth.lower() != 'april')

print("\nIf birthMonth == 'april', result will be 'False'.")
print(birthMonth == 'april')

# using keywords 'and' and 'in' in a conditional evaluation
groceryList = ['peas', 'rice cakes', 'salad mix', 'dressing', 'goat cheese']
print("\nGrocery List:\n", groceryList)
if 'peas' in groceryList and 'salad mix' in groceryList:
    print("You've got some healthy items in your list.")

# using keyword 'not' in a conditional evaluation
if 'ice cream' not in groceryList:
    print("Great job for sticking to your plan of not getting ice cream!")

# using keyword 'or' in a conditional evaluation
order = ['salad', 'fries', 'burger']
print("\nOrder includes:\n", order)
if 'burger' in order or 'fries' in order:
    print("I thought you were trying to eat healthy?")

