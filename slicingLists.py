players = ['tom', 'rob', 'randy', 'julian', 'wes', 'aaron', 'jared', 'rodney', 'asante']
# a slice is separated by a colon.  Will work with list up to the 2nd number, but not including.
print(players[1:5])
# can I step in a list? 
print(players[0:-1:2])
# yes I can!
# how do I select the last item in the list? 
print(players[0:-0:2])
# this does not seem to work.  -0 is slicing at the beginning, so no items in the list are being sliced.
print(players[0::2])
# this worked.  Not specifying a 2nd value and instead using another colon counts up to and including the last value.
# just as the last value can be omitted to count to the end of the list, the first value can be omitted to start slicing at the beginning of the list.
print(players[::2])
# to output the end of the list only, we can use a negative value as the first slice index 
print(players[-3:])

#looping through a slice
print("Here is the offensive weapons for the unstoppable Patriots dream team: ")
for player in players[:6]:
    print(player.title())
    
# copying a list or a part of a list.
myFoods = ['eggs', 'salad', 'chilli', 'cava', 'tofu', 'mushrooms', 'onions']
gfFoods = myFoods[:-3] # the list copy only worked because we used a slice, (even if we slice [:] the entire list).
print(gfFoods)

# appending new items to each list to prove that they are infact 2 separate lists
myFoods.append('mashed potatoes')
gfFoods.append('pickles')
print(myFoods)
print(gfFoods)

# assigning myFoods to broFoods (w/o slicing) will always equal what myFoods is
print("=============================================\nbroFoods")
broFoods = myFoods
print(broFoods)
myFoods.append('pickled onions')
print(broFoods)
# in this instance, both variables point to the same list, instead of making a copy of the original list
# if we modify the list via broFoods, it still modifies the original list.
broFoods.insert(0, 'acp')
print(myFoods)

print("Length of the list is: ", len(myFoods))
print("The first 3 items of the list are: ")
print(myFoods[:3])
print("3 items from the middle of the list are: ")
print(myFoods[4:7])
print("The last 3 items in the list are: ")
print(myFoods[-3:])

# using for loops w/ slices
print("The Patriot's best offensive players of all time are: ")
for player in players[:6]:
    print(player.title())

print("Some of my favorite things to eat are: ")
for _ in myFoods:
    print(_.title())
