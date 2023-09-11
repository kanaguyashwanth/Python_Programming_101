"""
STEPS:
1. Print report
2. Check resources sufficient
3. Process coins
4. Check transaction successful
5. Make coffee
"""


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Creating Objects from these Classes               [ object = Class() ]  [ NOTE: object is in lowercase ]
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# Calling the Methods from Objects                  # [ object.method() ]
money_machine.report()                              # Making money machine to create a report
coffee_maker.report()
# option = input(f"Choose {menu.get_items()}: ")    # menu.get_items returns "latte/espresso/cappuccino"
# menu.find_drink('latte')


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()                       # Displays the ingredients left
        money_machine.report()                      # Displays the profit made
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)
