from random import randint, choice

# Diccionario con todos los monstruos
MONSTERS = {"orco":{"ataque":3, "hp":100, "exp":20}, "elfo":{"ataque":5, "hp":90, "exp":40}, "hombre lobo":{"ataque":7, "hp":120, "exp":60}}

#CLASES
class Character:
    def __init__(self, name, atk, hp, exp, lvl):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.exp = exp
        self.lvl = lvl
        self.inv = {"pocion":3}
        self.wins = 0
    
    def attack(self, monster):
        monster.hp -= (self.atk + randint(0, 5)) * self.lvl

    def expgain(self, monster):
        self.exp += monster.exp
        if self.exp >= 100:
            self.lvl += 1
            print("Subiste al nivel "+str(self.lvl))
            if self.exp > 100:
                self.exp -= 100
            

class Monster:
    def __init__(self, name, atk, hp, exp):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.exp = exp

    def attack(self, character):
        character.hp -= (self.atk * randint(0, 5))


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def menu():
    print("1. Pelear")
    print("2. Curarse")
    print("3. Salir")
    opc = int(input(">: "))
    return opc

def pj_attack(_mon, _pj):
    _pj.attack(_mon)
    print("El "+_mon.name+" fue atacado y le quedan "+str(_mon.hp)+" puntos de vida!")
    return _pj

def mon_attack(_mon, _pj):
    _mon.attack(_pj)
    print(_pj.name+" fue atacado y le quedan "+str(_pj.hp)+" puntos de vida!")
    return _mon

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

def instance_player(_pjName):
    pjIns = Character(name=_pjName, atk=5, hp=100, exp=0, lvl=1)
    return pjIns

def instance_monster():
    monstername, monsterstats = choose_monster()
    monIns = Monster(monstername, monsterstats["ataque"], monsterstats["hp"], monsterstats["exp"])
    return monIns

def choose_monster():
    monsterName, monsterStats = choice(list(MONSTERS.items()))
    return (monsterName, monsterStats)

def main(pj=None):
    if pj is None:
        pjName = input("Tu nombre: ")
        pj = instance_player(pjName)
    else:
        pj = pj
    mon = instance_monster()
    # Instancia de poción de vida
    pocion = Item("pocion", 100)
    while True:
        opc = menu()
        if opc == 1:
            pj = pj_attack(mon, pj)
            if mon.hp <= 0:
                pj.wins += 1
                break
        elif opc == 2:
            use_pot(pj, pocion)
        elif opc == 3:
            return False

        mon = mon_attack(mon, pj)

        if pj.hp <= 0:
            print("Perdiste!")
            break
        else:
            pass
    
    if pj.wins >= 1 and pj.hp > 0:
        main(pj)
    else:
        print("Ganaste "+str(pj.wins)+" peleas!")











if __name__ == "__main__":
    main()