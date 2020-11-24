# 
# Import libs
# 
import utils, actions
from random import random

# 
# Variables
# 

# bot names
botNames = [
    "Elf",
    "DarkElf",
    "Kamael",
    "Loshara",
    "AppleHui",
    "Dalbayob",
    "HuiGolowa",
    "iJopa",
    "Dwarf",
    "Bandit",
    "Gopnik s iHui",
    "Gopnik bez Bluetooth",
    "Henrik",
    "Ib",
    "Chlen",
    "50 rublei ne budet",
    "Chita",
    "Cisco",
    "appleJop"   
]

# bot classes
# init
botClasses = []
# adding current classes
for char in utils.characters:
    botClasses.append(char)


# 
# Functions
# 

# bot initialization
def initBot():
    return utils.createCharacter(randomInArray(botNames),randomInArray(botClasses))

# take random element from arr
def randomInArray(array):
    return array[int(random()* len(array))]

# bot action
def botAction(bot, char):
    while True:
        # get action by random
        action = int(random() * 3) + 1

        # attack if action 1
        if action == 1:
            return actions.attack(bot,char)
        
        # if 2 attack boost
        elif action == 2 and not bot.attackBoostLife:
            return actions.activateAttackBoost(bot,30,5)
        
        # if 3 attack boost
        elif action == 2 and not bot.defenceBoostLife:
            return actions.actionActivateDefenceBoost(bot,30,5)