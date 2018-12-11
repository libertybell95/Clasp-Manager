"""UI to add new project to the database."""

from tkinter import *
from tkinter.messagebox import *

import sys
import os

# Weird hack to get sibling directory for import
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from lib.dbTools import Tools

def callback():
    """Execute submit to projects table in database."""
    ID = scriptID_E.get("1.0", END)
    name = name_E.get("1.0", END)
    desc = desc_E.get("1.0", END)
    print(len(ID))

    if (len(ID) != 1) and (len(desc) != 1):
        Tools().projectsInsert(
            scriptID = ID,
            pName = name,
            pDesc = desc
        )
        
        showinfo("Add Project", "Script Added")
        top.destroy()
    else:
        showwarning("Add Project", "ID or Name are empty")

# Initialize Tk window and format window
top = Tk()
top.title("Add Project")
top.resizable(0, 0)

# Script ID input
scriptID_L = Label(top, text="Script ID: ", anchor=E, justify=RIGHT)
scriptID_L.grid(row=0, column=0)
scriptID_E = Text(top, height=1, width=30)
scriptID_E.grid(row=0, column=1)

# Name input
name_L = Label(top, text="Name: ")
name_L.grid(row=2, column=0)
name_E = Text(top, height=1, width=30)
name_E.grid(row=2, column=1)

# Description input
desc_L = Label(top, text="Description: ")
desc_L.grid(row=3, column=0)
desc_E = Text(top, height=1, width=30)
desc_E.grid(row=3, column=1)

# Submit button
MyButton1 = Button(top, text="Submit", width=10, command=callback)
MyButton1.grid(row=4,column=1)

top.mainloop()