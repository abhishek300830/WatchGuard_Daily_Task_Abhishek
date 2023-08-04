from locators.books_locator import BookLocator
import re
import logging

logger = logging.getLogger("scraping.book_parser")


class BookParser:
    """
        class take HTML and part of it and find properties of it
        """
    RATINGS = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def __init__(self, parent):
        logger.debug(f"New book Parser created from `{parent}`")
        self.html_soup = parent

    def __repr__(self):
        return f"<Books {self.name}, (price: {self.price} ) ({self.rating} star)>"

    @property
    def name(self):
        logger.debug("Finding book name...")
        locator = BookLocator.NAME_LOCATOR
        item_link = self.html_soup.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f"Found book name...`{item_name}`")
        return item_name


    @property
    def link(self):
        logger.debug("Finding book link...")
        locator = BookLocator.LINK_LOCATOR
        item_link = self.html_soup.select_one(locator).attrs['href']
        logger.debug(f"Found book name...`{item_link}`")
        return item_link

    @property
    def price(self):
        logger.debug("Finding book price...")
        locator = BookLocator.PRICE_LOCATOR
        item_price = self.html_soup.select_one(locator)
        regular_exp = "£([0-9]+\.[0-9]*)"
        matcher = re.search(regular_exp, item_price.string)
        float_value = float(matcher.group(1))
        logger.debug(f"Found book name...`{float_value}`")
        return float_value

    @property
    def rating(self):
        logger.debug("Finding book rating...")
        locator = BookLocator.RATING_LOCATOR
        star_rating_tag = self.html_soup.select_one(locator)
        classes = star_rating_tag.attrs.get('class')
        rating_classes = [i for i in classes if i != "star-rating"]
        rating_number = BookParser.RATINGS.get(rating_classes[0], 0)
        logger.debug(f"Found book name...`{rating_number}`")
        return rating_number
