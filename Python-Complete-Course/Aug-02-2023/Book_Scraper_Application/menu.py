from app import books
import logging

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the Following
'b' look for best books
'c' look for cheapest books
'n' get the next available books in the catalogue
'q' to exit

'''


def print_best_books():
    logger.info("Finding best book by rating...")
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]

    for book in best_books:
        print(book)


def print_cheapest_book():
    logger.info("Finding cheap book by price...")

    cheapest_books = sorted(books, key=lambda x: x.price)[:10]

    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    logger.info("Getting next book from the generator ")
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_book,
    'n': get_next_book,
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in user_choices:
            user_choices[user_input]()
        else:
            print("Choose valid input ...")
        user_input = input(USER_CHOICE)
    logger.debug("Terminating Program")


menu()
