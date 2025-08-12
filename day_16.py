            # Object-Oriented Programming (OOP)
# This is breaking down a large project into modules that can be worked on by different people.
# The modules are scalable and/or reusable in other projects too.
# It's called OOP because it models a real world object.
# An OOP has two important things:
# Attributes - what it has i.e., variables associated with the modelled object
# Methods - what it does i.e., functions associated with the object. defines what the object does.
# Class - Different/multiple versions of the same object. This common object is the class.

        # Constructing an object & accessing their Attributes and Methods
# car = CarBlueprint():  # classes are written with pascal case to differentiate it with other functions
            ##  Let's look at Turtle Graphics

# from turtle import Turtle, Screen #(Turtle and Screen are classes)
# timmy = Turtle() # Turtle is the class which activates the construction of the object(which is Timmy).
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100.0)
# #   What can we do with the above object
# my_screen = Screen() #Screen() is the class, my_screen is the object built by the class.
# # how do we find the attributes of my_screen???
# print(my_screen.canvheight)
# # The above code identifies the obejct(my_screen) and its canvheight attribute(height of the screen canvas).
#
#     # Object Methods
# my_screen.exitonclick()

            ## Python Packages
            # PyPI = Python Package Index
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("City Name", ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
# table.align = "l"
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine.report()
coffee_maker.report()

machine_on = True
while machine_on == True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:\n")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)