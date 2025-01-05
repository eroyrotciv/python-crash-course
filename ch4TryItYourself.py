numbers = []
for value in range(1, 1_000_001):
    numbers.append(value)


print(min(numbers))
print(max(numbers))
print(sum(numbers))

oddNumbers = [value for value in range(1, 21, 2)]
print(oddNumbers)

multOf3 = []
for value in range(3, 31, 3):
    multOf3.append(value)
    print(value)
print(multOf3)

# cubes = [value**3 for value in range(1,11)] #list comprehension of the below for loop
cubes = []
for value in range(1, 11):
    print(value ** 3)
    cubes.append(value ** 3)
    
print(cubes)

cubes2 = [value ** 3 for value in range(1, 11)]
print(cubes2)


