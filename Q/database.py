import sqlite3
import os

conn = sqlite3.connect("python.db")

with conn:
    fileList = ('')
    cur = conn.cursor()
    cur.execute("SELECT col_filename, col_ext FROM fileList WHERE col_ext = '.txt'")
    varFile = cur.fetchall()
    

