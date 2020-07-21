#Grace Arnsberger
#File Transfer Main File

from tkinter import *
import tkinter as tk

import file_transfer_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define size and color of frame
        self.master = master
        self.master.minsize(500, 250)
        self.master.maxsize(500, 250)
        self.master.title("File Transfer")
        self.master.configure(bg="#F3F4F3")
        file_transfer_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
