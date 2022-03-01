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

# TODO 1 Take Input from the user
# Take input what to do next
# The prompt always run after function
user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO 2. Making report (if user type report print all the resources and money)

money = 0  # StartingMoney


# Defining function for report
def report(resource, balance):
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${balance}")


if user_choice == 'report':
    print(report(resources, money))

# TODO 3.Check how much resources left before making coffee


# for latte
def check_resources(resource, user_input, menu=MENU):
    """
    :param resource: fresh resource or left resource
    :param user_input: What user inputted (espresso/latte/cappuccino)
    :param menu: default MENU constant
    :return:
    """
    item = menu[user_input]
    if resource["water"] < item['ingredients'['water']]:






