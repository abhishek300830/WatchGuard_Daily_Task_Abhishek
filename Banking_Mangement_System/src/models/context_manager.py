import mysql.connector


class DBConnection:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="@MAnukul3008#",
            database="banking_management_system"
        )
        self.cursor = self.mydb.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mydb.commit()
        self.mydb.close()
