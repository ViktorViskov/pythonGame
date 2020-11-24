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
    
    # set data in form (from left posX must be positive, from right negative, top posY positive, bottom posY negative, center element in center)
    def setInForm(self, strToPrint, *optionsArr):

        # define position variables
        position = self.defPosition(optionsArr, len(strToPrint))

        # inset string in position
        for symbNum in range(len(strToPrint)):
            self.tdArray[position[1]][position[0] + symbNum] = strToPrint[symbNum]
    
    # 
    # Base utils
    # 

    # define option from array and return position
    def defPosition(self ,optionsArr ,sizeOfString = 0):
        position = [0,0]

        # start loop for define position
        for option in optionsArr:
            # convert string to arr
            convertedArr = option.split(":")

            # defining position

            # if x (horizontal)
            if convertedArr[0] == "x":

                # defining value

                # if center
                if convertedArr[1] == "center":
                    position[0] = int((self.formWidth) / 2 - (sizeOfString / 2))
                    # next iteration
                    continue

                # if value >= 0 element must stay in left side
                elif int(convertedArr[1]) >= 0:
                    position[0] = int(convertedArr[1])
                    # next iteration
                    continue
                
                # if value < 0 element must stay in right side
                elif int(convertedArr[1]) < 0:
                    position[0] = self.formWidth + int(convertedArr[1]) - sizeOfString
                    # next iteration
                    continue
                else:
                    print("Incorect input in defPosition in convertedArr[1]")
            
            # if all another values but not x (Dy default y)
            else:

                # if center
                if convertedArr[1] == "center":
                    position[1] = int((self.formHeight) / 2)
                    # next iteration
                    continue

                # if value >= 0 element must stay in top
                elif int(convertedArr[1]) >= 0:
                    position[1] = int(convertedArr[1])
                    # next iteration
                    continue
                
                # if value < 0 element must stay in bottom
                elif int(convertedArr[1]) < 0:
                    position[1] = self.formHeight + int(convertedArr[1])
                    # next iteration
                    continue
                else:
                    print("Incorect input in defPosition in convertedArr[1]")
        
        # return position array
        return position

