# Coffee Machine 

MENU = {
    "espresso" : {
            "ingridients" : {    
        "water" : 50,
        "coffee" : 18,
            },
            "cost" : 1.5
        },  
     
   "latte" : {    
            "ingridients" : {        
        "water" : 200,
        "milk" : 150,
        "coffee": 24,
            },
            "cost" : 2.5
        },
         
   "cappuccino" : {
            "ingridients" : {
        "water" : 250,
        "milk" : 150,
        "coffee": 24,
            },
            "cost" : 3.0
        }
}

coins = [
    {"name": "Penny", "price" : "$0.01"},
    {"name" :"Dime" , "price": "$0.10"},
    {"name" : "Nickel", "price" : "$0.05" },
    {"name" : "Quarter" , "price" : "$0.25" }
]

profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}

def is_resource_sufficient(order_ingridients):
    """Returns the resource sufficiency of the order"""
    for item in order_ingridients:
       if order_ingridients[item] >= resources[item]:
           print(f"sorry there is not enough {item}.")
           return False 
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert coins")
    total = int(input("how many quarters ? : ")) * 0.25
    total += int(input("how many dimes ? : ")) * 0.1
    total += int(input("how many nickles ? : ")) * 0.05
    total += int(input("how many pennies ? : ")) * 0.01
    return total

is_on = True

while is_on:
    choice = input("what would you like? , (espresso/latte/cappuccino):  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}ml")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingridients"]):
            payment = process_coins()
            
        