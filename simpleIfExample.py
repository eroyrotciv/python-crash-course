# using an if statement to print BMW in all caps instead of title
cars = ['audi', 'bmw', 'toyota', 'lexus', 'honda', 'acura']
for car in cars:
    if car == 'bmw': # equality operator checks to see if the variable assigned 
        print(car.upper()) # to car matches the value we are interested in
    else:
        print(car.title())

topping = 'mushrooms'
if topping.lower() != 'anchovies': # using a not equal operator as a conditional
    print("Hold the anchovies!") 

userAnswer = 17 # can use <, >, <=, >=, and, or to get the desired result
if userAnswer != 24:
    print('That is not correct, please try agian!')

age = input("How old are you? Please enter your age using integers. ")
age = int(age)
# below is a bad way to structure this, b/c once the firs under 21 block is met,
# non of the other blocks will be executed. So none of the driving related
# messages will be printed. 
"""
if age >= 21:
    print("Welcome to adulthood, you can make all kinds of bad decisions!")
elif age < 21:
    print("I'm sorry you are not old enough to buy alcohol.")
elif 18 <= age < 21:
    print("You are old enough to buy tobacco and lotery tickets, but you shouldn't.")
elif 16 <= age:
    print("You are old enought to drive.")
elif age == 15:
    print("You are old enough to drive w/ an adult in the car.")
else:
    print("You are still a child, go play.")
"""
# instead the code should start at one end of the values and increment
# to the other end like so
if age < 15:
    print("You are still a child, enjoy it while you can.")
elif age == 15:
    print("You are old enough to drive with an adult present to supervise.")
elif age < 18:
    print("You are old enough to drive.")
elif age < 21:
    print("You are old enough to buy tobacco and lottary tickets, though you shouldn't")
elif age == 21:
    print("You are old enough to buy alcohol, though I must war you, it is poison.")
elif age > 21:
    print("Welcom to adulthood, you can make all kinds of bad decisions! Good luck!")


# using and/or
"""
age0 = 22
age1 = 18
(age0 >= 21) and (age1 >= 21) # will return False since both are not >= 21

(age0 >= 21) or (age1 >= 21) # will return True since 1 of the 2 is >= 21
"""

# checking whether a value is in a list using keyword "in"
toppings = ['mushrooms', 'onions', 'peppers']
# 'mushrooms' in toppings # will evaluate to True, since the value is in fact listed
# 'pineapple' in toppings # will evaluate to False, since the value is NOT in the list

# checking to see if a value is NOT in a list using the keyword "not"
bannedUsers = ['andrew', 'caroline', 'david']
user = 'marie'
if user not in bannedUsers:
    print(f"{user.title()}, you are allowed in the forum.")

