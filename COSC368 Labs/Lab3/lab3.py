from tkinter import *
from tkinter.ttk import *
import time, csv, random


class Bar:
    """Class holds all the information relating to the bars"""

    def __init__(self, distances, widths,setting):
        self.distances=distances
        self.widths=widths
        self.setting = setting
        self.counter=-1
        self.runCounter=0
        self.startTime = time.time()

    def incrementCounter(self):
        self.counter+=1
        if(self.runCounter==0):
            if (self.counter == self.setting-1):
                self.runCounter += 1
                self.counter = 0
        #Checks if user has reached the given # of clicks. Goes to next width and resets
        if(self.counter==self.setting):
            global master
            self.runCounter+=1
            self.counter=0
            if (self.runCounter == len(self.widths)):
                print("Trial completed: check your log files for your results")
                master.destroy()
                master.quit()
                quit()

    def returnCounter(self):
        return self.counter

    def returnSetting(self):
        return self.setting

    def getTime(self):
        """Gets the time difference from when the timer had started"""
        total_time = (time.time() - self.startTime) * 1000
        self.startTime = time.time()
        return total_time

def leftPress(rect1,rect2):
    if (bar.runCounter != len(bar.widths) + 1):
        global padding
        global width
        bar.incrementCounter()


        #Changes the padding each time
        padding = (width-bar.distances[bar.runCounter]+ bar.widths[bar.runCounter])/2



        # Prints to log file
        with open('lab_3_log.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(
                ['George', bar.distances[bar.runCounter], bar.widths[bar.runCounter], bar.returnSetting(), bar.getTime()])

        #Changes the bars based on what side the green bar is
        if(bar.returnCounter()% 2 == 0):
            c.coords(rect2, padding, 0, padding + bar.widths[bar.runCounter], height)
            c.coords(rect1, padding + bar.widths[bar.runCounter] + bar.distances[bar.runCounter], 0, padding + 2 * bar.widths[bar.runCounter] + bar.distances[bar.runCounter],
                 height)
        if (bar.returnCounter() % 2 != 0):
            c.coords(rect1, padding, 0, padding + bar.widths[bar.runCounter], height)
            c.coords(rect2, padding + bar.widths[bar.runCounter] + bar.distances[bar.runCounter], 0,
                     padding + 2 * bar.widths[bar.runCounter] + bar.distances[bar.runCounter], height)


def rightPress(rect1,rect2):
    ##IF CORRECT BAR: increment counter, and swap, count time.
    return

#Sets up canvas and globals variables
height=700
width=1100
master = Tk()
c = Canvas(master, width=width, height=height)
c.pack()


#Creates the bar object with the list of distances, widths and repetitions
distances = [64, 128, 256, 512]
random.shuffle(distances)
widths=[4, 8, 16, 32]
random.shuffle(widths)
repetitions = 4
bar = Bar(distances,widths,repetitions)


# Delete entries from previous runs
with open('lab_3_log.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([' '])
csvfile.close()

"""create_rectangle(x1, y1, x2, y2, fill="blue")"""
#Creates the rectangle and assignes to objects
rect1 = c.create_rectangle(1, 1, 1, 1, fill="blue")
rect2 = c.create_rectangle(1, 1, 1, 1, fill="blue")

#initialises colors
c.itemconfigure(rect1, fill='green')
c.itemconfigure(rect2, fill='blue')

padding = (width-bar.distances[bar.runCounter]+ bar.widths[bar.runCounter])/2
#Initialises locations
c.coords(rect1, padding, 0, padding+bar.widths[bar.runCounter], height)
c.coords(rect2, padding+bar.widths[bar.runCounter]+bar.distances[bar.runCounter], 0, padding+2*bar.widths[bar.runCounter]+bar.distances[bar.runCounter], height)

#Initialises button presses
c.tag_bind(rect1, "<ButtonPress-1>", lambda x: leftPress(rect1,rect2))
c.tag_bind(rect2, "<ButtonPress-1>", lambda y: rightPress(rect1,rect2))



master.mainloop()
