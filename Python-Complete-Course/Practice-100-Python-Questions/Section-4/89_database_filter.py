import sqlite3

database_file_path = "Practice-100-Python-Questions\Section-4\database.db"

sqlite_connection = sqlite3.connect(database_file_path)
cursor = sqlite_connection.cursor()

cursor.execute("SELECT * FROM countries")
# cursor.execute("SELECT * FROM countries WHERE area >= 2000000")
countries_data = cursor.fetchall()

for country_data in countries_data:
    if (country_data[2] > 2000000):
        print(country_data[1])