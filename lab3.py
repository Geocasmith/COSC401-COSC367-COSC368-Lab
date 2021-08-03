from tkinter import *
from tkinter.ttk import *
master = Tk()
c = Canvas(master, width=200, height=200)
c.pack()
c.create_line(0, 0, 200, 100)
c.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
c.create_rectangle(50, 25, 150, 75, fill="blue")
master.mainloop()
