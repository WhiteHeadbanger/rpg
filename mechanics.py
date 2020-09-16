from base_classes import mobClasses
from random import choice

def instance_mob():
    instance = choice(mobClasses)
    return instance


