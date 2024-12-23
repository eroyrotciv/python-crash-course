cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus', 'honda', 'acura']

# .sort() method changes the order of the list permanently.  List is now ordered alphabetically and orginal order is 'lost'.
cars.sort()
print(cars)

# .sort(reverse=True) arugment reverse=true passed to the .sort() method will sort alphabetically in reverse order.
cars.sort(reverse=True)
print(cars)

# retain original list order and present list with sorted() function.
cars = ['lexus', 'toyota', 'acura', 'honda', 'subaru', 'audi', 'bmw']
print("\nHere is the list of cars in order I would choose from: ")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

# reverse=True used with the sorted() function. 
print("\nHere is the reversed sorted list:")
print(sorted(cars, reverse=True))

# showing the orginal list order is retained
print("\nHere is my original ordered list again.")
print(cars)

# using .reverse() method to reverse the original order
cars.reverse()
print(cars)

# .reverse() permanently changes the order of the list.  Can be reverted back to the original order with another .reverse() method call
cars.reverse()
print(cars)

# using len() function to find the number of items in a list
print(len(cars))

