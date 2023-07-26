# used to store and retrive data 
#  structure of txt file is 
# name,author,read\n

file_path =r'Python-Complete-Course\July-26-2023\MileStoneProject-usingCSV\utils\books.csv'

# create a file if not exist 
# def create_book_table():
#     with open(file_path,'w'):
#         pass

def add(name , author):
    with open(file_path,'a') as book_file:
        book_file.write(f"{name},{author},0\n")


def  get_all_books():
    with open(file_path,'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        books = [
            {
                "name":line[0],
                'author':line[1],
                'read':line[2]
            }
            for line in lines
        ]
        return books


def mark_book_as_read(book_name):
    books = get_all_books()
    for book in books:
        if book['name'] == book_name:
            book['read'] = 1
    _save_all_books(books)


def _save_all_books(books):
    with open(file_path,'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(book_to_delete):
    books = get_all_books()
    books = [book for book in books if book['name'] != book_to_delete]
    _save_all_books(books)
