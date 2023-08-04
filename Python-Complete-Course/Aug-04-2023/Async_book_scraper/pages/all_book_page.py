import re
import logging
from bs4 import BeautifulSoup

from locators.all_book_page import AllBooksPageLocator
from parsers.book_parser import BookParser

logger = logging.getLogger("scraping.all_books_page")


class AllBooksPage:
    def __init__(self, page_content):
        logger.debug("Parsing page content with  BeautifulSoup html parser")
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f"finding all books in the page using '{AllBooksPageLocator.BOOKS}'")
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocator.BOOKS)]

    @property
    def page_count(self):
        logger.debug("Finding all number of catalogue pages available")
        content = self.soup.select_one(AllBooksPageLocator.PAGERS).string
        logger.info(f"Found the number of catalogue pages available `{content}`")
        pattern = 'page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f"Extracted the number of pages extracted `{pages}`")
        return pages
