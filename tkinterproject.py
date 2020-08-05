from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import time
import shutil

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)
        self.master = master
        self.master.resizable(width= False, height = False)
        self.master.geometry("{}x{}".format(500,160))
        self.master.title("Check Files")
        self.master.config(bg='lightgray')
        
    
        
        self.btnBrowseOne = tk.Button(self.master, text="Browse...", width= 15, height= 1, command = self.browse_button1)
        self.btnBrowseOne.grid(row=0, column=1, padx=(10,0), pady=(35,0), sticky=NW)
    
        
        self.btnBrowseTwo = tk.Button(self.master, text="Browse...", width= 15, height= 1, command = self.browse_button2)
        self.btnBrowseTwo.grid(row=1, column=1, padx=(10,0),pady=(10,0), sticky=NW)

        self.btnCheckFiles = tk.Button(self.master, text="File Check...", width= 15, height = 2, command = self.recent_files)
        self.btnCheckFiles.grid(row=2,column=1, padx=(10,0),pady=(10,0), sticky=NW)
        
        self.btnClose = tk.Button(self.master, text="Close Program", width= 15, height= 2, command = self.cancel)
        self.btnClose.grid(row=2,column=2, padx=(50,0),pady=(10,0), sticky=E)
    
        self.entry_1 = tk.Entry(self.master, width = 50)
        self.entry_2 = tk.Entry(self.master, width = 50)

        self.entry_1.grid(row = 0, column = 2, padx = (10, 0), pady=(35,0), rowspan = 1, columnspan = 1)
        self.entry_2.grid(row = 1, column = 2, padx = (10, 0), pady = (10,0), rowspan = 1, columnspan = 1)


    def browse_button1(self):
        self.current_directory = filedialog.askdirectory()
        self.entry_1.delete(0,END)
        self.entry_1.insert(0,self.current_directory)

    def browse_button2(self):
        self.current_directory = filedialog.askdirectory()
        self.entry_2.delete(0,END)
        self.entry_2.insert(0,self.current_directory)


    def cancel(self): 
        self.master.destroy()


    def recent_files(self):
        now = time.time()
        SECONDS_IN_DAY = 24 * 60 * 60
        before = now - SECONDS_IN_DAY
        
        source= self.entry_1.get()
        destination = self.entry_2.get()
        
        for filename in os.listdir(source):
            source_filename = os.path.join(source, filename)
            lastmodTime = os.path.getmtime(source_filename)
        if lastmodTime > before:
            destination_filename = os.path.join(destination, filename)
            shutil.move(source_filename, destination_filename)

    

if __name__ == "__main__":
    root = Tk()
    
    App = ParentWindow(root)
    root.mainloop()
