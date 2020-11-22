# 
# Libs
# 
import os, shutil


# Form for printing
class Form:

    # 
    # Initialization
    # 
    def __init__ (self):

        # Define terminal sizes
        self.terminalSizes()

        # Create form
        self.makeForm()

    #
    # Terminal
    # 

    # screen cleaning
    def cleanScreen(self):
        os.system("clear")

    # define terminal sizes
    def terminalSizes(self):

        # box size width
        self.formWidth = shutil.get_terminal_size().columns

        # box size height -2 elements for input data
        self.formHeight = shutil.get_terminal_size().lines - 2

    # 
    # Working with form
    # 

    # create form
    def makeForm(self):

        # make two-dimensional array
        self.tdArray = []

        # make first line
        self.tdArray.append(self.createArrayLine("┌","─","┐",self.formWidth))

        # make middle lines
        for _ in range(self.formHeight - 2):
            self.tdArray.append(self.createArrayLine("│"," ", "│",self.formWidth))

        # last line
        self.tdArray.append(self.createArrayLine("└","─","┘",self.formWidth))


    def createArrayLine(self, fistSymb, middleSymb, lastSymb, count):

        # create array
        array = []

        # append fist symbol
        array.append(fistSymb)

        # set middle symbols
        for _ in range(count - 2):
            array.append(middleSymb)
        
        # set last symbol
        array.append(lastSymb)

        # return created string
        return array


    # print array form
    def printForm(self):
        # clean screen
        self.cleanScreen()

        # create empty string
        self.stringToPrint = ""

        # adding element in string
        for row in self.tdArray:
            for item in row:
                self.stringToPrint += item
            
            # adding new line
            self.stringToPrint += "\n"

        # print string
        print(self.stringToPrint)
    
    # set data in form
    def setInForm(self, inRow, fromItem, value):
        for itemNum in range(len(value)):
            self.tdArray[inRow][fromItem + itemNum] = value[itemNum]

someData = Form()
someData.setInForm(2,10,"Loshara")
someData.setInForm(2,50,"This is cool")
someData.printForm()
