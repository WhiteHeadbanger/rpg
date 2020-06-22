from base_classes import *

# ENEMIES
werewolf = Monster("Were-Wolf", 5, 0, 2, 0, 150, 25, 1)
orc = Monster("Orc", 2, 0, 4, 2, 100, 30, 1)
elf = Monster("Elf", 3, 3, 3, 3, 80, 15, 1)

# CONSUMABLES
hpPotion = Consumables("HP Potion", 5, "common", 20, 0, "C")
mpPotion = Consumables("Mana Potion", 5, "common", 0, 20, "C")

# WEAPONS
lamuerte = Weapons("La Muerte", 50, "epic", 10, 0, 5, 15, False)

# ARMORS
dragonscale = Armors("Dragon's Scale", 50, "epic", 10, 0, 100, 0, False)

print(hpPotion)

