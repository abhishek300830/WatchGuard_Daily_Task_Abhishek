from utils import database

USER_CHOICE ="""
Enter : 
'a' add a new book
'l' list all books
'm' mark a book as read
'd' delete a book
'q' quit
your choice: """

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'm':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Please Enter Correct Keyword.")
        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter Book Name : ")
    author = input("Enter Book author : ")
    database.add(name,author)


def list_books():
    books = database.get_all_books()
    for book in books:
        print(f"{book['name']} by {book['author']} , Read : {book['read']}")


def prompt_read_book():
    book_name = input("Enter Book name you want to mark Read : ")
    database.mark_book_as_read(book_name)


def prompt_delete_book():
    book_name = input("Enter Book name you want to Delete : ")
    database.delete_book(book_name)


menu()