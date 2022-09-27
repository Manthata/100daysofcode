# write a program that outputs heads or tails rendomly 
import random


random_num = random.randint(0,11)

if random_num%2==0:
    print("Heads")
else:
    print("Tails")