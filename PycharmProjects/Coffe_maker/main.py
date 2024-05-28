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


def is_resources_sufficient(order_ingredients):
    """Checks there are sufficient resources"""
    for item in order_ingredients:
        if resources[item] <= order_ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total coins inserted"""
    print("Insert Coins.")
    total = int(input("Number of quartiles")) * 0.25
    total += int(input("Number of dimes")) * 0.1
    total += int(input("Number of nickles")) * 0.05
    total += int(input("Number of pennies")) * 0.01
    return total


def is_transcation_sucessfull(money_recived, resource_cost):
    global profit
    profit += payment
    change = round(money_recived - resource_cost, 2)
    print(f"Here is ${change} dollars in change.")
    if money_recived >= resource_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(order_ingredients,drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


profit = 0
machine = True

while machine:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == 'off':
        machine = False
    elif order == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]

        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            is_transcation_sucessfull(payment, drink['cost'])
            make_coffee(drink['ingredients'],order)
