import sqlite3
import os

conn = sqlite3.connect("python.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_files
                 (id integer primary key, name varchar(50))""")

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg') 


for filename in fileList:
    if (filename.endswith('.txt')):
        print(filename)
        cursor.execute("""insert into tbl_files ("col_filename") values ('{}') """.format(filename))
        conn.commit()

conn.close() 



       
    
