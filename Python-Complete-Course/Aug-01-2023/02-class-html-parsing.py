from bs4 import BeautifulSoup
import re

HTML = '''<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">       
            <div class="image_container">                   
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>              
            </div>            
            <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
            </p>  
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>       
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>   
        In stock  
</p>    
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>                
            </div>       
    </article>
</li>'''

class ParsedItemLocator:
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod div.product_price p'
    RATING_LOCATOR = "article.product_pod p.star-rating"


class ParsedItem:
    """
        class take HTML and part of it and find properties of it
        """

    def __init__(self, page):
        self.html_soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocator.NAME_LOCATOR
        item_link = self.html_soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocator.LINK_LOCATOR
        item_link = self.html_soup.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        item_price = self.html_soup.select_one(locator)
        regular_exp = "£([0-9]+\.[0-9]*)"
        matcher = re.search(regular_exp, item_price.string)
        return matcher.group(1)

    @property
    def rating(self):
        locator = ParsedItemLocator.RATING_LOCATOR
        star_rating_tag = self.html_soup.select_one(locator)
        classes = star_rating_tag.attrs.get('class')
        classes = [i for i in classes if i != "star-rating"]
        return classes


item = ParsedItem(HTML)
print(item.name)
print(item.price)
print(item.rating)
