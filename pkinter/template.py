import tkinter as tk
from tkinter import ttk

#link

__title__ = "Template"
__version__ = "1.0.2"
__author__ = "DeflatedPickle"

class Template (ttk.Frame):
    """
            -----DESCRIPTION-----

            -----USAGE-----

            -----CONTENTS-----
    ---VARIABLES---

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    """
    def __init__ (self, parent, *args):
        ttk.Frame.__init__ (self, parent, *args)

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    temp = Template (root)
    temp.pack (expand = True, padx = 5, pady = 5)
    root.mainloop ()
