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

html_soup = BeautifulSoup(HTML, 'html.parser')


def find_item_name():
    locator = 'article.product_pod h3 a'
    item_link = html_soup.select_one(locator)
    item_name = item_link.attrs['title']
    print(item_name)


def find_item_link():
    locator = 'article.product_pod h3 a'
    item_link = html_soup.select_one(locator).attrs['href']
    print(item_link)


def get_item_price():
    locator = 'article.product_pod div.product_price p'
    item_price = html_soup.select_one(locator)
    regular_exp = "£([0-9]+\.[0-9]*)"
    matcher = re.search(regular_exp, item_price.string)
    print(matcher.group(0))
    print(matcher.group(1))


def get_item_rating():
    locator = "article.product_pod p.star-rating"
    star_rating_tag = html_soup.select_one(locator)
    classes = star_rating_tag.attrs.get('class')
    classes = [i for i in classes if i !="star-rating"]
    print(classes)


find_item_name()
find_item_link()
get_item_price()
get_item_rating()
