"""
# asiging a multi-line prompt to a variable, then passing that variable as 
# the input argument to be presented to the user.
prompt = (
    "If you share some information about yourself, I can use that information "
    "to present more personalized messges. "
)
prompt += "What is your name? "

name = input(prompt)
print(
    f"Thank you {name.title()}, how can I help today? "
)

# converting an input string value to a numeric value using int()
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are old enough to vote!")

# the modulo operator (%) divides one number by another and return the remainder
print("4/3 has a remainder of: " + str(4%3)) # 4/3 is 1 w/ a remainder of 1, 1 is returned
print("5/3 has a ramainder of: " + str(5%3)) # 5/2 is 1 w/ a remainder of 2, 2 is returned
print("6/3 has a ramainder of: " + str(6%3)) # 6.3 is 2 w/ a remainder of 0, 0 is returned

# using input, int(), and modulo to determine if the user's number is even/odd
num = input("Enter a number and I'll tell you if its even or odd: ")
num = int(num)

if num % 2 == 0: # read as modulo of a number and 2
    print("The number you entered is even.")
else:
    print("The number you entered is odd.")

# try it yourself exercises
requested_car = input("What kind of car are you looking for today? ")
print(
    f"Let me see if we have a {requested_car.title()} in stock today."
)

num_people = input("How many people are in your party? ")
num_people = int(num_people)

if num_people < 8:
    print(
        f"I've got a table for {num_people} ready. Please follow me."
    )
else:
    print(
        f"Right now I don't have a table that can seat {num_people}. "
        "Looks like it might be an hour wait."
    )

num = input(
    "Please provide a number and I'll determine if the number is a multiple of "
    "10 or not: "
)
num = int(num)

if num % 10 == 0:
    print(
        f"{num} is a multiple of 10."
    )
else:
    print(
        f"{num} is NOT a multiple of 10."
    )


# a for loop takes a collection of items and runs a block of code once for 
# each item in the collection
# a while loop runs as long as (or while) a certain condition is True

# using a while loop to count up to a certain number
num = 1
while num <= 11:
    print(num)
    num += 1 # shorthand for num = num + 1
print("\n")

# using a while loop to keep a program running until user input the quit value
prompt = "Write something and I will repeat it back. "
prompt += "Type 'quit' to stop. "

message = "" # initializing w/o a value allows python to compare to quit!!
# even though message is an empty value, it can be compared to another string
while message != 'quit':
    message = input(prompt)
    if message != 'quit': # using an if statement to NOT print the quit!! statement
        print(message)
print("\n")

# using a flag variable to monitor multiple events that can trigger a program to stop
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
print("\n")

# you can use a break statement to exit a while loop immediately w/o running 
# any remaining code in the loop, regardless of the result of any conditional
prompt = "\nPlease enter a name of a city you have visited. "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}.")
print("\n")

# you can use a continue statement to return to the beginning of the loop
# an not execute the remainder of the code
num = 0
while num <= 10:
    num += 1
    if num % 2 == 0: # if the number is even, continue does NOT execute the rest
        continue # of the code and instead returns to the beginning and runs again
    
    print(num)
print("\n")

# my own practice examples of while loops, flags, break/continue statements
games = []
prompt = (
    "Type the name of a game you may want to play and press enter. "
    "To stop, type 'stop': "
)

def print_games(games_list): # defining a function that prints the list of games
    print("The games you have listed so far: ")
    for i, game in enumerate(games_list, start=1): # use enumerate to count up
          print(
               f"{i}. {game.title()}"
          )
    print("\n")

active = True
while active:
    game = input(prompt)
    if game == 'stop': # stops the loop if user types 'stop'
        active = False
        break
    elif game.strip() == '': # request another input if user type whitespaces
        print("Looks like you did not enter a valid game. ")
        continue

    if game in games: # conditional that checks if the game already exist in list
        print(
            f"{game.title()} has already been added."
        )
        print_games(games)
        continue

    games.append(game) # appends the input to the list
    if len(games) >= 10: # limits the size of the list
        print(
            "I'm sorry, you have reached the max number of games I can track "
            "at this time, which is 10."
        )
        active = False
        print_games(games)
        break
    print_games(games)


# moving items from one list to another using a while loop
unconfirmed_users = ['alice', 'brian', 'michael', 'victor', 'stephanie']
confirmed_users = []

while unconfirmed_users: # runs as long as the list is NOT empty
    current_user = unconfirmed_users.pop() # temp variable for list item

    print(f"Verifying user: {current_user.title()}") # output to show work
    confirmed_users.append(current_user) # appends the variable to another list

print("\nThe following users have been confirmed: ")
for i in confirmed_users: # use for loop to list items instead of just printing
    print(i.title()) # the list, which will be in a list format 
print("\n")

# removing all instances of a specific value in a list using a while loop
pets = ['horse', 'cat', 'dog', 'cat', 'donkey', 'cat', 'cat', 'horse', 'fish']
print("We will be removing all instances of 'cat' from the following list.")
for pet in pets:
    print(pet)
print("\n")

while 'cat' in pets:
    pets.remove('cat')

print("All instances of 'cat' removed.")
for pet in pets:
    print(pet)
print("\n")

"""

# filling a dictionary w/ user inputs
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which video game would you like to play? ")

    responses[name] = response

    repeat = input(
        "Is there anybody else who would like to respond? Please type y/n: "
    )
    if repeat == 'n':
        print(
            "Polling has been closed."
        )
        polling_active = False

print("\n-----Poll Results-----")
for name, response in responses.items():
    print(
        f"{name.title()} would like to play {response.title()}!"
    )
print("\n")
