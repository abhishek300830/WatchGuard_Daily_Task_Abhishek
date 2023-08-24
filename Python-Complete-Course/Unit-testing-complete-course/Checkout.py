class Checkout:

    def __init__(self):
        self.prices = {}
        self.total = 0

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        self.total += self.prices[item]

    def calculate_area(self):
        return self.total

    def add_discount(self, item, no_of_item, price):
        pass
