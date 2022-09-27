# a program to randomly pick who will pay the meal 
import random

names = input("inpu the names of people here: ").split(",")
print(names)
# picker = random.randint(0,len(names)-1)
#even better
picker = random.choice(names)

print(names[picker])
