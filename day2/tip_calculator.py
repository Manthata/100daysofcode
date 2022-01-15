# Manthata William 
# Day 2 of 100 days of code
# Tip calculator 


# what is the total bill 

total_bill = int(input("How much was your total bill? "))

# What percentage would you like to give 

percentage = int(input("What percentage would you like to give? 10, 12 or 15 "))

#How many people 

num_people = int(input("How many people should pay? "))

tip = (total_bill*(percentage/100))/num_people

print(f"each person should pay ${tip} for tip")

 
