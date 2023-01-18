# 29-11-2022 Day 15 Project: Coffee machine
from data import MENU, resources


def print_report():
    """prints the current resource values"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_amount}")


def check_resources(coffee_choice, coffee_resources):
    """checks whether we have enough resources to make the selected coffee
    returns True if we have enough resources else False"""
    remaining_water = coffee_resources["water"] - coffee_choice["ingredients"]["water"]
    remaining_coffee = coffee_resources["coffee"] - coffee_choice["ingredients"]["coffee"]
    if coffee_choice != MENU["espresso"]:
        remaining_milk = coffee_resources["milk"] - coffee_choice["ingredients"]["milk"]
        if remaining_milk < 0:
            print("Sorry there is not enough milk.")
            return False
    if remaining_coffee < 0:
        print("Sorry there is not enough milk.")
        return False

    if remaining_water < 0:
        print("Sorry there is not enough milk.")
        return False
    return True


def make_coffee(coffee_choice, coffee_resources):
    """returns resources remaining after making coffee"""
    coffee_resources["water"] -= coffee_choice["ingredients"]["water"]
    coffee_resources["coffee"] -= coffee_choice["ingredients"]["coffee"]
    if coffee_choice != MENU["espresso"]:
        coffee_resources["milk"] -= coffee_choice["ingredients"]["milk"]
    return coffee_resources


print("Welcome to the coffee machine")
total_amount = 0
should_continue = True  # whether to off the machine
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print_report()
    elif choice == "off":
        should_continue = False
    elif choice in MENU:
        if check_resources(MENU[choice], resources):
            resources = make_coffee(MENU[choice], resources)
            total_amount += MENU[choice]["cost"]
            print(f"Here is your {choice}. Enjoy!")
    else:
        print("Invalid selection")
