# insert 10 values into databases

import sqlite3
import pandas

ten_countries_path = "Practice-100-Python-Questions\Section-4\\ten_more_countries_91.txt"
database_file_path = "Practice-100-Python-Questions\Section-4\database.db"


data = pandas.read_csv(ten_countries_path)

conn = sqlite3.connect(database_file_path)
cur = conn.cursor()

for index,row in data.iterrows():
    print(row['Country'],row['Area'])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row['Country'],row['Area']))

conn.commit()
conn.close()