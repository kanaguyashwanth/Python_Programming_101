    """
    FEATURES OF THE COFFEE MACHINE:
    - 3 Hot flavors
        - Espresso     $1.50    (50 ml water, 18g coffee)
        - Latte        $2.50    (200 ml water, 24g coffee, 150 ml milk)
        - Cappuccino   $3.00    (250 ml water, 24g coffee, 100 ml milk)
    
    - Tank: (Minimum)
        - Water:  300 ml
        - Milk:   200 ml
        - Coffee: 100g
    
    - Coins operated: (US)
        - Penny   (1 Cent)
        - Nickel  (5 Cents)
        - Dime    (10 Cents)
        - Quarter (25 Cents)
    
    - PROGRAMMING REQUIREMENTS: [IMPORTANT]
    1. Print Report (How much resources are left?) - Type 'Report'
    2. Check resources are sufficient? - Tells the user that there are less/no resources
    3. Process coins - less money, then return money. If more money, then return the change
    4. Successful transaction?
    
    - Automatic cup dispenser
    - Counting cup selling
    
    Analytic Table:
    - Water inlet
    - Coin slot
    - Coin acceptor
    - LCD
    - Drink 1
    - Drink 2
    - Drink 3
    - +
    - -
    - Menu
    - Drink Outlet
    - Waste water box
    """



    # CODE:
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }


    def coffee_machine():
        # TODO: 1. Prompting User
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
            # TODO 5. Process coins
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            dollars = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

            if dollars >= MENU[user_input]['cost']:
                change = dollars - MENU[user_input]['cost']
                change = round(change, 2)

                for key in MENU[user_input]['ingredients']:

                    if ( (resources[key]) - (MENU[user_input]['ingredients'][key]) > 0 ):
                        resources[key] = resources[key] - MENU[user_input]['ingredients'][key]
                        resources_flag = 'Sufficient'
                    else:
                        resources_flag = 'Insufficient'
                        insuff_ingred = key

                if resources_flag == 'Sufficient':
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {user_input}. Enjoy!")
                    coffee_machine()
                elif resources_flag == 'Insufficient':
                    print(f"Sorry, there is not enough {insuff_ingred}")
                    exit()

            else:
                print("Sorry, that's not enough money. Money refunded.")

        # TODO 3. Print Report.
        if user_input == 'report':
            for key in resources:
                print(f"{key}: {resources[key]}")
            coffee_machine()

        # TODO 4. Check resources.



    coffee_machine()
