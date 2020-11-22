# import utils
import utils
# import system comands
import os
#import actions
import actions

# define game engine
class Game:

    # initiolization
    def __init__(self):

        # create user and mob
        self.initUserChar()
        self.initMobChar()
        self.printControlInfo()
        self.startGame()
        
        
    
    # take data from user and create char for user
    def initUserChar(self):
        # clean screen
        os.system("clear")
        charName = input("Insert character name ")
        charType = input("Insert character type ")
        self.char = utils.createCharacter(charName,charType)
    
    # creating mob
    def initMobChar(self):
        self.mob = utils.createCharacter("Dark Elf","Mag")

    # print game controls
    def printControlInfo(self):

        gameContol = '''
        Hello in mini RPG game!
        1 -> Attack
        2 -> Use attack boost
        3 -> Use defence boost
        0 -> stop game
        '''

        print(gameContol)

    # update screen
    def scrUpd(self):
        os.system("clear")

    # print information about characters
    def printCharsInfo(self):
        userData = self.char
        mobData = self.char
        formatString = '''
User                                    Mob
%s                                      %s
%s - LVL  %s - to next LVL              %s - LVL  %s - to next LVL
%s - Max HP  %s HP                      %s - Max HP  %s HP
%s - Attack  %s Defence                 %s - Attack  %s Defence
%s - Atk boost  %s Rest                 %s - Atk boost  %s Rest
%s - Def boost  %s Rest                 %s - Def boost  %s Rest
        ''' % (userData.name, mobData.name, userData.lvl, userData.toNextLvl, mobData.lvl, mobData.toNextLvl, userData.maxHp, userData.currentHp, mobData.maxHp, mobData.currentHp, userData.attack, userData.defence, mobData.attack, mobData.defence,userData.attackBoost, userData.attackBoostLife, mobData.attackBoost, mobData.attackBoostLife, userData.defenceBoost, userData.defenceBoostLife, mobData.defenceBoost, mobData.defenceBoostLife)
        print(formatString)
    


    # start game
    def startGame(self):
        # testing action 
        # init action
        actions.attack(self.mob, self.char)

        # take game action befor loop
        self.gameAction = int(input("Insert game action "))

        # start loop
        while self.gameAction or (self.mob.currentHp <= 0 or self.char.currentHp <= 0):
            # clean screen
            self.scrUpd()
            # print information
            self.printCharsInfo()
            # attack
            if self.gameAction == 1:
                actions.attack(self.char, self.mob)
                actions.attack(self.mob, self.char)
            self.gameAction = int(input("Insert game action "))
            

Game()
