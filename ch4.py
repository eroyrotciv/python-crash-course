magicians = ['alice', 'david', 'victor']
for magician in magicians[:-1]:
    print(magician.title(), end=', ')
print(magicians[-1].title(), end='.\n')

for magician in magicians:
    print(f"{magician.title()}, nice trick.")

