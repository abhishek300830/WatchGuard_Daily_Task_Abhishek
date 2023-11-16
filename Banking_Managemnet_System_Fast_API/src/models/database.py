import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()


class DBConnection:
    """This class helps to make a connection to a database"""

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("USER"),
            passwd=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        self.cursor = self.mydb.cursor()

    def get_cursor(self):
        return self.cursor

    def get_database_connection(self):
        return self.mydb


db = DBConnection()
db_cursor = db.get_cursor()
db_connection = db.get_database_connection()


def get_item(query, data):
    """get item from database

    Args:
        query (sql query): query to get item from database
        data (tuple): replace query placeholder with tuple values

    Returns:
        tuple: return a tuple of data
    """
    try:
        db_cursor.execute(query, data)
        response = db_cursor.fetchone()
        db_connection.commit()
        return response
    except mysql.connector.Error as error:
        print(error)


def get_items(query, data):
    """get items from database

    Args:
        query (sql query): query to get item from database
        data (tuple): replace query placeholder with tuple values

    Returns:
        tuple: return a tuple of data
    """
    try:
        db_cursor.execute(query, data)
        response = db_cursor.fetchall()
        db_connection.commit()
        return response
    except mysql.connector.Error as error:
        print(error)


def insert_item(query, data):
    """insert item into databases

    Args:
        query (sql query): query to update item from database
        data (tuple): replace query placeholder with tuple values

    """
    try:
        db_cursor.execute(query, data)
        db_connection.commit()
    except mysql.connector.Error as error:
        print(error)


def update_item(query, data):
    """update item into databases

    Args:
        query (sql query): query to update item from database
        data (tuple): replace query placeholder with tuple values
    """
    try:
        db_cursor.execute(query, data)
        db_connection.commit()

    except mysql.connector.Error as error:
        print(error)
