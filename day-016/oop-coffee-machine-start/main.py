from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            payment = money_machine.process_coins()
            if money_machine.make_payment(payment):
                coffee.make_coffee(drink)

