from random import randint, choice
from itemdescriptions import items_descriptions
import math
from consolemenu.screen import Screen


class Game:
    
    def __init__(self):
        pass

class Character:
    
    def __init__(self, name, attack, magic_attack, armor, magic_armor, hp_max, level):
        self.name = name
        self.attack = attack
        self.magic_attack = magic_attack
        self.armor = armor
        self.magic_armor = magic_armor
        self.hp_max = hp_max
        self.level = level
        self.wins = 0
        self.gold = 100
    
    def _physicalattack(self, target):
        target.hp -= (self.attack + randint(0, 5)) * self.level
        Screen.println("{} fue atacado y le quedan {}/{} puntos de vida!".format(target.name, target.hp, target.hp_max))
        

    def _magicattack(self, target):
        target.hp -= (self.magic_attack + randint(0, 5)) * self.level
        Screen.println("{} fue atacado y le quedan {}/{} puntos de vida!".format(target.name, target.hp, target.hp_max))

    ## Todo -- hacer el combate completo como metodos

            

class Monster(Character):
    
    def __init__(self, name, attack, magic_attack, armor, magic_armor, hp_max, level, exp, hp):
        super().__init__(name, attack, magic_attack, armor, magic_armor, hp_max, level)
        self.exp = exp
        self.hp = hp
        self.gold_calc = math.ceil(self.gold * 0.5 * self.level)
    
    def _physicalattack(self, target):
        super()._physicalattack(target)
        if target.hp <= 0:
            Screen.println("WASTED")
            return False
        return True

    def drop_item(self):
        item = choice(itemClasses)
        return item
    
    def drop_gold(self, target):
        target.gold += self.gold_calc
        return self.gold_calc
    


class Player(Character):

    def __init__(self, name, attack, magic_attack, armor, magic_armor, hp_max, level, exp, mana_max, mana, crit_chance, crit_damage, speed, hp):
        super().__init__(name, attack, magic_attack, armor, magic_armor, hp_max, level)
        self.exp = exp
        self.mana = mana
        self.mana_max = mana_max
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.speed = speed
        self.hp = hp
        # Agregar magic crit
        self.inventory = {}
        self.equipped_items = []

    def _physicalattack(self, target):
        super()._physicalattack(target)
        if target.hp <= 0:
            self.exp_gain(target.exp)
            self.wins += 1
            Screen.println("Ganaste {}XP".format(target.exp))
            return False
        return True

    def __str__(self):
        return f"Name: {self.name}\nAttack: {self.attack}\nMagic Attack: {self.magic_attack}\nArmor: {self.armor}\nMagic Armor: {self.magic_armor}\nHP: {self.hp}/{self.hp_max}\nMana: {self.mana}/{self.mana_max}\nCritical Chance: {self.crit_chance}\nCritical Damange: {self.crit_damage}\nSpeed: {self.speed}\nLevel: {self.level}\nExperience: {self.exp}\nItems Equipados: {self.equipped_items}"

    def move(self):
        pass
    
    def add_to_inventory(self, item):
        self.inventory.update({item.name:item})

    def show_inventory(self):
        for key in self.inventory.keys():
            Screen.println("{}\n".format(key))
        return self.inventory

    def use_item(self, item):
        if item._type == "C":
            del self.inventory[item.name]
            self.hp += item.hp
            self.mana += item.mana
            Screen.println("Ahora tenés {}HP y {}MP".format(self.hp, self.mana))
        else:
            Screen.println("Este item no se puede consumir")
    
    def examine_item(self, item):
        Screen.println(item.description)

    def buy(self, item_to_buy):
        if self.gold >= item_to_buy.value:
            self.gold -= item_to_buy.value
            self.add_to_inventory(item_to_buy)
            Screen.println("Compraste {}\nTu oro restante: {}".format(item_to_buy.name, self.gold))
        else:
            Screen.println("No tenés oro para comprar ese item")

    def exp_gain(self, expAmount):
        self.exp += expAmount
        if self.exp >= 100:
            self.level += 1
            Screen.println("Subiste al nivel "+str(self.level))
            if self.exp > 100:
                self.exp -= 100


class Item:
    
    def __init__(self, name, value, rarity, _type, description):
        self.name = name
        self.value = value
        self.rarity = rarity
        self._type = _type
        self.description = description


    def show_more(self):
        return f"{self.name} - {self.value}G - {self.rarity}"


class Consumables(Item):

    def __init__(self, name, value, rarity, _type, description, hp, mana):
        super().__init__(name, value, rarity, _type, description)
        self.hp = hp
        self.mana = mana


class Weapons(Item):
    
    def __init__(self, name, value, rarity, _type, description, attack, magic_attack, crit_chance, crit_damage, state):
        super().__init__(name, value, rarity, _type, description)
        self.attack = attack
        self.magic_attack = magic_attack
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.state = state

    def equip(self, player):
        if not self.state:
            player.magic_attack += self.magic_attack
            player.attack += self.attack
            player.crit_damage += (player.attack * self.crit_chance / 100)
            player.equipped_items.append(self.name)
            self.state = True
        else:
            Screen.println("Este item ya está equipado!")
            # Agregar magic crit

    def unequip(self, player):
        if self.state:
            player.magic_attack -= self.magic_attack
            player.attack -= self.attack
            player.crit_damage -= (player.attack * self.crit_chance / 100)
            player.equipped_items.remove(self.name)
            self.state = False
            # Agregar magic crit

class Armors(Item):

    def __init__(self, name, value, rarity, _type, description, armor, magic_armor, hp_max, mana_max, state):
        super().__init__(name, value, rarity, _type, description)
        self.armor = armor
        self.magic_armor = magic_armor
        self.hp_max = hp_max    
        self.mana_max = mana_max
        self.state = state

    def equip(self, player):
        if not self.state:
            player.magic_armor += self.magic_armor
            player.armor += self.armor
            player.hp_max += self.hp_max
            player.mana_max += self.mana_max
            player.equipped_items.append(self.name)
            self.state = True
        else:
            Screen.println("Este item ya está equipado!")

    def unequip(self, player):
        if self.state:
            player.magic_armor -= self.magic_armor
            player.armor -= self.armor
            player.hp_max -= self.hp_max
            player.mana_max -= self.mana_max
            player.equipped_items.remove(self.name)
            self.state = False
        
class Shop():

    def __init__(self):
        pass

    def item_stock(self):
        return itemClasses

    def buy(self, item, player):
        if player.gold >= item.value:
            player.gold -= item.value
            player.add_to_inventory(item)
            Screen.println("Compraste {}\nTu oro restante: {}".format(item.name, player.gold))
        else:
            Screen.println("No tenés oro para comprar ese item")






#RARITY: Common, Rare, Epic, Legendary

# ENEMIES name, attack, magic_attack, armor, magic_armor, hp_max, level, exp, hp
werewolf = Monster(name="Were-Wolf", attack=5, magic_attack=0, armor=2, magic_armor=0, hp_max=150, level=1, exp=25, hp=150)
orc = Monster("Orc", 2, 0, 4, 2, 100, 1, 30, 100)
elf = Monster("Elf", 3, 3, 3, 3, 80, 1, 15, 80)
slime = Monster("Slime", 1, 0, 1, 1, 20, 1, 5, 20)
skeleton = Monster("Skeleton", 4, 0, 4, 0, 80, 1, 15, 80)
zombie = Monster("Zombie", 2, 0, 1, 0, 50, 1, 10, 50)
witch = Monster("Witch", 1, 3, 0, 2, 90, 1, 15, 90)


mobClasses = (werewolf, orc, elf, slime, skeleton, zombie, witch)


# CONSUMABLES name, value, rarity, _type, hp, mana 
hpPotion = Consumables(
    name="Small HP Potion", 
    value=5,
    rarity="common",
    _type="C",
    description="Recupera 20HP",
    hp=20,
    mana=0
    )
mpPotion = Consumables(
    name="Small Mana Potion", 
    value=5, 
    rarity="common", 
    _type="C", 
    description="Recupera 20MP",
    hp=0, 
    mana=20
    )
hpPotionPlus = Consumables(
    name="Medium HP Potion", 
    value=20, 
    rarity="common", 
    _type="C",
    description="Recupera 40 HP",
    hp=40, 
    mana=0
    )
mpPotionPlus = Consumables(
    name="Medium Mana Potion", 
    value=20, 
    rarity="common", 
    _type="C",
    description="Recupera 40MP", 
    hp=0, 
    mana=40)
hpPotionPlusPlus = Consumables(
    name="Big HP Potion", 
    value=50, 
    rarity="common", 
    _type="C", 
    description="Recupera 80HP", 
    hp=80, 
    mana=0
    )
mpPotionPlusPlus = Consumables(
    name="Big Mana Potion", 
    value=50, 
    rarity="common", 
    _type="C", 
    description="Recupera 80MP", 
    hp=0, 
    mana=80
    )

consumableClasses = {
    'Small HP Potion':hpPotion, 
    'Medium HP Potion':hpPotionPlus, 
    'Big HP Potion':hpPotionPlusPlus, 
    'Small Mana Potion':mpPotion, 
    'Medium Mana Potion':mpPotionPlus, 
    'Big Mana Potion':mpPotionPlusPlus
}

# WEAPONS name, value, rarity, _type, attack, magic_attack, crit_chance, crit_damage, state
lamuerte = Weapons(
    name="La Muerte", 
    value=500, 
    rarity="epic", 
    _type="E",
    description="Esta espada le fue dada a un rey por la mismísima Muerte, que ansiaba poder para vencer en batalla a sus más feroces enemigos, convirtiéndolo en el rey más poderoso."
                "Pero la trampa de la muerte se hizo presente, y era que cada vez que la espada asesinaba, una parte del alma del rey se unía a la espada, hasta consumirlo para siempre..", 
    attack=10, 
    magic_attack=0, 
    crit_chance=5, 
    crit_damage=15, 
    state=False
    )

weaponsClasses = {1:lamuerte}

# ARMORS name, value, rarity, _type, armor, magic_armor, hp_max, mana_max, state
dragonscale = Armors(
    name="Dragon's Scale", 
    value=500, 
    rarity="epic", 
    _type="E", 
    description="Dicen que esta armadura legendaria fue hecha con escamas del dragón ancestral Marcelo. Este dragon estaba hasta las bolas de que lo carguen todo el tiempo con el chiste facil."
                "Así que se volvio re loco y empezó a destruir todo. Vinieron los heroes polenta, lo bajaron e hicieron esta linda armadura."
                "Asi que mas te vale usarla para enfrentarte a los hermanos de Marcelo: Raul, Micho, Tito, Gordo y Cabezón",
    armor=10, 
    magic_armor=0, 
    hp_max=100, 
    mana_max=0, 
    state=False
    )

armorsClasses = {1:dragonscale}

itemClasses = [hpPotion, hpPotionPlus, hpPotionPlusPlus, mpPotion, mpPotionPlus, mpPotionPlusPlus, lamuerte, dragonscale]

