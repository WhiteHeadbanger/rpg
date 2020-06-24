from random import randint, choice
from base_classes import Monster, Player
from mechanics import *
from menu import *


def mon_death(_mon, _pj):
    print("Ganaste "+str(_mon.exp)+" EXP")
    _pj.expgain(_mon)

def use_pot(_pj, _pocion):
    if _pj.inv["pocion"] == 0:
        print("No tenes mas pociones!")
    else:
        _pj.hp += _pocion.value
        _pj.inv["pocion"] -= 1
        print("Te curaste "+str(_pocion.value)+" puntos de vida!")
        print("Te quedan "+str(_pj.inv["pocion"])+ " pociones!")


def main(pj=None):
    if pj is None:
        pjName = input("Tu nombre: ")
        pj = Player(pjName, 5, 1, 0, 0, 100, 1, 0, 100, 0, 0, 0, 0, 100)

    mob = instance_mob()
    print("Proximo oponente: "+mob.name)

    while True:
        option = menu()
        # Fight
        if option == 1:
            pj._physicalattack(mob)
            print("El "+mob.name+" fue atacado y le quedan "+str(mob.hp)+"/"+str(mob.hp_max)+" puntos de vida!")
            if mob.hp <= 0:
                pj.exp_gain(mob.exp)
                pj.wins += 1
                break
        # Character
        elif option == 2:
            print(pj)
        # Inventory
        elif option == 3:
            pj.show_inventory()
        # Shop
        elif option == 4:
            shop_menu()
        # Quit
        elif option == 5:
            break

        mob._physicalattack(pj)
        print(pj.name+" fue atacado y le quedan "+str(pj.hp)+"/"+str(pj.hp_max)+" puntos de vida!")
        if pj.hp <= 0:
            print("Perdiste!")
            break
        else:
            pass
    
    if pj.wins >= 1 and pj.hp > 0:
        main(pj)
    else:
        if pj.wins > 0:
            print("Ganaste "+str(pj.wins)+" peleas!")
        else:
            pass


if __name__ == "__main__":
    main()