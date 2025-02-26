sandwich_orders = [
    'pastrami', 'tuna', 'chicken', 'turkey', 'pastrami', 'ham', 'italian', 
    'supreme', 'club', 'pizza', 'meat ball', 'steak and cheese', 'chicken chop', 
    'pastrami'
]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        substitute = input(
            "I'm sorry, we have ran out of pastrami today. \n"
            "Is there another type of sandwich you would like instead? \n"
            "Please type the sandwich you would like instead. \n"
            "If you don't want another type of sandwich, please type 'no': "
        )
        if substitute == 'no':
            print(
                "We're so sorry about that. It's a very popular sandwich.\n"
            )
        else:
            print(
                f"Ok, we'll make you a {substitute} sandwich instead.\n"
            )
            sandwich_orders.append(substitute)
        continue
    print(
        f"We are making your {sandwich} sandwich right now."
    )
    finished_sandwiches.append(sandwich)
    print(
        f"Your {sandwich} sandwich is made.\n"
    )
print(
    "\nWe are finsished with your order. "
    "Here is the list of sandwiches we have made: "
)
for i in finished_sandwiches:
    print(i, "sandwich")
print("Does everything look correct?\n")

