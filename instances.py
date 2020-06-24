from base_classes import Monster, Consumables, Weapons, Armors
from random import choice

#RARITY: Common, Rare, Epic, Legendary

# ENEMIES name, attack, magic_attack, armor, magic_armor, hp_max, level, exp, hp
werewolf = Monster(name="Were-Wolf", attack=5, magic_attack=0, armor=2, magic_armor=0, hp_max=150, level=1, exp=25, hp=150)
orc = Monster("Orc", 2, 0, 4, 2, 100, 1, 30, 100)
elf = Monster("Elf", 3, 3, 3, 3, 80, 1, 15, 80)
slime = Monster("Slime", 1, 0, 1, 1, 20, 1, 0, 20)
skeleton = Monster("Skeleton", 4, 0, 4, 0, 80, 1, 0, 80)
zombie = Monster("Zombie", 2, 0, 1, 0, 50, 1, 0, 50)
witch = Monster("Witch", 1, 3, 0, 2, 90, 1, 0, 90)


mobClasses = (werewolf, orc, elf, slime, skeleton, zombie, witch)


# CONSUMABLES name, value, rarity, hp, mana, _type
hpPotion = Consumables("Small HP Potion", 5, "common", 20, 0, "C")
mpPotion = Consumables("Small Mana Potion", 5, "common", 0, 40, "C")
hpPotionPlus = Consumables("Medium HP Potion ", 20, "common", 40, 0, "C")
mpPotionPlus = Consumables("Medium Mana Potion", 20, "common", 0, 40, "C")
hpPotionPlusPlus = Consumables("Big HP Potion ", 50, "common", 80, 0, "C")
mpPotionPlusPlus = Consumables("Big Mana Potion", 50, "common", 0, 80, "C")

consumableClasses = (hpPotion, hpPotionPlus, hpPotionPlusPlus, mpPotion, mpPotionPlus, mpPotionPlusPlus)

# WEAPONS name, value, rarity, attack, magic_attack, crit_chance, crit_damage, state
lamuerte = Weapons("La Muerte", 50, "epic", 10, 0, 5, 15, False)

weaponsClasses = (lamuerte)

# ARMORS name, value, rarity, armor, magic_armor, hp_max, mana_max, state
dragonscale = Armors("Dragon's Scale", 50, "epic", 10, 0, 100, 0, False)

armorsClasses = (dragonscale)

