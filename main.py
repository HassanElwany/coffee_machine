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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient(order_ingredients):
    for key in order_ingredients:
        if order_ingredients[key] > resources[key]:
            print(f"Sorry not enough {key}")
            return False
    return True


def coins():
    print("Insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_machine(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"pick up your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry you can afford this drink")

        return False


def make_coffee(drink_name, order_ingredients):
    for key in order_ingredients:
        resources[key] -= order_ingredients[key]
    print(f" here are your {drink_name}")


is_on = True

while is_on:

    user_drink = input(" What would you like? (espresso/latte/cappuccino):  ")
    if user_drink == "off":
        is_on = False
    elif user_drink == "report":

        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: $ {profit}")
    else:
        drink = MENU[user_drink]
        if sufficient(drink["ingredients"]):
            payment = coins()
            if transaction_machine(payment, drink['cost']):
                make_coffee(user_drink, drink['ingredients'])
