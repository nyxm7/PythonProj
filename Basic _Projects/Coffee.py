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
def money():
    quarter = float(input("How many quarters ?"))
    dimes = float(input("How many dimes ?"))
    nickel = float(input("How many nickels ?"))
    pennies = float(input("How many quarters ?"))
    total_money = (pennies * 0.01)+(quarter * 0.25)+(dimes * 0.10)+(nickel * 0.05)
    return total_money
def check_inventory(choice1):
    for items in MENU[choice1]["ingredients"]:
        if MENU[choice1]["ingredients"][items] < resources[items]:
            print(f"Not enough {items}")
            return False
def coffee(choice1):
    if choice1 == "espresso":
        change = money()
        change -= MENU[choice1]["cost"]
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
        for items in MENU[choice1]["ingredients"]:

#print(travel_log["Germany"]["cities_visited"][2])
state = True
while state:
     choice = input("What would you like? (espresso/latte/cappuccino")
