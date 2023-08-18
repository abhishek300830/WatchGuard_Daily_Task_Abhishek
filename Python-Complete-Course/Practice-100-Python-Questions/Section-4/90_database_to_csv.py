#  export database rows to csv file
import sqlite3
import pandas

database_file_path = "Practice-100-Python-Questions\Section-4\database.db"
csv_file_path = "Practice-100-Python-Questions\Section-4\csv_file_generated_90.csv"

sqlite_connection = sqlite3.connect(database_file_path)
cursor = sqlite_connection.cursor()

cursor.execute("SELECT * FROM countries WHERE area >= 2000000")
countries_data = cursor.fetchall()

sqlite_connection.close()

df = pandas.DataFrame.from_records(countries_data)
df.columns = ["Rank","Country","Area","Population"]
df.to_csv(csv_file_path)