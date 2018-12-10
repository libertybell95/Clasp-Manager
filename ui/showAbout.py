"""Shows about page."""
from tkinter.messagebox import *

def _showInfo():
    info = """
    Clasp Manager """+"v1.0"+"""

    Created by Joshua Bell (joshuakbell@gmail.com)

    for use with clasp v1.6.0
    """
    showinfo(
        title = "About",
        message = info
    )