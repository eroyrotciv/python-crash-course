def greet_user(username): # begins the difining of the function. 
    # '()' are required even if there no parameter
    """Displays a personalized greeting.""" # function docstring
    print(f"Hello, {username.title()}!") # function code block.

greet_user('victor') # function being called and executed with a passed argument
# the argument 'victor' is passed to the function and is assigned to the
# paremeter username.

def display_message():
    """Simple message describing what I'm learning about in Ch7!"""
    print(
        "In chapter 7 I am learning all about functions. "
        "How to define and call them.  How to pass arguments to the function. "
        "Functions allow us to write a block of code and then reuse it "
        "as many times as we would like. "
    )

display_message()

def fave_game(title):
    """Gives the title of a favorite game."""
    print(
        f"One of my favorite video games is {title.title()}."
    )

fave_game('elden ring')

# if a function has multiple paremeters, a function call may need multiple 
# arguments.  Arguments can be passed in multiple ways.
# positional arguments - need to be in the same order as the paremeters defined
# keyword arguments - where arguments consist of variable name and its value;
# and lists and dictionaries of values.

# positional arguments
def describe_pet(animal_type, pet_name):
    """Displays information about the pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'meli') # functions can be calles as many times as we like
describe_pet('cat', 'tux') # if code is repeated, it might need to be a function
describe_pet('morgan', 'dog') # obviously order matters in positional arguments
describe_pet(pet_name='morgan', animal_type='dog') # we can explicitely specify
# which argument should be passed to which parameter

# keyword argument is a name-value pair you pass to a function.
# you directly associate the name and the value within the argument.
# you don't have to worry about the order of arguments. 

def describe_game(genre, title):
    """Provide a description of a game, mostly the genre and the title."""
    print(f"\nOne of my favorite video games is {title.title()}.")
    print(f"It is an {genre}.")

describe_game(genre='action RPG', title='elden ring')
describe_game(title='lies of p', genre='action RPG') # because we explicitely
# specify which argument is passed to which parameter, the order is irrelavent

# a default value can be describe in a function call. If an argument is not
# provided for that parameter, the default value will be used instead.

def describe_car(model, make='toyota'): # parameters with a default value 
    # should be listed last, that way when only required arguments are passed, 
    # they will automatically be passed to the required parameters 

    """Describes the vehicles that I own. make default is toyota because 
    I mostly own or will own toyota vehicles."""
    print(
        f"\nOne of the vehicles that I own is a {make.title()} {model.title()}."
    )

describe_car('prius') # since make has a default, only one argument is passed
describe_car('4Runner') # one argument needed, since make has default
describe_car('a8', 'audi') # make isn't toyta, so passing 2nd argument replaces
describe_car(make='lexus', model='ILX')# showing you can explicitely assign arguments
print("\n")

def make_shirt(message, size='large'):
    """Accepts a shirt size and a message that should be printed on the shirt."""
    print(
        f"We have an order for a {size} shirt. "
        f'The message on the shirt reads "{message}".\n'
    )

make_shirt('Get to work!', 'large')
make_shirt(size='extra large', message='Eat the rich!')
make_shirt('I love Python')
make_shirt('I love Pie Thongs', 'extra large')
make_shirt('Dun dun dun duuunnn', '4X')

def describe_city(city, country='America'):
    """Prints a message stating the city is located in the country."""
    print(
        f"{city.title()} is in {country.title()}.\n"
    )

describe_city('Rome', 'Italy')
describe_city('Chicago')
describe_city(country='Japan', city="Tokyo")

# functions can return values to be used in the call location
# make an argument optional by giving it an empty defaul and listing last
def get_formated_name(first_name, last_name, middle_name=""):
    """Returns a neatly formated full name."""
    if middle_name: # using an if statemet, otherwise there is an extra space 
        # when a middle name is not provided 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

goat_rapper = get_formated_name('kendrick', 'lamar')
wack_rapper = get_formated_name('abrey', 'graham', 'drake')

print(goat_rapper, "\n")
print(wack_rapper, "\n")

# function returning dictionary keys and values
def build_person(first_name, last_name, age=None):
    """Returns a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name,
    }
    if age:
        person['age'] = age
    return person

# build a dictionary of musicians with a dictionary as values. 
musician = build_person('jermaine', 'cole')

print(musician, "\n")

# using while loops with functions
while True:
    print("\nPlease provide your name: ")
    print("(enter 'q' at any time to quite)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formated_name = get_formated_name(f_name, l_name)
    print(f"\nHello, {formated_name}.")
