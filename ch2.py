name = "algor rhythm"
#using string functions to modify the string
print(name.title()) #Algor Rhythm
print(name.upper()) #ALGOR RHYTHM
print(name.lower()) #algor rhythm

#using variables inside of strings
firstName = "algor"
lastName = "rhythm"
fullName = f"{firstName} {lastName}" #f-strings 
#fullName = firstName + " " + lastName  #concatenation can also be used
print(fullName.title()) #Algor Rhythm
print(f"Hello, {fullName.title()}! Is it {lastName.title()} or Rizzem?") 

message = f"Good day to you, {firstName.title()}!"
print(message)

#using whitespace
print("Python")
print("\tPython") #\t is a tab
print("Languages:\nPython\nJavaScript\nSwift") #\n is a newline
print("Languages:\n\tPython\n\tJavaScript\n\tSwift") #can combine \n and \t to have a new line and tabbed

#stripping whitespace
favLanguage = " Swift "
print(favLanguage)
print(favLanguage.rstrip().lstrip()) #strips whitespace from right and left
print(favLanguage.strip()) #also strips whitespace from right and left

#permanently removing whitespace by reassigning the variable
favLanguage = favLanguage.strip()
print(favLanguage)

#removing prefixes and suffixes
webUrl = "https://www.apple.com"
webSite = webUrl.strip("https://") #removes the prefix using strip method
print(webSite)
company = webSite.removeprefix("www.").removesuffix(".com").title() #removes the prefix using removeprefix method and suffix using removesuffix method
print(company)

#testing if I can strip a prefix and a suffix at the same time
print(webUrl.strip("https://www.").strip(".com").title()) #it works

#testing if strip method and what all it can remove
testString = "abcbcacabcbaEnglish MUTHAFUCKA! Do you speak it?abcbcacabcba" 
print(testString.strip("abc")) #removes all instances of a, b, and c from beginning and end of string until it reaches a character that is not a, b, or c
testString = "abccba dabccabEnglish MUTHAFUCKA! Do you speak it? abccbaab dbcabac"
print(testString.strip("abc")) #once it reached a character that wasn't a, b, or c it stopped removing said characters, including whitespace
testString = "abccbadabccabEnglish MUTHAFUCKA! Do you speak it? abccbaabdbcabac"
print(testString.strip("abcdE")) #if E was NOT capitalized, it would not have removed it.  Literally strips the characters requested
print(testString.removeprefix("abccbadabc").removesuffix("baabdbcabac")) #removes the exact phrases specified in the methods

