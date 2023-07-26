# used to store and retrive data 
books = []

def add(name , author):
    books.append({'name':name, 'author':author, 'read':False})


def  get_all_books():
    return books 


def mark_book_as_read(book_name):
    for book in books:
        if book['name'] == book_name:
            book['read'] = True


def delete_book(book_to_delete):
    global books
    books = [book for book in books if book['name'] != book_to_delete]


# this is not a good practice
# def delete_book(book_to_delete):
#     for book in books:
#         if book['name'] == book_to_delete:
#             books.remove(book)
