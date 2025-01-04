for value in range(1, 5):
    print(value) #prints 1-4. range() function starts counting at the 1st value and stops when it reaches the 2nd provided number

for value in range(1, 6):
    print(value)

for value in range(6): #passing only one value to range() will start the sequence at 0
    print(value) #will print 0-5

#can use list() function to create a list with the values generated by range()
numbers = list(range(1, 24))
print(numbers)

#3rd value passed into the range() function specifies a step size
evenNumbers = list(range(2, 25, 2))
print(evenNumbers)

oddNumbers = list(range(1, 25, 2))
print(oddNumbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

squaresSquared = [] #squaring the squares values
for value in squares:
    squaresSquared.append(value ** 2)

print(squaresSquared)

print(min(squaresSquared)) #using simple statistics w/ list of numbers
print(max(squaresSquared))
print(sum(squaresSquared))

#list comprehension allows us to generate a list of squares w/ 1 line of code insted of the 3-4 it took earlier. 
#combines the for loop and the creation of the new element into 1 line.  Automatically .appends() each new element.
squares = [value**2 for value in range(1, 100, 5)]
print(squares)

