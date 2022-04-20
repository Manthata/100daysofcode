

print("Welcome to pizza diliveries")

size = input("What is the size of pizza you want ? S, M or L ")
add_pepperoni = input("would you like to add pepperoni ? Y or N ")
extra_cheese = input("would you like to have extra cheeze ? Y or N")

if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price +=2
    if extra_cheese == "Y":
        price +=1
    print(f"Your pizza price is ${price}")

elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price +=3
    if extra_cheese == "Y":
        price +=1
    print(f"Your pizza price is ${price}")

elif size == "L":
    price = 25
    if add_pepperoni == "Y":
        price +=3
    if extra_cheese == "Y":
        price +=1
    print(f"Your pizza price is ${price}")