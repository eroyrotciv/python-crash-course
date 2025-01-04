magicians = ['victor', 'michael', 'tyler']
for magician in magicians: #pulls a name out of the list and associates it w/ the variable magician
    print(magician) #for every magician in the list of magicians, print the magician's name

for magician in magicians:
    print(f"{magician.title()}, that was a neat trick. How'd you do that!?")
    print(f"I can't wait to see you rnext trick, {magician.title()}.\n") #any code that is indented is part of the for loop and will run for each item in the list 

print("Thank you, all for the great magic show!") #since this line is not indented, it is not part of the for loop
