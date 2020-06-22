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
    
    def __init__(self, name, attack, magic_attack, armor, magic_armor, hp_max, exp, level):
        super().__init__(name, attack, magic_attack, armor, magic_armor, hp_max, exp, level)
        self.level = 1



class Player(Character):

    def __init__(self, name, attack, magic_attack, armor, magic_armor, hp_max, level, exp, mana_max, mana, crit_chance, crit_damage, speed, hp):
        super().__init__(name, attack, magic_attack, armor, magic_armor, hp_max, level)
        self.level = 1
        self.exp = exp
        self.mana = mana
        self.mana_max = mana_max
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
            self.mana_max += item.mana_max
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
    
    def __init__(self, name, value, rarity):
        self.name = name
        self.value = value
        self.rarity = rarity

    def __str__(self):
        return f"{self.name} - {self.value}G - {self.rarity}"

class Consumables(Item):

    def __init__(self, name, value, rarity, hp, mana, _type):
        super().__init__(name, value, rarity)
        self.hp = hp
        self.mana = mana
        self._type = _type


class Weapons(Item):
    
    def __init__(self, name, value, rarity, attack, magic_attack, crit_chance, crit_damage, state):
        super().__init__(name, value, rarity)
        self.attack = attack
        self.magic_attack = magic_attack
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.state = state

class Armors(Item):

    def __init__(self, name, value, rarity, armor, magic_armor, hp_max, mana_max, state):
        super().__init__(name, value, rarity)
        self.armor = armor
        self.magic_armor = magic_armor
        self.hp_max = hp_max    
        self.mana_max = mana_max
        self.state = state
        



