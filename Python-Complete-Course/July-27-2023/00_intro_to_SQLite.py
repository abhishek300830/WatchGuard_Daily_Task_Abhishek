# making connection of sqlite database

import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("your sql query here...")
connection.commit()

connection.close()
