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
def resources_left(prompt):
    """this will check if machine has enough resources"""
    user_drink = MENU[prompt]['ingredients'].items()
    for my_resource, value in user_drink:
        if resources[my_resource]< value:
            print(f'Sorry there is not enough {my_resource}')
            return False
    for my_resource, value in user_drink:
        resources[my_resource]-=value
    return True

profit = 0
def calculate(prompt):
    """this will calculate if your user's money is enough or not"""
    print('Please insert coins.')
    quarter = int(input('How many quarters?: '))
    dime = int(input('How many dimes?: '))
    nickle = int(input('How many nickles?: '))
    penny = int(input('How many pennies?: '))
    sum_coins = quarter*0.25 + dime*0.10 + nickle*0.05 + penny*0.01
    cost = MENU[prompt]['cost']
    if sum_coins<cost:
        print('Sorry that\'s not enough money. Money refunded.')
        return False
    else:
        global profit
        profit= round(profit + cost, 2)
        user_change = sum_coins - cost
        if user_change == 0:
            print('You have no change.')
            return True
        else:
            print(f'Here is ${round(user_change, 2)} in change.')
            print(f'Here is your {prompt}. Enjoy!')
            return True

def refund(prompt):
    user_drink = MENU[prompt]['ingredients'].items()
    for my_resource, value in user_drink:
        resources[my_resource] += value

def coffee_machine():
    """this is a main coffee machine"""
    while True:
        prompt = input('What would you like? (espresso/latte/cappuccino): ')

        if prompt == 'off':
            break
        elif prompt == 'report':
            for ingredient, value in resources.items():
                if ingredient == 'coffee':
                    print(ingredient.title() + ":", str(value) + "g")
                else:
                    print(ingredient.title() + ":", str(value) + "ml")
            print('$' + str(profit))

        elif prompt not in MENU:
            print("Invalid input. Please try again.")
            coffee_machine()
            break
        elif resources_left(prompt) == False:
            print('Choose another option')
            coffee_machine()
            break
        elif calculate(prompt) == False:
            refund(prompt)
            coffee_machine()
            break
        else :
            continue

coffee_machine()




