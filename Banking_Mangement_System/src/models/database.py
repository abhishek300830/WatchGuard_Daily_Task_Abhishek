import os
import mysql.connector

from dotenv import load_dotenv
load_dotenv()


class DBConnection:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("USER"),
            passwd=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.mydb.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mydb.commit()
        self.mydb.close()


def get_item(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)
            response = cursor.fetchone()
        except mysql.connector.Error as error:
            print(error)
        return response


def get_items(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)
            response = cursor.fetchall()
        except mysql.connector.Error as error:
            print(error)
        return response


def insert_item(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)
        except mysql.connector.Error as error:
            print(error)


def update_item(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)
        except mysql.connector.Error as error:
            print(error)
