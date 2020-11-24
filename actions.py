import utils

# attack action
def attack(char, target):
    # check and update boosts
    utils.updateBoosts(char)
    # if defence 10 and attack 10 damage wil be 10 hitpoint, defence 20, attact 10, damage 5 hp
    damage = utils.canculateDamage(char, target)
    target.currentHp -= damage
    # print information about attack
    return "%s caused %d damage to %s" % (char.name, damage, target.name)

# activate attack boost and set life for boost
def activateAttackBoost(char, boostPercent, time):
    # check and update boosts
    utils.updateBoosts(char)
    # set new boost
    char.attackBoost = True
    char.attackBoostValue = (float(boostPercent) / 100) + 1
    char.attackBoostLife = time
    # print info in console
    return "Attack boost have been activated for %s user, for %d steps!" % (char.name, char.attackBoostLife)

# activate defence boost and set life for boost
def actionActivateDefenceBoost(char, boostPercent, life):
    # check and decrement boosts
    utils.updateBoosts(char)
    # set new boost
    char.defenceBoost = True
    char.defenceBoostValue = (float(boostPercent) / 100) + 1
    char.defenceBoostLife = life
    # print info in console
    return "Defence boost have been activated for %s user, for %d steps!" % (char.name, char.defenceBoostLife)