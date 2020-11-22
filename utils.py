# class for character
from character import Character
# file with avaible characters
from characterClasses import characters
# math lib
from math import floor

# canculate damage
def canculateDamage(char, target):
    # if defence 10 and attack 10 damage wil be 10 hitpoint, defence 20, attact 10, damage 5 hp
    return floor((char.attack * char.attackBoostValue) * (10 / (target.defence * target.defenceBoostValue)))

# updater for boosts life
def updateBoosts(char):
    # decrementing and disabling attack boost
    if not char.attackBoostLife and char.attackBoost:
        char.attackBoostValue = 1.0
        char.attackBoost = False
    elif char.attackBoostLife:
        char.attackBoostLife -= 1

    # decrementing and disabling defence boost
    if not char.defenceBoostLife and char.defenceBoost:
        char.defenceBoost = False
        char.defenceBoostValue = 1.0
    elif char.defenceBoostLife:
        char.defenceBoostLife -= 1

# creating char
def createCharacter(name, type):
    # create character
    return Character(name,characters[type]["HP"],characters[type]["attack"],characters[type]["defence"])


