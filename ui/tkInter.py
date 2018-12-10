"""Tkinter test."""

import tkinter

top = Tk()

LB = Listbox(top)

LB.insert(0, "This thing")
LB.pack()

top.mainloop()