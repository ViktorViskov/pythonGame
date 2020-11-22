from math import floor

# create character class
class Character:
    
    # inicilized class
    def __init__(self, name, hp, attack, defence):

        # character name
        self.name = name

        # character lvl and percent for next lvl
        self.lvl = 1
        self.toNextLvl = 100

        # character maxHp and currentHp
        self.maxHp = hp
        self.currentHp = self.maxHp

        # character attack hp
        self.attack = attack

        # character base defence
        self.defence = defence

        # attackboost value and boostlife value
        self.attackBoost = False
        self.attackBoostValue = 1.0
        self.attackBoostLife = 0

        # defenceboost value and boostlife value
        self.defenceBoost = False
        self.defenceBoostValue = 1.0
        self.defenceBoostLife = 0
