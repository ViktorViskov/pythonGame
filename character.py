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

    # activate attack boost and set life for boost
    def actionActivateAttackBoost(self, boostPercent, life):
        # check and decrement boosts
        self.checkBoosts()

        self.attackBoost = True
        self.attackBoostValue = (float(boostPercent) / 100) * 1
        self.attackBoostLife = life
        # print info in console
        print("Attack boost have been activated for %s user, for %d steps!" % (self.name, self.attackBoostLife))
        
    # activate defence boost and set life for boost
    def actionActivateDefenceBoost(self, boostPercent, life):
        # check and decrement boosts
        self.checkBoosts()

        self.defenceBoost = True
        self.defenceBoostValue = (float(boostPercent) / 100) * 1
        self.defenceBoostLife = life
        # print info in console
        print("Defence boost have been activated for %s user, for %d steps!" % (self.name, self.defenceBoostLife))
        
    # attack action
    def actionAttack(self, target):
        # check and decrement boosts
        self.checkBoosts()
        # if defence 10 and attack 10 damage wil be 10 hitpoint, defence 20, attact 10, damage 5 hp
        damage = floor((self.attack * self.attackBoostValue) * (10 / (target.defence * target.defenceBoostValue)))
        target.currentHp -= damage
        # print information about attack
        print("%s caused %d damage to %s" % (self.name, damage, target.name))
    
    # updater for boosts life
    def checkBoosts(self):
        # decrementing and disabling attack boost
        if not self.attackBoostLife and self.attackBoost:
            self.attackBoostValue = 1.0
            self.attackBoost = False
        elif self.attackBoostLife:
            self.attackBoostLife -= 1

        # decrementing and disabling defence boost
        if not self.defenceBoostLife and self.defenceBoost:
            self.defenceBoost = False
            self.defenceBoostValue = 1.0
        elif self.defenceBoostLife:
            self.defenceBoostLife -= 1
