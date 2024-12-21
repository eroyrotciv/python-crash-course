# initialize an empty list, then ask user to input guests they would like to have at dinner, appending them to the empty list. 
guestList = []
guest = input("If you had to choose one person to invite to dinner, dead or alive, whom would you invite? ")
guestList.append(guest.title())
guest = input("If you had to invite another person, whom would you invite? ")
guestList.append(guest.title())
guest = input("Alright, last person that you can invite to dinner. Who will it be? ")
guestList.append(guest.title())

print(guestList)

print(f"{guestList[0]}, how would you feel about coming down to have dinner with me?")
print(f"{guestList[1]}, come have dinner with myself and {guestList[0]}.")
print(f"{guestList[2]}, I've got {guestList[0]} and {guestList[1]} coming to dinner.  Would you be so kind as to bless us with your presence?")

