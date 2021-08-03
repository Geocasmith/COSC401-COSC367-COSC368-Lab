from tkinter import *
from tkinter.ttk import *
import time, csv, random


class Block:
    """Class holds all the information relating to the blocks"""

    def __init__(self, stringBlock, style):
        self.stringBlock = stringBlock
        self.position = 0
        self.style = style
        self.startTime = time.time()
        self.blocks = [''.join(random.sample(stringBlock, len(stringBlock))),
                       ''.join(random.sample(stringBlock, len(stringBlock))),
                       ''.join(random.sample(stringBlock, len(stringBlock))),
                       ''.join(random.sample(stringBlock, len(stringBlock))),
                       ''.join(random.sample(stringBlock, len(stringBlock))),
                       ''.join(random.sample(stringBlock, len(stringBlock)))]

        self.blockCount = 0

    def incrementPosition(self):
        self.position += 1

    def printBlocks(self):
        print("Block1: " + self.blocks[0])
        print("Block2: " + self.blocks[1])
        print("Block3: " + self.blocks[2])
        print("Block4: " + self.blocks[3])
        print("Block5: " + self.blocks[4])
        print("Block6: " + self.blocks[5])

    def getLetter(self):
        """Returns the current letter or goes to next block or exits program"""
        global window
        if (self.position < 6):
            return self.blocks[self.blockCount][self.position]
        else:
            self.blockCount += 1
            if (self.blockCount == 6):
                print("Trial completed: check your log files for your results")
                quit()

            self.position = 0
            return self.blocks[self.blockCount][self.position]

    def nextLetter(self):
        """Returns the next letter"""
        if (self.position != 5):
            return self.stringBlock[self.position + 1]

    def getTime(self):
        """Gets the time difference from when the timer had started"""
        total_time = (time.time() - self.startTime) * 1000
        self.startTime = time.time()
        return total_time


def randomiseBoard():
    """Destroys buttons, makes new buttons with randomised alphabet to make new keyboard"""
    global bottomframe

    # Destroys all the buttons in the keyboard frame
    for widgets in bottomframe.winfo_children():
        widgets.destroy()

    # Randomises the alphabet and splits into rows for the keyboard
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    randomalphabet = ''.join(random.sample(alphabet, len(alphabet)))
    board = [randomalphabet[0:10], randomalphabet[10:19], randomalphabet[19:26]]

    # Creates new keyboard based on the randomised board
    rownum = 0
    for row in board:
        charnum = 0
        for ch in row:
            b = Button(bottomframe, text=ch, command=lambda x=ch: sendChar(x))
            colnum = 2 * charnum + rownum
            b.grid(row=rownum, column=colnum, columnspan=2)
            charnum += 1
        rownum += 1
    label.grid(row=0, column=0)


def sendChar(ch):
    """Method is triggered by a button press"""

    if (ch == block.getLetter()):

        # ONLY WRITES LAST ONE?
        if (block.style == "static"):
            with open('experiment_static_log.txt', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['George', block.style, block.getLetter(), (block.blockCount + 1), block.getTime()])
        else:
            with open('experiment_dynamic_log.txt', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['George', block.style, block.getLetter(), (block.blockCount + 1), block.getTime()])

                # Randomises the board
        if (block.style == "dynamic"):
            randomiseBoard()

        # Increments position in block and displays that in the frame
        block.incrementPosition()
        data.set(block.getLetter())
    else:
        print("GET SOME GLASSES!!!")


# Setting up Block

# Asks the user to enter Y/n to choose static or dynamic
val = input("Static? [Y/n]: ")
style = "dynamic"
if (val == "Y" or val == "y"):
    style = "static"

# Asks the user to enter the 6 character block
inputChars = input("Enter 6 alphabetical characters to create the blocks: ")
while (len(inputChars) != 6):
    print("You did not enter 6 characters")
    inputChars = input("Enter 6 alphabetical characters to create the blocks: ")

block = Block(inputChars, style)
block.printBlocks()
# Delete entries from previous runs
with open('log.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([' '])
csvfile.close()

# Setting up the window
window = Tk()
data = StringVar()
data.set(block.getLetter())
intVar = IntVar()

# Setting up the text display box
label = Label(window, textvariable=data)
label.grid(row=1, column=0)

# Setting up the frame. I have an outerframe so I can destroy the inner frame to remove buttons and remake keyboard
bottomframe = Frame(window)
bottomframe.grid(row=2, column=0)
bottomframe['padding'] = 5
bottomframe['relief'] = 'sunken'

# Putting buttons in the frame
board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
rownum = 0
for row in board:
    charnum = 0
    for ch in row:
        b = Button(bottomframe, text=ch, command=lambda x=ch: sendChar(x))
        colnum = 2 * charnum + rownum
        b.grid(row=rownum, column=colnum, columnspan=2)
        charnum += 1
    rownum += 1
label.grid(row=0, column=0)


# Give it the frame and have the function create a new keyboard with the letters.
# bottomframe.destoy to destoy it

def displayTargetLetter(letter):
    """Displays the current character in the Label"""
    data.set(letter)


window.mainloop()
