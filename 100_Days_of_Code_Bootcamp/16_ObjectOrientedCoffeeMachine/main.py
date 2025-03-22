from coffee import Coffee
from coffeeMachine import CoffeeMachine


# Declaring coffees values ## coment
espresso_coffee = Coffee
espresso_coffee.name = "espresso"
espresso_coffee.water_requirement = 50
espresso_coffee.milk_requirement = 0
espresso_coffee.coffee_requirement = 18
espresso_coffee.cost = 1.5

latte_coffee = Coffee
latte_coffee.name = "latte"
latte_coffee.water_requirement = 200
latte_coffee.milk_requirement = 150
latte_coffee.coffee_requirement = 24
latte_coffee.cost = 2.5

cappuccino_coffee = Coffee
cappuccino_coffee.name = "cappuccino"
cappuccino_coffee.water_requirement = 250
cappuccino_coffee.milk_requirement = 100
cappuccino_coffee.coffee_requirement = 24
cappuccino_coffee.cost = 3.0

royal_coffee_machine = CoffeeMachine()


def report():
    print(f"Water :{royal_coffee_machine.water_in_tank}ml")
    print(f"milk :{royal_coffee_machine.milk_in_tank}ml")
    print(f"coffee :{royal_coffee_machine.coffee_in_tank}g")


coffee_option = input("What is your coffee?(espresso,latte,cappuccino)")

# 0.25
quarters = float(input("How many quarters?"))
# 0.10
dimes = float(input("How many dimes?"))
# 0.05
nickles = float(input("How many nickles?"))
# 0.01
pennies = float(input("How many pennies?"))

royal_coffee_machine.money_stored = (quarters*0.25)+(dimes*0.10) + (nickles*0.05) + (pennies*0.01)
# print(resources["money"])


# still need to be implemented
def use_ingredients(water, coffee, milk):

    if royal_coffee_machine.water_in_tank >= water:
        royal_coffee_machine.water_in_tank -= water
    else:
        return False
    if royal_coffee_machine.coffee_in_tank >= coffee:
        royal_coffee_machine.coffee_in_tank -= coffee
    else:
        return False
    if royal_coffee_machine.milk_in_tank >= milk:
        royal_coffee_machine.milk_in_tank -= milk
    else:
        return False
    return True


if coffee_option == "espresso":

    print("espresso selected")
    if espresso_coffee.cost <= royal_coffee_machine.money_stored:
        print("Here is your espresso")
        print(f"Your change is: ${royal_coffee_machine.money_stored - espresso_coffee.cost}")
    else:
        print("Not enough coins")

elif coffee_option == "latte":
    print("latte selected")
    if latte_coffee.cost <= royal_coffee_machine.money_stored:
        print("Here is your latte")
        print(f"Your change is: ${royal_coffee_machine.money_stored - latte_coffee.cost}")
    else:
        print("Not enough coins")

elif coffee_option == "cappuccino":
    print("cappuccino selected")
    if cappuccino_coffee.cost <= royal_coffee_machine.money_stored:
        print("Here is your cappuccino")
        print(f"Your change is: ${royal_coffee_machine.money_stored - cappuccino_coffee.cost}")
    else:
        print("Not enough coins")

else:
    report()
