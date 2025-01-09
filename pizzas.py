favPizzas = ['veggie', 'cheese-less', 'supreme']
for favPizza in favPizzas:
    print(f"One of my favorite pizzas is {favPizza} pizza!")

print("I like pizza, but it's not my favorite.")

gfPizzas = favPizzas[:]
favPizzas.append('meat-lovers')
gfPizzas.remove('cheese-less')

print("My favorite pizzas are: ")
for pizza in favPizzas[:]:
    print(pizza)

print("My girlfriends favorite pizzas are: ")
for pizza in gfPizzas[:]:
    print(pizza)

