from tkinter import *
import tkinter as tk
import shutil
import os
import time

import file_transfer_func

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)
        self.master = master
        self.master.resizable(width= True, height = True)
        self.master.geometry("{}x{}".format(500,160))
        
    def gui_main(self):
        self.lbl_header = tk.Label(self.master, font=('Verdana', 20, 'italic'), text=("Transfer files recently modified"), bg="lightblue")
        self.lbl_header.grid(row=0, column=0, columnspan=6, pady=(12,12), padx=(24, 6), sticky=N)
        self.btnBrowseOne = tk.Button(self.master, text="Browse...", width= 15, height= 1, command = self.browse_button1)
        self.btnBrowseOne.grid(row=0, column=1, padx=(10,0), pady=(35,0), sticky=NW)
    
        
        self.btnBrowseTwo = tk.Button(self.master, text="Browse...", width= 15, height= 1, command = self.browse_button2)
        self.btnBrowseTwo.grid(row=1, column=1, padx=(10,0),pady=(10,0), sticky=NW)

        self.btnRetrieveFiles = tk.Button(self.master, text="Transfer From..", width= 15, height = 2, command = self.print_path)
        self.btnRetrieveFiles.grid(row=2,column=1, padx=(10,0),pady=(10,0), sticky=NW)

        self.btnSendFiles = tk.Button(self.master, text="Transfer To..", width= 15, height = 2, command = self.print_path)
        self.btnSendFiles.grid(row=2,column=2, padx=(10,0),pady=(10,0), sticky=NW)
        
        self.btnRun = tk.Button(self.master, text="Run", width= 15, height= 2, command = self.cancel)
        self.btnRun.grid(row=2,column=2, padx=(50,0),pady=(10,0), sticky=E)

        self.entry_1 = tk.Entry(self.master, width = 50)
        self.entry_2 = tk.Entry(self.master, width = 50)

        self.entry_1.grid(row = 0, column = 2, padx = (10, 0), pady=(35,0), rowspan = 1, columnspan = 1)
        self.entry_2.grid(row = 1, column = 2, padx = (10, 0), pady = (10,0), rowspan = 1, columnspan = 1)
    
        
        
if __name__ == "__main__":
    root = Tk()
    
    App = ParentWindow(root)
    root.mainloop()
