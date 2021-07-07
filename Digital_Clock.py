from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime


def quit(*args):
    root.destroy()


def clock():
    day=datetime.datetime.now()
    day=(day.strftime("%A %B %d"))
    time = datetime.datetime.now()
    time = (time.strftime("%I:%M:%S:%p"))
    total = day +"\n"+"     "+time
    txt.set(total)

    root.after(1000, clock)


root = Tk()
root.attributes("-fullscreen", False)
root.configure(background="black")
root.bind("x", quit)
root.after(1000, clock)
root.title("DigitalClock")

font = font.Font(family='Helvetica', size=69)
txt = StringVar()
label = ttk.Label(root, textvariable=txt, font=font, foreground='white', background='black')
label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
