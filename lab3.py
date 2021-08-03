from tkinter import *
from tkinter.ttk import *

class Bar:
    """Class holds all the information relating to the bars"""

    def __init__(self, distances, widths,setting):
        self.distances=distances
        self.widths=widths
        self.setting = setting
        self.counter=0
def leftPress(rect1,rect2):
    print("Left")
    c.coords(rect2, padding, 0, padding + bar.widths[0], height)
    c.coords(rect1, padding + bar.widths[0] + bar.distances[0], 0, padding + 2 * bar.widths[0] + bar.distances[0],
             height)

def rightPress(rect1,rect2):
    ##IF CORRECT BAR: increment counter, and swap, count time.
    print("Right")
    c.coords(rect1, padding, 0, padding + bar.widths[0], height)
    c.coords(rect2, padding + bar.widths[0] + bar.distances[0], 0, padding + 2 * bar.widths[0] + bar.distances[0],
             height)

height=700
width=700
padding = 100
master = Tk()
c = Canvas(master, width=width, height=height)
c.pack()
#c.create_line(0, 0, 200, 100, tag='cool')
#c.create_line(0, 100, 200, 0, fill="red", dash=(4, 4), tag='cool')
#Create Bar Object
bar = Bar([64, 128, 256, 512],[4, 8, 16, 32],4)

"""create_rectangle(x1, y1, x2, y2, fill="blue")"""
#Creates the rectangle and assignes to objects
rect1 = c.create_rectangle(1, 1, 1, 1, fill="blue")
rect2 = c.create_rectangle(1, 1, 1, 1, fill="blue")

#initialises colors
c.itemconfigure(rect1, fill='blue')
c.itemconfigure(rect2, fill='green')

#Initialises locations
c.coords(rect1, padding, 0, padding+bar.widths[0], height)
c.coords(rect2, padding+bar.widths[0]+bar.distances[0], 0, padding+2*bar.widths[0]+bar.distances[0], height)

#Initialises button presses
c.tag_bind(rect1, "<ButtonPress-1>", lambda x: leftPress(rect1,rect2))
c.tag_bind(rect2, "<ButtonPress-1>", lambda y: rightPress(rect1,rect2))



master.mainloop()
