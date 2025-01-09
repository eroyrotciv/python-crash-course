# tuple is an immutable list.  That is it cannot be changed.  Like a constant? 
# tuple is defined similar to a list, except you use () instead of []
dimensions = (200, 50)
print(dimensions[0]) # just like in a list, the index value is used to acces items in tuple
print(dimensions[1]) # [] are used to acces the index value, not (). () are only used to define the tuple

# dimensions[0] = 250 # code gives an error message stating that a tuple does not support item assignment 

# technically, the presense of a comme "," is what defines a tuple, so if for whatever reason a tuple of 1 value is desired it can be initiated as shown below
myT = (24, )

# looping through a tuple just like a list
for _ in dimensions:
    print(_)

# eventhough a tuple cannot be modified, new values can be assigned 
print("Original dimensions: ")
for _ in dimensions:
    print(_)

dimensions = (240, 420)

print("\nModified dimensions: ")
for _ in dimensions:
    print(_)

buffetItems = ('chicken', 'beef', 'rice', 'salad', 'cheese')
print("\nOur buffet items this week are: ")
for _ in buffetItems:
    print(_.title())

# buffetItems.clear() # throws an error, because a tuple CANNOT be modified.

buffetItems = ('fish', 'pork', 'mashed potatoes', 'steamed vegetables', 'salad')
print("\nOur buffet items next week will be: ")
for _ in buffetItems:
    print(_.title())

