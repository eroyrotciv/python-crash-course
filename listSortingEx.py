# places I'd like to visit
visitList = ['japan', 'greece', 'ice land', 'spain', 'colorado']
print(visitList)

print(f"My list sorted in alphabetical order: {sorted(visitList)}")
print(f"My list in the original order: {visitList}")
print(f"My list sorted in reverse alphabetical order: {sorted(visitList, reverse=True)}")
print(f"My list in the original order: {visitList}")

visitList.reverse()
print(f"My list in the original order, but reversed: {visitList}")

visitList.reverse()
print(f"List reversed again to the orignal order: {visitList}")

visitList.sort()
print(f"List permanently sorted alphabetically: {visitList}")

visitList.sort(reverse=True)
print(f"List permanently sorted in reverse alphabetical order: {visitList}")

visitList.append(input("Is there anywhere else you'd like to visit before you die? ").lower())
visitList.append(input("Anywhere else? ").lower())
visitList.append(input("One more place? ").lower())
print(visitList)