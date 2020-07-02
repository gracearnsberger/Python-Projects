import sqlite3
import os

conn = sqlite3.connect("python.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_files
                 (id integer primary key, name varchar(50))
          """)

## change the path
path = 'C:\Python Projects\Q'

for file in os.listdir(path):
    if file.endswith('.txt'):
        print(file)
        cursor.execute("""insert into tbl_files (name) values ('{}') """.format(file))
        conn.commit()

conn.close()      
