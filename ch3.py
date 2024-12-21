games = ['Elden Ring', 'Sekiro', 'Witcher 3', 'Outer Wilds', 'Skyrim', 'RDR2', 'Ghost of Tsushima', 'God of War', 'Last of Us', 'MGS V',
     'Nier Automata',  'Cyberpunk', 'BG3', 'Hades', 'Binding of Isac', 'Prey', 'Control', 'Factorio', 'Disco Elysium', 'Hollow Knight', 
     'Dark Souls', 'Yakuza', 'Persona', 'Portal', 'Bioshock', 'Mass Effect']
# using lists w/ index numbers starting at 0 and using "-" to start at the end of a list
print(games)
print(games[0])
print(games[-1])

# using lists w/ f-string format
message = f"The game I've been playing the most lately has been {games[0].title()}."
print(message)

ownedGames = ['Elden Ring', 'Sekiro', 'Witcher 3', 'Outer Wilds', 'Skyrim', 'RDR2', 'MGS V', 'Nier Automata', 'Cyberpunk', 'BG3', 'Hades',
              'Prey', 'Control', 'Disco Elysium', 'Hollow Knight', 'Dark Souls', 'Yakuza', 'Persona', 'Portal', 'Bioshock']

# modifying elements wihtin lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[2] = 'ducati'
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

# empty list with variables added using append method
installedGames = []
installedGames.append('elden ring')
installedGames.append('outer wilds')
installedGames.append('RDR2')
installedGames.append('MGS V')
installedGames.append('persona')

print(installedGames)

# using insert method to insert variables into specific index location within a list
installedGames.insert(0, 'dark souls')
installedGames.insert(0, 'cyberpunk') #cyberpunk takes place as the 1st value in the list, sliding all other values one to the right
print(installedGames)

# removing items from list using del if you know the position within the list
del installedGames[0]
print(installedGames)

# using .pop() method to remove an item from a list and to still be able to use said item
poppedGame = installedGames.pop() #last item in the list removed and assigned to a new variable
print(installedGames) # showing the item removed
print(poppedGame) # showing that we still have acces to the popped value
mostPlayed = installedGames.pop(1) # using .pop() method w/ an index number
print(f"The game I've played the most is probably {mostPlayed.title()}.")

# removing an item using the .remove() mehtod when the value is known
games.remove('Yakuza')
print(games)

# removing a value using an intermediary variable.  
tooWeird = 'Binding of Isac'
games.remove(tooWeird)
print(games)
print(f"{tooWeird}, looks like a game I wouldn't enjoy.")

motorcycles.append('harley')
motorcycles.append('suzuki')
print(motorcycles)

# .remove() only removes the first instance of a value it finds.  
motorcycles.remove('suzuki')
print(motorcycles)

