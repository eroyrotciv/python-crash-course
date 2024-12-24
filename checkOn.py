# initializing an empty list and then addin people to the list
people = []
people.append('justin')
people.insert(0, 'stephanie')
people[1] = 'mom'
people.append('dad')
people.append('josh')
people.append('adam')
people.append('jordan')
people.append('aaron')
people.append('oksana')
people.append('michael')
people.append('tyler')
people.append('michelle')
people.append('jacob')
people.append('ava')
people.insert(3, 'mariah')
people.insert(5, 'steph')

# using temporary sorted function to print list in alphabetical and reverse order
print(sorted(people))
print(sorted(people, reverse=True))

# permanently sort the list in alphabetical order, passing reverse=False to .sort() method
people.sort(reverse=False)
print(people)
# finding out and printing the length of the list of people
print(len(people))

# deleting, popping, and removing items from a list
del people[1]
baby = people.pop(-3)
print(f"{baby.title()} is short for {people[-2].title()}, so no need to have her listed twice.")
people.remove('mariah')
print(people)
print(len(people))