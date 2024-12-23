# initialize an empty list, then ask user to input guests they would like to have at dinner, appending them to the empty list. 
guestList = []
guest = input("If you had to choose one person to invite to dinner, dead or alive, whom would you invite? ")
guestList.append(guest.title())
guest = input("If you had to invite another person, whom would you invite? ")
guestList.append(guest.title())
guest = input("Alright, last person that you can invite to dinner. Who will it be? ")
guestList.append(guest.title())

print(guestList)
# actually asking the guest to dinner.  Using f-strings with lists
print(f"{guestList[0]}, how would you feel about coming down to have dinner with me?") # next block of code relys on input being "Nipsey Hussle"
print(f"{guestList[1]}, come have dinner with myself and {guestList[0]}.")
print(f"{guestList[2]}, I've got {guestList[0]} and {guestList[1]} coming to dinner.  Would you be so kind as to bless us with your presence?")

cantCome = "Nipsey Hussle"
guestList.remove(cantCome)

print(f"Unfortunately, {cantCome} can't make it to dinner.")
guestList.append(input(f"So far we have {guestList[0]} and {guestList[1]}.  Who else should we invite to dinner? "))

# asking guests to come to dinner again.  
print(f"{guestList[0]}, I'm having a little get together.  Would you like to come? ")
print(f"{guestList[1]}, {guestList[0]} is coming over for dinner.  Do you wanna come too?")
print(f"{guestList[2]}, {guestList[0]} and {guestList[1]} are coming over for dinner.  You should come!")
print("I found a bigger table, so now we can have even more people over for dinner.")

# inserting and appending to the list manually.
guestList.insert(0, 'Eminem')
guestList.insert(2, 'Nas')
guestList.append('Lil Wayne')
print(guestList)

# all new invited to everyone on the list.
print(f"{guestList[0]}, I'm having a dinner with some of my favorite rappers, come save them!")
print(f"{guestList[1]}, I've got you a safe spot at my dinner table.  I'd love it if you came if you're able.")
print(f"{guestList[2]} the OG kingmaker.  If your able, come join some of the GOATs at my dinner table.")
print(f"{guestList[3]}, you're ego may have gotten swole.  Come and take your place amongst the GOATs.")
print(f"{guestList[4]}, I may be crazy, but can't deny the fact that you're one of the GOATs. For you my dinner table has some space, just bring the Spade of Ace.")
print(f"{guestList[5]}, it would be a shame if you didn't come to dinner and maintain your reign.")

# shriking list exercise
print("This is really embarrasing.  The table I ordered for our dinner won't be here in time.  So I only have a spot for 2 people.  This is gonna be tough.")

uninvited = guestList.pop(0)
print(f"{uninvited}, I'm sorry to do this to you.  But I can't let you embarrass them.  You're uninvited, let me tell the rest of them.")

# had to remember that the list shrinks as the names are popped.  Previous error was using an index that was out of limits to what is 
# actually contained within the list.  
uninvited = guestList.pop(2)
print(f"{uninvited}, you old soul.  I can't have you at dinner no more, I must roll.")

uninvited = guestList.pop(2)
print(f"{uninvited}, now I'm just being lazy.  This dinner is for OGs who I can one day see paying me.  Since you'll be in jail soon, I'll just email you.")

uninvited = guestList.pop(2)
print(f"{uninvited}, I hope this note reaches you before you board the train.  My dinner guestlist has been slain, you're uninvited. Repeat, return from where you came.")

print(guestList)
print(f"{guestList[0]}, you've still retained your number one spot.  Come to the house let's get busy with this pot.")
print(f"OG {guestList[1]}, on this guestlist I had to spaz.  If you can still make it, let's talk about this dough that we'll be raking.")

# again forgot that once the first index is deleted, the 2 index becomes the first.  
del guestList[0]
del guestList[0] # previous error was written as del guestList[1].  guestList shrunk to 1 value w/ index of [0]. 
print(guestList)