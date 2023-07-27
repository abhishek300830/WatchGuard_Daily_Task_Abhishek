# used to store and retrieve data
# import sqlite3
from .database_connection import DatabaseConnection
from typing import List, Dict


def create_book_table() -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


# def create_book_table():
#     connection = sqlite3.connect("data.db")
#
#     cursor = connection.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
#
#     connection.commit()
#     connection.close()


def add(name, author) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))


# def add(name, author):
#     connection = sqlite3.connect("data.db")
#
#     cursor = connection.cursor()
#     cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))
#
#     connection.commit()
#     connection.close()


def get_all_books() -> List[Dict]:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")

        books = cursor.fetchall()  # [(name, author, read),(name, author, read)]
        books = [
            {
                "name": row[0],
                'author': row[1],
                'read': row[2]
            }
            for row in books
        ]
    return books


# def get_all_books():
#     connection = sqlite3.connect("data.db")
#
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM books")
#
#     books = cursor.fetchall()  # [(name, author, read),(name, author, read)]
#     books = [
#         {
#             "name": row[0],
#             'author': row[1],
#             'read': row[2]
#         }
#         for row in books
#     ]
#
#     connection.close()
#     return books

# we are not making any changes, so we don't need connection.commit() here


def mark_book_as_read(book_name) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read=1 WHERE name=?", (book_name,))


# def mark_book_as_read(book_name):
#     connection = sqlite3.connect("data.db")
#
#     cursor = connection.cursor()
#     cursor.execute("UPDATE books SET read=1 WHERE name=?", (book_name,))
#
#     connection.commit()
#     connection.close()


def delete_book(book_to_delete):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE name=?", (book_to_delete,))

# def delete_book(book_to_delete):
#     connection = sqlite3.connect("data.db")
#     cursor = connection.cursor()
#
#     cursor.execute("DELETE FROM books WHERE name=?", (book_to_delete,))
#
#     connection.commit()
#     connection.close()
