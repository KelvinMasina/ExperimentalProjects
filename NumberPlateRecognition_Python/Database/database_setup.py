import sqlite3

connection = sqlite3.connect('SmartGateSys.db')
cur = connection.cursor()
cur.execute("CREATE TABLE Users(UserID INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, Email TEXT, Password TEXT)")
connection.commit()
connection.close()