"""Tkinter test."""

import tkinter

# Weird hack to get sibling directory for import
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from lib.dbTools import Tools as dT
from lib.claspTools import claspTools as cT

top = Tk()
LB = Listbox(top)

LB.insert(0, "This thing")
LB.pack()

top.mainloop()