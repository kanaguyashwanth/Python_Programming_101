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


# KEEPING COFFEE MACHINE TURNED ON
is_on = True

# MAKING COFFEE
while is_on:
    # ACCESSING ATTRIBUTES:
    choice = input(f"Select drink{menu.get_items()}: ")
    drink = menu.find_drink(choice)             # [ Prints "Sorry that item is not available." if the item is NOT available. ]

    if choice == "off":
        # EXIT LOOP
        is_on = False
    elif choice == "report":
        # PRINTING REPORT
        money_machine.report()                  # [ Prints NET PROFIT amount ]
        coffee_maker.report()                   # [ Prints RESOURCES needed ]
    else:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
