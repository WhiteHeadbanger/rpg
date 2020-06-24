from instances import consumableClasses, weaponsClasses, armorsClasses

def menu():
    print("1. Fight")
    print("2. Character")
    print("3. Inventory")
    print("4. Shop")
    print("5. Quit")
    ch = int(input(">: "))
    return ch

def fight_menu():
    print("1. Physical Attack")
    print("2. Spells")
    print("3. Inventory")
    print("4. Run")
    ch = int(input(">: "))
    return ch

def shop_menu():
    
    def shop_consumables():
        for i in consumableClasses:
            print(i)
    
    def shop_weapons():
        for i in weaponsClasses:
            print(i)

    def shop_armors():
        for i in armorsClasses:
            print(i)
    
    print("Welcome to the shop!")
    print("1. Consumables")
    print("2. Weapons")
    print("3. Armor")

    

    ch = int(input(">: "))
    if ch == 1:
        shop_consumables()
    elif ch == 2:
        shop_weapons()
    elif ch == 3:
        shop_armors()
    else:
        return

    
