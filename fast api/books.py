from fastapi import Body, FastAPI

app = FastAPI()


BOOKS = [
    {"title": "Harry Potter", "author": "J. K. Rowling", "category": "Fantasy"},
    {
        "title": "Jurassic Park",
        "author": "Michael Crichton",
        "category": "Science Fiction",
    },
    {"title": "The Martian", "author": "Andy Weir", "category": "Science Fiction"},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "category": "Thriller"},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "category": "Thriller"},
    {
        "title": "The Fellowship of the Ring",
        "author": "J. R. R. Tolkien",
        "category": "Fantasy",
    },
    {
        "title": "A Game of Thrones",
        "author": "George R. R. Martin",
        "category": "Fantasy",
    },
]


@app.get("/status")
async def check_status():
    return {"message": "hello Abhishek"}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            book_title.pop(i)
            break


@app.get("/books/byauthor/{author}")
async def read_book_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return
