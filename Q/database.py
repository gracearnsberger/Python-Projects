import sqlite3

conn = sqlite3.connect("python.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT,  \
        col_filename TEXT, \
        col_ext TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect("python.db")

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_filename, col_ext) VALUES (?,?)", \
               ("information", ".docx") )
    cur.execute("INSERT INTO tbl_files(col_filename, col_ext) VALUES (?,?)", \
                ("Hello", ".txt") )
    cur.execute("INSERT INTO tbl_files(col_filename, col_ext) VALUES (?,?)", \
                ("myImage", ".png") )
    cur.execute("INSERT INTO tbl_files(col_filename, col_ext) VALUES (?,?)", \
                ("myMovie", ".mpg") )
    cur.execute("INSERT INTO tbl_files(col_filename, col_ext) VALUES (?,?)", \
                ("World", ".txt") )
    cur.execute("INSERT INTO tbl_files(col_filename, col_ext) VALUES (?,?)", \
                ("data", ".pdf") )
    cur.execute("INSERT INTO tbl_files(col_filename, col_ext) VALUES (?,?)", \
                ("myPhoto", ".jpg") )
    conn.commit()
conn.close()


conn = sqlite3.connect("python.db")

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_filename, col_ext FROM tbl_files WHERE col_ext = '.txt'")
    varFile = cur.fetchall()
    for item in varFile: 
        msg = "FIle Name: ()\nExtension: ()".format(item[0],item[1])
print(msg)

