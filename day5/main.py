from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# First task, I need to print the report 

menu = Menu()
coffemaker = CoffeeMaker()
moneymachine = MoneyMachine()
machine_on = True
print(f"Financial report: {moneymachine.report()}")
print()
print(f"Coffee report: {coffemaker.report()}")

while machine_on:
    print()
    options = menu.get_items()
    print("Which hot beverage would you like to have? ")
    choice = input("please type in the beverage : ")
    # check if we have the beverage
    drink = menu.find_drink(choice)
    if menu.find_drink(choice):
        drink = menu.find_drink(choice)
        print(f"Your beverage costs {drink.cost}")
        suffient = coffemaker.is_resource_sufficient(drink)
        if suffient:
            print("We have the appropriate resources for your drink")
        else:
            print(f"Sorry, we are currently out of resources to make {choice}")
            break
        # check if the money is enough
        money_enough = moneymachine.make_payment(drink.cost)
        coffemaker.make_coffee(drink)
        machine_on = False
    else:
        break
   


