prompt = (
    "Please type the toppings you would like on your pizza one at a time. "
    "Type 'done' to stop: "
)
toppings = []
active = True

while active:
    topping = input(prompt)
    if topping == 'done':
        print("You have finished selecting your toppings.")
        print(
            "Your pizza will come with: "
        )
        for item in toppings:
            print(item)
        break
    elif topping.strip() == "":
        print("You didn't enter any toppings.")
        continue
    toppings.append(topping)
    print(
        "So far your pizza will come with: "
    )
    for item in toppings:
        print(item)
    print("\n")
print("\n")

prompt = "Welcome to Yore Cinema. How old are you? Please enter a number. "
prompt += "Type 'cancel' to stop: "
age = 0

while age != 'cancel':
    age = input(prompt)
    if age == 'cancel':
        print("You don't want to watch a movie? Ok then, have a good day! \n")
        break
    elif age.strip() == "":
        print("You did not enter a value. Please try again. \n")
        continue
    age = int(age)
    if age > 0 and age < 3:
        print("Because you're under 3 years old, you get to watch for free. \n")
    elif age >= 3 and age <= 12:
        print("Because you are so young, you admission cost is $10. \n")
    elif age > 12:
        print("Since you're a teenager, your cost is $15. \n")

