import mysql.connector

from src.models.context_manager import DBConnection


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