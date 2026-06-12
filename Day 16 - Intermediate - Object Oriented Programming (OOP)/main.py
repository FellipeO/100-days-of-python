from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


on = True
my_menu = Menu()
my_coffe_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
order = ""

while on:
    order = input(f"What would you like? {my_menu.get_items()}: ")
    if order == "off":
        on = False
    elif order == "refill":
        my_coffe_maker.refill_machine()
    elif order == "report":
        my_coffe_maker.report()
        my_money_machine.report()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if my_coffe_maker.is_resource_sufficient(my_menu.find_drink(order)):
            if my_money_machine.make_payment(my_menu.find_drink(order).cost):
                my_coffe_maker.make_coffee(my_menu.find_drink(order))
    else:
        print("Invalid Option")
