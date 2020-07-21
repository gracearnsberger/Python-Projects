#Grace Arnsberger
from tkinter import *
import tkinter as tk

import file_transfer_func


def load_gui(self):
        
    self.custom_source = StringVar()
    self.custom_source.set('Select a source file')
    self.text_source = tk.Entry(self.master, width=60, textvariable=self.custom_source)
    self.text_source.grid(row=0, column=0, rowspan=1, columnspan=2, padx=(5, 0),
                          pady=(10, 20))
    self.custom_dest = StringVar()
    self.custom_dest.set('Select a destination file')
    
    self.text_dest = tk.Entry(self.master, width=60, textvariable=self.custom_dest)
    self.text_dest.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

    self.button_source = tk.Button(self.master, text="Transfer From..", width=12, height=1,
                                   command=lambda: file_transfer_func.get_source(self))
    self.button_source.grid(row=0, column=2, padx=(10, 0), pady=(10, 20))

    self.button_dest = tk.Button(self.master, text="Transfer To..", width=12, height=1,
                                 command=lambda: file_xfer_func.get_dest(self))
    self.button_dest.grid(row=1, column=2, padx=(10, 0), pady=(10, 20))
    
    self.button_transfer = tk.Button(self.master, width=16, height=2, text="Transfer",
                                command=lambda: file_transfer_func.move_files(self, self.custom_source, self.custom_dest))
                                
    self.button_transfer.grid(row=2, column=0, padx=(0, 0), pady=(10, 10))

    self.button_done = tk.Button(self.master, width=16, height=2, text="Complete",
                                 command=lambda: file_xfer_func.close(self))
    self.button_done.grid(row=2, column=1, padx=(0, 0), pady=(10, 10))

    file_transfer_func.create_db(self)

