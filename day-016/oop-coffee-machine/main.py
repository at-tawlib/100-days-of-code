from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    options = menu.get_items() # get all items
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee.make_coffee(drink)

