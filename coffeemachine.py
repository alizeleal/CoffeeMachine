from data import MENU
from data import resources
from data import coins





def makeCoffee(coffee):
    """Makes the Selected Coffee"""
    resources["water"] -= MENU[f"{coffee}"]["ingredients"]["water"]
    resources["coffee"] -= MENU[f"{coffee}"]["ingredients"]["coffee"]
    if "milk" in MENU[f"{coffee}"]:
        if resources["milk"] >= MENU[f"{coffee}"]["ingredients"]["milk"]:
            resources["milk"] -= MENU[f"{coffee}"]["ingredients"]["milk"]
            return True
        else:
            return False
    else:
        return True
    
def checkResources(coffee):
    """Checks if there are enough resources to make the coffee."""
    if resources["water"] >= MENU[f"{coffee}"]["ingredients"]["water"] & resources["coffee"]>=MENU[f"{coffee}"]["ingredients"]["coffee"] :
        if "milk" in MENU[f"{coffee}"]:
            if resources["milk"] >= MENU[f"{coffee}"]["ingredients"]["milk"]:
                return True
            else:
                print("Sorry, there's not enough coffee.")
                return False
        return True
    elif resources["water"] < MENU[f"{coffee}"]["ingredients"]["water"] :
        print("Sorry, there's not enough water.")
        return False
    else:
        print("Sorry, there's not enough coffee.")
        return False        

    
def showReport():
    """Show the current resources levels"""
    print(resources)

def countMoney(coffee):
    """Receives payment and checks if it's enough to pay for the order"""
    print("Please insert the coins to pay  for your order:")
    quartersInserted = float(input("Quarters: "))
    dimesInserted = float(input("Dimes: "))
    nicklesInserted = float(input("Nickles: "))
    penniesInserted = float(input("Pennies: "))
    totalInserted = quartersInserted * coins["quarter"] + dimesInserted * coins["dime"]  + nicklesInserted * coins["nickel"]  + penniesInserted * coins["penny"]  
    if totalInserted <  MENU[f"{coffee}"]["cost"]:
        print("\nSorry, that's not enough money. Money refunded.")
        return False
    elif totalInserted ==  MENU[f"{coffee}"]["cost"]:
        return True
    else:
        print(f"\nYour change is: $ {round(totalInserted - MENU[f"{coffee}"]["cost"], 2)}.")
        return True
    
def refill():
    """Update the resources"""
    resources["water"] += int(input("\nHow much more water are you adding? In milliliters "))
    resources["milk"] += int(input("\nHow much more milk are you adding? In milliliters "))
    resources["coffee"] += int(input("\nHow much more coffee are you adding? In grams "))
    print(f"\nThe current resources levels are: {resources}")



def coffeeMachine():
    """This function is the main function of the coffee machine program."""
    order = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    print(f"\nYou chose: {order}\n")
    if order == "report":
        showReport()
    elif order == "refill":
        refill()
    elif order == "off":
        print("\nTurning off...\n")
        return False
    else:
        enoughResources = checkResources(order)
        if enoughResources:
            money = countMoney(order)
            if money:
                makeCoffee(order)
                print(f"Here's your {order}! Enjoy!")
            else:
                print("\nIt wasn't possible to proccess your order.")
        else:
                print("\nIt wasn't possible to proccess your order.")
    coffeeMachine()

coffeeMachine()








    



