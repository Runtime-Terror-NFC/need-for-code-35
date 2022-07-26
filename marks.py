import pandas as pd
import sqlite3

connection = sqlite3.connect('marks.db')
cursor = connection.cursor()
table = "CREATE TABLE marks(Name VARCHAR(255),RollNo INT,Date DATE,Subject VARCHAR(255),Marks INT)"
try:
    cursor.execute(table)
except:
    exit
def store_marks(path):
    file = pd.read_csv(path)
    for i in range(len(file['Name'])):
        name = file['Name'][i]
        roll = file['Roll No'][i]
        date = file['Date'][i]
        subject = file['Subject'][i]
        marks = file['Marks'][i]
        command = "SELECT * FROM marks WHERE Name='"+name+"'"
        cursor.execute(command)
        res = cursor.fetchall()
        # print(res[0][2])
        # if(res[0]==[]):
        com = "INSERT INTO marks VALUES('"+name+"','"+str(roll)+"','"+str(date)+"','"+subject+"','"+str(marks)+"')"
        cursor.execute(com)
        # else:
        #     exit
        # print(res[0][2]==date)
    connection.commit()
