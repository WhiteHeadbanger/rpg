from random import randint, choice
from base_classes import Player, Shop
import mechanics, menu
from consolemenu.screen import Screen

"""
TO-DO
* 

"""

def main(pj=None):
    if pj is None:
        pjName = input("Tu nombre: ")
        pj = Player(pjName, 5, 1, 0, 0, 100, 1, 0, 100, 0, 0, 0, 0, 100)

    mob = mechanics.instance_mob()
    Screen.printf("Proximo oponente: {}\n".format(mob.name))
    shop = Shop()

    while True:
        menu.main_menu(pj, mob, shop)
        if mob.hp <= 0 or pj.hp <= 0:
            break
    
    if pj.wins >= 1 and pj.hp > 0:
        main(pj)
    else:
        if pj.wins > 0:
            Screen.println("Ganaste "+str(pj.wins)+" peleas!")
        else:
            pass


if __name__ == "__main__":
    main()