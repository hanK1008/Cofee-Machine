MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# TODO 1 Take Input from the user
# Take input what to do next
# The prompt always run after function


machine_on = True
money = 0  # StartingMoney
while machine_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()


# TODO 2. Making report (if user type report print all the resources and money)


# Defining function for report


    def report(resource, balance):
        water = resource["water"]
        milk = resource["milk"]
        coffee = resource["coffee"]
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${balance}")


    # if user_choice == 'report':
    #     print(report(resources, money))


# TODO 3.Check how much resources left before making coffee


    def check_resources(resource, user_drink, menu=MENU, ):
        """
        :param resource: fresh resource or left resource
        :param user_drink: What user inputted (espresso/latte/cappuccino)
        :param menu: default MENU constant
        :return: What resources are not enough for making drink / is all good return 'True'
        """
        item = menu[user_drink]
        if resource["water"] < item['ingredients']['water']:
            return 'Sorry there is not enough water'
        elif resource["milk"] < item['ingredients']['milk']:
            return 'Sorry there is not enough milk'
        elif resource["coffee"] < item['ingredients']['coffee']:
            return 'Sorry there is not enough coffee'
        else:
            return True


    # print(check_resources(resources, user_choice))


# TODO 4. calculate coins as machine is coin operated if user insert enough coin
    # Use all coins with values: quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01


    def calculate_coins():
        """
        :return: Sum of how much coins user inserted in the machine
        """
        quarters = int(input("Please insert coins.\nHow many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles*0.05) + (pennies*0.01)
        return total


    # inserted_money = calculate_coins()


# TODO 5. complete the transaction by comparing inserted money and price of drink


    def transaction(user_inserted_money, user_drink, menu=MENU):
        """
        :param user_inserted_money: money inserted by user (inserted_money)
        :param user_drink: User choice of drink (espresso/latte/cappuccino)
        :param menu: Menu of the drinks and prices (MENU)
        :return:
        """
        if menu[user_drink]['cost'] > user_inserted_money:
            return False
        else:
            return True


    # successful_transaction = transaction(inserted_money, user_choice)
    # print(successful_transaction)

    if user_choice == 'report':  # It will print the report
        report(resources, money)

    elif user_choice == 'off':  # It will flip the switch and programme will be stopped
        machine_on = False

    else:
        proceed = check_resources(resources, user_choice)
        if proceed == True:
            inserted_money = calculate_coins()
            successful_transaction = transaction(inserted_money, user_choice)
            drink_cost = MENU[user_choice]['cost']
            refund_money = round((inserted_money - drink_cost), 2)

            if successful_transaction:
                print(f"Here is ${refund_money} in change ")
                print(f"Here is your {user_choice} ☕ , Enjoy\n")
                # TODO 7: After making coffee balanced out the resource
                user_drink = MENU[user_choice]["ingredients"]
                resources["water"] -= user_drink["water"]
                resources["milk"] -= user_drink["milk"]
                resources["coffee"] -= user_drink["coffee"]
                money += drink_cost
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            print(proceed)



# TODO 6: Make coffee and refund money

    # drink_cost = MENU[user_choice]['cost']
    # refund_money = round((inserted_money - drink_cost), 2)
    #
    # if successful_transaction:
    #     print(f"Here is ${refund_money} in change ")
    #     print(f"Here is your {user_choice} ☕ , Enjoy")
    #     # TODO 7: After making coffee balanced out the resource
    #     user_drink = MENU[user_choice]["ingredients"]
    #     resources["water"] -= user_drink["water"]
    #     resources["milk"] -= user_drink["milk"]
    #     resources["coffee"] -= user_drink["coffee"]
    #     money += drink_cost
    # else:
    #     print("Sorry that's not enough money. Money refunded")
    #
    # print(resources)










