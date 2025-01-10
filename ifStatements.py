# simple if statement has one test and one action
# if conditionalTest:
#     do something
# if condition evaluates True, all indented code will be executed
# if-else is used when you want a different action to be executed
# when the condition evaluates as False, the else statement will execute
age = input("How old are you? Please enter an integer: ")
age = int(age)
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n")

print("\n")
# if-elif-else is used when testing more than 2 possible situations
# only 1 block will be executed in an if-elif-else statement
# once one condition is met, the indented code is executed and the rest 
# of the elif-else statements are ignored.
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# a more concise way to execute above code
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# using multiple elif blocks
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# else block is optional and can be omitted
# omitting the else block is helpful to catch a specific condition
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your adimssion cost is ${price}.")
# the else block is a catch-all statement.  It will catch all statements that
# were not caught by the if-elif statements.

# if more than one contdition should be checked, multiple if statements
# should be used. Since an if-elif-else statement will not check the other 
# blocks once the first True condition is returned
requested_toppings = ['mushrooms', 'extra cheese', 'onions']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
if 'onions' in requested_toppings:
    print("Adding onionos.")
if 'peppers' in requested_toppings:
    print("Adding peppers.")
print("\nFinished making your pizza.")

