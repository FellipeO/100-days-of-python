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

def machine_report ():
    """Returns a report listing the resources the machine has left"""
    report = ""
    for item in resources:
        report += f"{item}: {resources[item]}{"g" if item == "coffee" else "ml"}\n"
    return report

def resource_check(user_order):
    """Checks if there's enough ingredients for the order. Warns what is missing"""
    for item in MENU[user_order]["ingredients"]:
        if MENU[user_order]["ingredients"][item] > resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True

def resource_manager(user_order):
    """Deducts the resources required for the order from the machine"""
    for item in MENU[user_order]["ingredients"]:
        resources[item] -= MENU[user_order]["ingredients"][item]

def money_handler(user_order):
    """Processes the order by checking if the user gave enough money"""
    order_cost = MENU[user_order]["cost"]
    user_payment = 0
    print("Please insert coins: ")
    user_payment += int(input("How many quarters? "))* 0.25
    user_payment += int(input("How many dimes? ")) * 0.10
    user_payment += int(input("How many nickels? ")) * 0.05
    user_payment += int(input("How many pennies? ")) * 0.01
    if user_payment == order_cost:
        resource_manager(user_order)
        print(f"Here is your {user_order}!")
        return True
    elif user_payment > order_cost:
        resource_manager(user_order)
        print(f"Here is ${round(user_payment - order_cost, 2)} dollars in change!\nHere is your {user_order}!")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

money = 0
on = True
enough_resources = ""
while on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        on = False
    elif order == "report":
        print(f"{machine_report()}money: ${money}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        #enough_resources = resource_check(order)
        if resource_check(order):
            if money_handler(order):
                money += MENU[order]["cost"]
    else:
        print("Invalid option")
