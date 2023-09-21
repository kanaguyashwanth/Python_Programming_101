"""
STEPS:
1. Print report
2. Check resources sufficient
3. Process coins
4. Check transaction successful
5. Make coffee
"""

# IMPORTING MODULES / CLASSES:
from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

# CREATING OBJECTS FROM CLASSES:        [ object = Class() ]
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# ACCESSING ATTRIBUTES:
choice = input(f"Select drink{menu.get_items()}: ")
drink = menu.find_drink(choice)         # [ Prints "Sorry that item is not available." if the item is NOT available. ]

# PRINTING REPORT
money_machine.report()                  # [ Prints NET PROFIT amount ]
coffee_maker.report()                   # [ Prints RESOURCES needed ]

# MAKING COFFEE
if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
    coffee_maker.make_coffee(drink)
