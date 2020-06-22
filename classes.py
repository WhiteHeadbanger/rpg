from random import randint

class Character:
    
    def __init__(self, name, attack, magic_attack, armor, magic_armor, hp_max, level):
        self.name = name
        self.attack = attack
        self.magic_attack = magic_attack
        self.armor = armor
        self.magic_armor = magic_armor
        self.hp_max = hp_max
        self.level = level
        self.inv = {"pocion":3}
        self.wins = 0
        self.gold = 100 
    
    def _baseattack(self, target):
        target.hp -= (self.attack + randint(0, 5)) * self.level
            

class Monster(Character):
    
    def __init__(self, name, attack, magic_attack, armor, magic_armor, hp_max, exp):
        super().__init__(name, attack, magic_attack, armor, magic_armor, hp_max, exp, level=1)



class Player(Character):

    def __init__(self, name, attack, magic_attack, armor, magic_armor, hp_max, exp, mana, crit_chance, crit_damage, speed, hp):
        super().__init__(name, attack, magic_attack, armor, magic_armor, hp_max, level=1)
        self.exp = exp
        self.mana = mana
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.speed = speed
        self.hp = hp
        self.inventory = []

    def show_inventory(self):
        for item in self.inventory:
            f"{item}"

    def equip_item(self, item):
        # Si el item no está equipado
        if item.state == False:
            # Equiparlo
            item.state = True
            # Y aumentar los stats
            self.attack += item.attack
            self.magic_attack += item.magic_attack
            self.armor += item.armor
            self.magic_armor += item.magic_armor
            self.mana += item.mana
            self.crit_chance += item.crit_chance
            self.crit_damage += item.crit_damage
            self.speed += item.speed
            self.hp_max += item.hp_max
        else:
            print("Este item ya esta equipado.")
    
    def use_item(self, item):
        if item.type == "C": # Consumable
            self.inventory # remover item del inventario (completar cuando tenga internet, no recuerdo como remover de listas)
            self.mana += item.mana
            self.hp += item.hp
        else:
            print("Este item no se puede usar.")
            
    def move(self):
        pass

    def exp_gain(self, expAmount):
        self.exp += expAmount
        if self.exp >= 100:
            self.level += 1
            print("Subiste al nivel "+str(self.level))
            if self.exp > 100:
                self.exp -= 100


class Item:
    
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Consumables(Item):

    def __init__(self, name, value, hp, mana, type="C"):
        super().__init__(name, value)
        self.hp = hp
        self.mana = mana


class Weapons(Item):
    
    def __init__(self, name, value, attack, magic_attack, crit_chance, crit_damage, state):
        super().__init__(name, value)
        self.attack = attack
        self.magic_attack = magic_attack
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.state = state
        

asd = Weapons(1, 1, 1, 1, 1, 1, True)
#asd.state = True
print(asd.state)


