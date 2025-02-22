# conditional loops and if-elif-else statements to work through lists
usernames = ['vic', 'admin', 'temp', 'steph', 'mike', 'gootch']
if usernames:
    for _ in usernames:
        if _.lower() == 'admin':
            print(f"Hello {_.title()}, would you like to see a status report?")
        else:
            print(f"Hello {_.title()}, what are you working on today?")
else:
    print("I'm sorry, it seems I'm having a problem locating your account. " \
          "Please contact your admin.")

new_users = ['vic', 'admin', 'mike', 'joeseph', 'aaron', 'josh', 'tricky']
print("\n")

# comparing 2 lists and appending new users to existing users w/o duplicates
for _ in new_users:
    if _.lower() in usernames:
        print(f"Sorry, {_} is already being used, please choose a different " \
              "username.")
    elif _.lower() not in usernames:
        usernames.append(_)
        print(f"Congratulations, {_} is available. Please choose a password.")
# showing that values have been appended to users
print(usernames)

