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


machine_on = True
profit = 0

def sufficiency(order_ingredients):
    """Returns True if order can be made and False if resources are insuffient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns value of total coins inserted"""
    print("Please insert coins:")
    total = int(input("How many quarters?:\n")) * 0.25
    total += int(input("How many dime?:\n")) * 0.1
    total += int(input("How many nickels?:\n")) * 0.05
    total += int(input("How many pennies?:\n")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted or False when money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink {drink_name} ☕.")

while machine_on == True:
    choice = input("What would you like? Espresso/Latte/Cappuccino:\n").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if sufficiency(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])