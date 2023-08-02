import requests
import logging

import pages
from pages.all_book_page import AllBooksPage

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger("scraping")

logger.info("Loading Books List ...")

page_content = requests.get("https://books.toscrape.com").content
page = AllBooksPage(page_content)

books = page.books

for page_no in range(1, 50):
    url = f"https://books.toscrape.com/catalogue/page-{page_no + 1}.html"
    page_content = requests.get(url).content
    logger.debug("Creating all book page from Page content.")
    page = AllBooksPage(page_content)
    books.extend(page.books)

# run menu file to run program
