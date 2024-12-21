firstName = input("What is your first name? ").strip()
lastName = input("What is your last name? ").strip()
fullName = f"{firstName} {lastName}"
message = f"Hi, {firstName.title()}, welcome to the beginning of your Python journey!"
print(message)

print(f"{firstName.upper()}, LOOK OUT! There'a a Python snake by your feet!")
print(f"{lastName.lower()} is lowercased of your last name: {lastName.title()}.")

quoteAuthor = "Nipsey Hussle"
quote = "Ima die for my fucking respect!"
print(f'{quoteAuthor} once said, "{quote}"\nAnd boy did he?')
message = f'{quoteAuthor} once said, "{quote}" Unforutnately he did.'
print(message)

#using single/double quotes within themselves
quote = "I wrote it down, then I followed through!"
print(f'"{quote}" \n\t\t\t\t\t-{quoteAuthor}\nIs one of my favorite quotes.')

#using "\" the escape character to escape double/single quotation marks
fileName = 'pythonNotes.txt'
print(f"The file name without it's extension is \"{fileName.removesuffix(".txt")}\".")
