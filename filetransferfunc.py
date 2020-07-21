#Grace Arnsberger
#File Transfer Practice Using Python
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import datetime
import os
import shutil
import sqlite3
import time


def create_db(self):
    conn = sqlite3.connect('file_transfer.db')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS timestamps(unix REAL)")
        conn.commit()
        c.close()
    conn.close()

def read_db(self):
    conn = sqlite3.connect('file_transfer.db')
    with conn:
        c = conn.cursor()
        c.execute("SELECT MAX(unix) FROM timestamps")
        most_recent = c.fetchone()[0]
        most_recent = time.ctime(most_recent)
        c.close()
    conn.close()

        self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
        self.label_print.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

    read_db(self)


def get_source(self):
    self.text_source.delete(0, 50)
    self.custom_source = filedialog.askdirectory()
    self.text_source.insert(0, self.custom_source)


def get_dest(self):
    self.text_dest.delete(0, 50)
    self.custom_dest = filedialog.askdirectory()
    self.text_dest.insert(0, self.custom_dest)


def move_files(self, source, destination):
    now = datetime.datetime.now()
    before = now - datetime.timedelta(hours=24)
    print('The following files were recentley edited in the last 24 hours: ')

    for files in os.listdir(source):
        if files.endswith('.txt'):
            path = os.path.join(source, files)
            st = os.stat(path)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                print('{} ~ last modified {}'.format(path, mtime))
                file_source = os.path.join(source, files)
                file_destination = os.path.join(destination, files)
                shutil.move(file_source, file_destination)
                print("\tMoved {} to {}.\n".format(files, destination))

    current_time = time.time()
    conn = sqlite3.connect('file_transfer.db')
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO timestamps VALUES({})".format(current_time))
        conn.commit()
        c.close()
    conn.close()

    messagebox.showinfo("File Transfer", "Files moved successfully!")

    def read_db(self):
        conn = sqlite3.connect('file_transfer.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT MAX(unix) FROM timestamps")
            most_recent = c.fetchone()[0]
            most_recent = time.ctime(most_recent)
            c.close()
        conn.close()

        self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
        self.label_print.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

    read_db(self)
