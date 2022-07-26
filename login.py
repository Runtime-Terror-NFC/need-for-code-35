import sqlite3
 
con = sqlite3.connect('login.db')
cursor = con.cursor()

try:
    com = "CREATE TABLE login(email NVARCHAR(255),name VARCHAR(255),password VARCHAR(255))"
    cursor.execute(com)
except:
    exit
com1  ="INSERT INTO login VALUES('daanish303@gmail.com','daanish peerkhan','daani')"
cursor.execute(com1)
con.commit()
con.close()