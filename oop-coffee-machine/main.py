from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
machine = MoneyMachine()

end_of_game = True

while end_of_game:
 
    choose = input(f'choose one of {menu.get_items()}')
    
    if choose == 'off':
        end_of_game = False
        break
    elif choose == 'report':
        coffee_maker.report()
        machine.report()
        continue
    drink = menu.find_drink(choose)
    if drink == None:
        continue

    else:
        if coffee_maker.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
                continue
 