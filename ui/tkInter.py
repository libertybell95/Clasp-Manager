"""Tkinter test."""

import tkinter
from tkinter.tix import *

top = Tk()

LB = Listbox(top)

LB.insert(0, "This thing")
LB.pack()

top.mainloop()