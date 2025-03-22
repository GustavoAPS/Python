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
    "money": 0.00,
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water :{resources['water']}ml")
    print(f"milk :{resources['milk']}ml")
    print(f"coffee :{resources['coffee']}g")


coffee_option = input("What is your coffee?(espresso,latte,cappuccino)")

# 0.25
quarters = float(input("How many quarters?"))
# 0.10
dimes = float(input("How many dimes?"))
# 0.05
nickles = float(input("How many nickles?"))
# 0.01
pennies = float(input("How many pennies?"))

resources["money"] = (quarters*0.25)+(dimes*0.10) + (nickles*0.05) + (pennies*0.01)
# print(resources["money"])

# still need to be implemented
def use_ingredients(water, coffee, milk):

    if resources["water"] >= water:
        resources["water"] -= water
    else:
        return False
    if resources["coffee"] >= coffee:
        resources["coffee"] -= coffee
    else:
        return False
    if resources["milk"] >= milk:
        resources["milk"] -= milk
    else:
        return False
    return True


if coffee_option == "espresso":

    print("espresso selected")
    if(MENU["espresso"]["cost"]) <= (resources["money"]):
        print("Here is your espresso")
        print(f"Your change is: ${(resources['money']) - (MENU['espresso']['cost'])}")
    else:
        print("Not enough coins")

elif coffee_option == "latte":
    print("latte selected")
    if(MENU["latte"]["cost"]) <= (resources["money"]):
        print("Here is your latte")
        print(f"Your change is: ${(resources['money']) - (MENU['espresso']['cost'])}")
    else:
        print("Not enough coins")

elif coffee_option == "cappuccino":
    print("cappuccino selected")
    if(MENU["cappuccino"]["cost"]) <= (resources["money"]):
        print("Here is your cappuccino")
        print(f"Your change is: ${(resources['money']) - (MENU['espresso']['cost'])}")
    else:
        print("Not enough coins")

else:
    report()
