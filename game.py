from random import randint, choice

# Diccionario con todos los monstruos
MONSTERS = {"orco":{"ataque":3, "hp":100}, "elfo":{"ataque":5, "hp":90}, "hombre lobo":{"ataque":7, "hp":120}}

#CLASES
class Character:
    def __init__(self, atk, hp, exp):
        self.atk = atk
        self.hp = hp
        self.exp = exp
        self.inv = {"pocion":3}
    
    def attack(self, monster):
        monster.hp = monster.hp - (self.atk * randint(0, 5))

class Monster:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def attack(self, character):
        character.hp = character.hp - (self.atk * randint(0, 5))

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

#---------------------------------------------#
# EL JUEGO EN SI #
#---------------------------------------------#
def main():
    # Instancia de jugador
    pj = Character(atk=5, hp=100, exp=0)
    # Elegimos un monstruo al azar
    monstername, monsterstats = choose_monster(MONSTERS)
    # Instancia del monstruo
    mon = Monster(monstername, monsterstats["ataque"], monsterstats["hp"])
    pjName = input("Cual es tu nombre? ")
    wins = 0
    # Instancia de poción de vida
    pocion = Item("pocion", 50)
    while True:
        print("Turno de "+pjName)
        print("1. Pelear")
        print("2. Curarse")
        print("3. Salir")

        opc = int(input(">: "))
        if opc == 1:
            pj.attack(mon)
            print("El "+mon.name+" fue atacado y le quedan "+str(mon.hp)+" puntos de vida!")
            if mon.hp <= 0:
                print("Ganaste!")
                wins =+ 1
                break
        elif opc == 2:
            if pj.inv["pocion"] == 0:
                print("No tenes mas pociones!")
            else:
                pj.hp += pocion.value
                pj.inv["pocion"] -= 1
                print("Te curaste "+str(pocion.value)+" puntos de vida!")
                print("Te quedan "+str(pj.inv["pocion"])+ " pociones!")
        elif opc == 3:
            break

        
        mon.attack(pj)
        print(pjName+" fue atacado y le quedan "+str(pj.hp)+" puntos de vida!")

        if pj.hp <= 0:
            print("Perdiste!")
            break
        else:
            pass
    
    print("Ganaste "+str(wins)+" peleas!")

def choose_monster(MONSTERS):
    monsterName, monsterStats = choice(list(MONSTERS.items()))
    return (monsterName, monsterStats)








if __name__ == "__main__":
    main()