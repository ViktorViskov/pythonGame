# import utils
import utils
# import system comands
import os
# import actions
import actions
# Form
import Form
# bot
import bot

# define game engine
class Game:

    # initiolization
    def __init__(self):
        # create display
        self.display = Form.Form()

        # create user
        self.initUserChar()

        # create mob
        self.initMobChar()

        # start game
        self.startGame()
        
        
    
    # take data from user and create char for user
    def initUserChar(self):
        self.display.makeForm()

        # set values in form
        self.display.setInForm("Insert character name ","x:center","y:center")
        self.display.printForm()
        # take data from user
        charName = input("### ")


        # print characters
        self.printCharacterList("center", 5);

        self.display.setInForm("Insert character type ","x:center","y:center")
        self.display.printForm()
        # take data from user
        charType = input("### ")

        # creating character
        self.char = utils.createCharacter(charName,charType)


    # creating mob
    def initMobChar(self):
        self.mob = bot.initBot()
    
    # print characters
    def printCharacterList(self,x,y):
        # set value on display
        for key in utils.characters:
            # set value
            print(key)
            self.display.setInForm(key,"x:" + x,"y:" + str(y))
            # add for new line
            y += 1

    # print information about chars
    def printCharsInfo(self):

        # adding elements
        # users names and types
        self.display.setInForm("%s  %s" % (self.char.name, self.char.type), "x:2","y:1")
        self.display.setInForm("%s  %s" % (self.mob.name, self.mob.type), "x:-2","y:1")
        # lvl
        self.display.setInForm("%s - LVL   %s - to next LVL" % (self.char.lvl, self.char.toNextLvl), "x:2","y:2")
        self.display.setInForm("%s - LVL   %s - to next LVL" % (self.mob.lvl, self.mob.toNextLvl), "x:-2","y:2")
        # HP
        self.display.setInForm("%s - HP %s  Max HP" % (self.char.currentHp, self.char.maxHp), "x:2","y:3")
        self.display.setInForm("%s - Max HP  %s HP" % (self.mob.maxHp, self.mob.currentHp), "x:-2","y:3")
        # Attack and defence
        self.display.setInForm("%s - Attack  %s - Defence" % (self.char.attack, self.char.defence), "x:2","y:4")
        self.display.setInForm("%s - Defence  %s - Attack" % (self.mob.defence, self.mob.attack), "x:-2","y:4")
        # Boosts
        self.display.setInForm("%s - Life  %s - Life" % (self.char.attackBoostLife, self.char.defenceBoostLife), "x:2","y:5")
        self.display.setInForm("%s - Life  %s - Life" % (self.mob.defenceBoostLife, self.mob.attackBoostLife), "x:-2","y:5")  

    # start game
    def startGame(self):

        # take game action befor loop
        self.gameAction = -1

        # start loop
        while True:
            # clean screen
            self.display.makeForm()
            
            # exit
            if self.gameAction == 0:
                break
            
            # attack
            elif self.gameAction == 1:

                # set information about attack attack
                self.display.setInForm(actions.attack(self.char, self.mob),"x:2","y:-2")
                self.display.setInForm(bot.botAction(self.mob, self.char),"x:-2","y:-2")
            
            # activate attack boost
            elif self.gameAction == 2:
                # start boost 30% boost for 5 steps
                self.display.setInForm(actions.activateAttackBoost(self.char,30,5),"x:2","y:-2")
                self.display.setInForm(bot.botAction(self.mob, self.char),"x:-2","y:-2")
 
            # activate defence boost
            elif self.gameAction == 3:
                # start boost 30% boost for 5 steps
                self.display.setInForm(actions.actionActivateDefenceBoost(self.char,30,5),"x:2","y:-2")
                self.display.setInForm(bot.botAction(self.mob, self.char),"x:-2","y:-2")

            # add information about chars
            self.printCharsInfo()

            # print form
            self.display.printForm()

            # check HP and if some not have hp stop game and print result
            if self.mob.currentHp > 0 and self.char.currentHp > 0:

                # take game action
                self.gameAction = int(input("Insert game action "))

            else:
                
                # print winner
                self.display.setInForm("%s <<< Winner" % (self.char.name if self.char.currentHp > self.mob.currentHp else self.mob.name),"x:center","y:center")
                # print form
                self.display.printForm()
                break
            

Game()
