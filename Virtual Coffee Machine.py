MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        }
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        }
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        }
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def payment():
    print("Please insert coins.")
    quarter = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarter*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    return total

def change_espresso(x):
    total = x - 1.5
    return total

def change_latte(x):
    total = x - 2.5
    return total

def change_cappuccino(x):
    total = x - 3
    return total

def espresso():
    money = payment()
    missing = []
    for item, amount_needed in MENU["espresso"]["ingredients"].items():
        if resources.get(item, 0) < amount_needed:
            missing.append(item)
    if missing:
        return f"Sorry, there is not enough: {', '.join(missing)}"
    if money < 1.5:
        return "Sorry that's not enough money. Money refunded"
    print(f"Here is ${round(change_espresso(money), 2)} in change.")
    print("Here is your espresso ☕️. Enjoy!")
    for item, amount_needed in MENU["espresso"]["ingredients"].items():
        resources[item] -= amount_needed
    return None

def latte():
    money = payment()
    missing = []
    for item, amount_needed in MENU["latte"]["ingredients"].items():
        if resources.get(item, 0) < amount_needed:
            missing.append(item)
    if missing:
        return f"Sorry, there is not enough: {', '.join(missing)}"
    if money < 2.5:
        return "Sorry that's not enough money. Money refunded"
    print(f"Here is ${round(change_latte(money), 2)} in change.")
    print("Here is your latte ☕️. Enjoy!")
    for item, amount_needed in MENU["latte"]["ingredients"].items():
        resources[item] -= amount_needed
    return None

def cappuccino():
    money = payment()
    missing = []
    for item, amount_needed in MENU["cappuccino"]["ingredients"].items():
        if resources.get(item, 0) < amount_needed:
            missing.append(item)
    if missing:
        return f"Sorry, there is not enough: {', '.join(missing)}"
    if money < 3:
        return "Sorry that's not enough money. Money refunded"
    print(f"Here is ${round(change_cappuccino(money), 2)} in change.")
    print("Here is your cappuccino ☕️. Enjoy!")
    for item, amount_needed in MENU["cappuccino"]["ingredients"].items():
        resources[item] -= amount_needed
    return None

def report(money):
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")

cash = 0
coffee = True
while coffee:
    action = input("\n\nMENU\n\nespresso - $1.5\nlatte - $2.5\ncappuccino - $3.0\n\nWhat would you like? ").lower()
    if action == "report":
        report(cash)
    elif action == "off":
        coffee = False
    elif action == "espresso":
        result = espresso()
        if result is None:
            cash += 1.5
        else:
            print(result)
    elif action == "latte":
        result = latte()
        if result is None:
            cash += 2.5
        else:
            print(result)
    elif action == "cappuccino":
        result = cappuccino()
        if result is None:
            cash += 3
        else:
            print(result)